#!/usr/bin/env python3
"""
rtc_route_detector.py

One-shot detector for the four route shapes currently established in the
AO30-covered corpus.

Input: CSV with one row per RTC session and stage-count columns.
Rows with ao30_events == 0 are labeled NO_AO30_COVERAGE, never BASELINE_LIKE.

Typical:
  python rtc_route_detector.py rtc_stage_routes.csv --out detected_routes.csv

Labels:
  B50_LIKE
  ROUTE455_LIKE
  A29_LIKE
  BASELINE_LIKE
  OTHER_COVERED
  NO_AO30_COVERAGE

These are empirical observable-route labels for the current corpus, not
provider-secret backend route names.
"""

from __future__ import annotations
import argparse
import pandas as pd
from pathlib import Path

COUNT_COLS = [
    "thoughts_nodes",
    "reasoning_recap_nodes",
    "preamble_nodes",
    "visually_hidden_nodes",
    "checking_nodes",
    "work_status_nodes",
    "system_nodes",
    "model_editable_context_nodes",
    "tool_nodes",
    "ao30_events",
]

def yn(v) -> bool:
    try:
        return float(v) > 0
    except Exception:
        return False

def classify(r):
    if not yn(r.get("ao30_events", 0)):
        return "NO_AO30_COVERAGE"

    thoughts = yn(r.get("thoughts_nodes", 0))
    preamble = yn(r.get("preamble_nodes", 0))
    hidden = yn(r.get("visually_hidden_nodes", 0))
    checking = yn(r.get("checking_nodes", 0))
    work = yn(r.get("work_status_nodes", 0))
    tool = yn(r.get("tool_nodes", 0))

    # Minimal discriminators found against all 27 AO30-covered sessions.
    if thoughts and (not hidden) and (not work) and (not tool):
        return "B50_LIKE"
    if thoughts and hidden and work and (not tool):
        return "ROUTE455_LIKE"
    if preamble and hidden and (not checking):
        return "A29_LIKE"
    if (not preamble) and (not hidden) and (not checking):
        return "BASELINE_LIKE"
    return "OTHER_COVERED"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_csv", type=Path)
    ap.add_argument("--out", type=Path, default=Path("detected_routes.csv"))
    args = ap.parse_args()

    df = pd.read_csv(args.input_csv, low_memory=False)
    for c in COUNT_COLS:
        if c not in df.columns:
            df[c] = 0
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)

    df["detector_label"] = df.apply(classify, axis=1)
    df["detector_scope"] = "EMPIRICAL_RULES_FROM_CURRENT_27_AO30_COVERED_SESSIONS"

    priority = {
        "B50_LIKE": 1,
        "ROUTE455_LIKE": 2,
        "A29_LIKE": 3,
        "BASELINE_LIKE": 4,
        "OTHER_COVERED": 5,
        "NO_AO30_COVERAGE": 6,
    }
    df["detector_priority"] = df["detector_label"].map(priority)

    sort_cols = [c for c in ["detector_priority","case_id","rtc_id"] if c in df.columns]
    df = df.sort_values(sort_cols)
    df.to_csv(args.out, index=False)

    print(df["detector_label"].value_counts().to_string())
    print(f"\nWrote: {args.out}")

if __name__ == "__main__":
    main()
