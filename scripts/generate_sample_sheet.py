"""
Usage: python scripts/generate_sample_sheet.py --fastq_dir data/fastq/
Generates resources/sample_sheet.csv from paired FASTQ files.
"""
import argparse, os, re, csv


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--fastq_dir", required=True)
    p.add_argument("--out", default="resources/sample_sheet.csv")
    return p.parse_args()


def main():
    args = parse_args()
    r1_files = sorted(f for f in os.listdir(args.fastq_dir) if "_R1" in f and f.endswith(".fastq.gz"))
    rows = []
    for r1 in r1_files:
        sample = re.sub(r"_R1.*", "", r1)
        r2 = r1.replace("_R1", "_R2")
        rows.append({"sample": sample,
                     "r1": os.path.join(args.fastq_dir, r1),
                     "r2": os.path.join(args.fastq_dir, r2)})
    with open(args.out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["sample", "r1", "r2"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Written {len(rows)} samples to {args.out}")


if __name__ == "__main__":
    main()