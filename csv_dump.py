#!/usr/bin/env python3
"""📄 csv_dump.py — extract & pretty-print Brawl Stars CSV configs.

APK csv files live in assets/csv_logic/*.csv
They are regular CSVs with ';' or ',' separators and a header row.

Usage:
    python csv_dump.py characters.csv
    python csv_dump.py --all ./csv_logic/
"""
import csv
import sys
from pathlib import Path


def sniff(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        sample = f.read(4096)
    dialect = csv.Sniffer().sniff(sample, delimiters=";,\t")
    return dialect.delimiter


def dump(path, limit=20):
    path = Path(path)
    delim = sniff(path)
    print(f"file: {path.name}  (delimiter={delim!r})")
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f, delimiter=delim)
        cols = reader.fieldnames or []
        print(f"cols ({len(cols)}): {', '.join(cols[:12])}" + (" ..." if len(cols) > 12 else ""))
        print("-" * 60)
        for i, row in enumerate(reader):
            if i >= limit:
                print(f"... (truncated, use --all-rows to see everything)")
                break
            name = row.get("Name") or row.get("name") or list(row.values())[0]
            print(f"  [{i:3}] {name}")


def main():
    args = sys.argv[1:]
    if not args:
        print("usage: python csv_dump.py <file.csv> | --all <dir>")
        sys.exit(1)
    if args[0] == "--all":
        d = Path(args[1])
        for csv_file in sorted(d.glob("*.csv")):
            dump(csv_file, limit=5)
            print()
    else:
        dump(args[0])


if __name__ == "__main__":
    main()
