#!/usr/bin/env python3
"""Merge SLR search results with snowballing results and de-duplicate.

Example:
    python merge_slr.py slr_consolidated_results.xlsx snowball_out.csv -o merged.xlsx
"""
import argparse
import re
import sys
from pathlib import Path

import pandas as pd

EXCEL_CELL_LIMIT = 32767


def load(path: Path, origin: str) -> pd.DataFrame:
    df = pd.read_csv(path) if path.suffix.lower() == ".csv" else pd.read_excel(path)
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]  # drop stray index cols
    df["origin"] = origin
    return df


def norm_doi(s: pd.Series) -> pd.Series:
    return (s.astype("string").str.lower().str.strip()
            .str.replace(r"^https?://(dx\.)?doi\.org/", "", regex=True)
            .replace("", pd.NA))


def norm_title(s: pd.Series) -> pd.Series:
    return (s.astype("string").str.lower()
            .str.replace(r"[^a-z0-9]", "", regex=True).replace("", pd.NA))


def join_unique(vals):
    return ";".join(dict.fromkeys(str(v) for v in vals if pd.notna(v)))


def merge(dfs, dedupe=True):
    df = pd.concat(dfs, ignore_index=True)
    n_in = len(df)
    if not dedupe:
        return df, n_in
    # Key: normalized DOI, fallback normalized title, fallback row id
    key = norm_doi(df["doi"]).fillna("t:" + norm_title(df["title"]))
    key = key.fillna(pd.Series("r:" + df.index.astype(str), index=df.index))
    df["_key"] = key
    agg = {c: "first" for c in df.columns if c != "_key"}  # first non-null wins
    agg.update(source_db=join_unique, origin=join_unique)
    out = df.groupby("_key", sort=False).agg(agg).reset_index(drop=True)
    out["n_merged"] = df.groupby("_key", sort=False).size().values
    return out, n_in


def save(df: pd.DataFrame, path: Path):
    if path.suffix.lower() == ".csv":
        df.to_csv(path, index=False)
        return
    obj = df.select_dtypes(include=["object", "string"]).columns
    too_long = df[obj].apply(lambda c: c.astype(str).str.len() > EXCEL_CELL_LIMIT).sum().sum()
    if too_long:
        print(f"warning: truncated {too_long} cells to Excel's {EXCEL_CELL_LIMIT}-char limit",
              file=sys.stderr)
        df[obj] = df[obj].apply(lambda c: c.where(c.isna(), c.astype(str).str[:EXCEL_CELL_LIMIT]))
    df.to_excel(path, index=False, sheet_name="Merged")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("inputs", nargs="+", type=Path,
                   help="Input files (.xlsx/.csv). Earlier files take priority on conflicts.")
    p.add_argument("-o", "--output", type=Path, default=Path("merged.xlsx"),
                   help="Output file (.xlsx or .csv). Default: merged.xlsx")
    p.add_argument("--labels", nargs="+",
                   help="Origin label per input (default: file stem)")
    p.add_argument("--no-dedupe", action="store_true", help="Concatenate only")
    a = p.parse_args(argv)

    labels = a.labels or [f.stem for f in a.inputs]
    if len(labels) != len(a.inputs):
        p.error("--labels must match number of inputs")

    dfs = [load(f, l) for f, l in zip(a.inputs, labels)]
    for f, d in zip(a.inputs, dfs):
        print(f"{f.name}: {len(d)} rows")
    out, n_in = merge(dfs, dedupe=not a.no_dedupe)
    save(out, a.output)
    print(f"{n_in} rows in -> {len(out)} rows out ({n_in - len(out)} duplicates merged) -> {a.output}")


if __name__ == "__main__":
    main()