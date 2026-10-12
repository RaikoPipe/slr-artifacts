"""Left anti join: keep rows of dataset_update.csv that do NOT exist in
dataset_original_snowball_merged.xlsx.

A record counts as a duplicate if ANY of these match (after normalisation):
  1. DOI          (lower-cased, 'https://doi.org/' etc. stripped)
  2. source_id    (original cell may hold several ids joined by ';')
  3. title        (lower-cased, punctuation/whitespace removed)
"""
import re
import sys
import pandas as pd

ORIG = sys.argv[1] if len(sys.argv) > 1 else "dataset_original_snowball_merged.xlsx"
UPD = sys.argv[2] if len(sys.argv) > 2 else "dataset_update.csv"
OUT = sys.argv[3] if len(sys.argv) > 3 else "dataset_update_anti_join.csv"


def norm_doi(x):
    if pd.isna(x):
        return None
    x = re.sub(r"^(https?://)?(dx\.)?doi\.org/|^doi:\s*", "", str(x).strip().lower())
    return x or None


def norm_title(x):
    if pd.isna(x):
        return None
    x = re.sub(r"[^a-z0-9]", "", str(x).lower())
    return x if len(x) >= 10 else None  # skip very short/generic titles


def split_ids(x):
    if pd.isna(x):
        return []
    return [s.strip().lower() for s in str(x).split(";") if s.strip()]


orig = pd.read_excel(ORIG)
upd = pd.read_csv(UPD)

orig_dois = set(orig["doi"].map(norm_doi).dropna())
orig_titles = set(orig["title"].map(norm_title).dropna())
orig_ids = {i for cell in orig["source_id"] for i in split_ids(cell)}

m_doi = upd["doi"].map(norm_doi).isin(orig_dois)
m_title = upd["title"].map(norm_title).isin(orig_titles)
m_id = upd["source_id"].map(lambda c: any(i in orig_ids for i in split_ids(c)))
dup = m_doi | m_title | m_id

result = upd[~dup]
result.to_csv(OUT, index=False)

print(f"update rows:        {len(upd)}")
print(f"  matched by DOI:   {m_doi.sum()}")
print(f"  matched by title: {m_title.sum()}")
print(f"  matched by id:    {m_id.sum()}")
print(f"removed (any):      {dup.sum()}")
print(f"kept -> {OUT}:  {len(result)}")