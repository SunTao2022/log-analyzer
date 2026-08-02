import argparse
from src_1.parser import parser_file
from src_1.report import generate_report

def main():
    parser = argparse.ArgumentParser(description="Nginx log analysis tool")
    parser.add_argument("logfile" , help="path of log_file")
    parser.add_argument("--top-ips" , type=int , default=5 , help="show fitst N ips")
    parser.add_argument("--output" , help="file was exporting to ")

    args = parser.parse_args()

    records = parser_file(args.logfile)
    report = generate_report(records)

    if args.output:
        with open(args.output , "w" ,encoding="utf-8") as f:
            f.write(report)
        print(f"report was save as {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()