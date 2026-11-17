import argparse

from src_1.parser import parser_file
from src_1.report import generate_report


def main():
    parser = argparse.ArgumentParser(description="Analyze Nginx access logs")
    parser.add_argument("logfile", help="Path to an Nginx access log")
    parser.add_argument(
        "--top-ips", type=int, default=5, help="Number of top client IPs (default: 5)"
    )
    parser.add_argument("--output", help="Optional output report path")
    args = parser.parse_args()

    if args.top_ips < 1:
        parser.error("--top-ips must be a positive integer")

    records = parser_file(args.logfile)
    report = generate_report(records, top_ips=args.top_ips)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
