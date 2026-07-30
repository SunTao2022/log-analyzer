import argparse
from src.parser import parse_file
from src.report import generate_report

def main():
    parser = argparse.ArgumentParser(description="Nhinx analysis tool")
    parser.add_argument("log_file" , help="log_file path")
    parser.add_argument("--top-ips" , type=int , default=5 , help="show top x , default=5")
    parser.add_argument("--output" , help="exporting report")

    args = parser.parse_args()


    records = parse_file(args.log_file)
    report = generate_report(records)


    if args.output:
        with open(args.output , "w" , encoding="utf-8") as f:
            f.write(report)
        print(f"report saved at : {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
    