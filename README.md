# Nginx Access Log Analyzer

A small Python CLI for parsing Nginx access logs and reporting request volumes, status codes, common client IPs, requested paths, and endpoints returning HTTP 5xx errors.

This is a personal automation project, with unit tests and a GitHub Actions test workflow.

## Requirements

- Python 3.11+ (the CI uses Python 3.11)
- `pytest` to run the tests

## Run

```bash
python main.py sample_data/access.log
python main.py sample_data/access.log --output report.txt
python -m pytest tests/ -v
```

Supported options:
- `logfile`: path to an Nginx access log in the supported combined-log style.
- `--output`: save the report to a file.
- `--top-ips`: number of client IPs to display (default 5).

## Sample output

The report lists total requests, status-code distribution, the most frequent IP addresses and requested paths, and paths returning 5xx errors. Use `sample_data/access.log` to reproduce locally.

## Project structure

```text
main.py                 # CLI
src_1/parser.py         # Parse access-log lines
src_1/analyzer.py       # Aggregate and filter records
src_1/report.py         # Generate a text report
tests/                  # Pytest unit tests
sample_data/            # Sample input logs
.github/workflows/      # CI tests
Dockerfile              # Container packaging
```

## CI evidence

[Successful Python test run](https://github.com/SunTao2022/log-analyzer/actions/runs/30848998045).

## Limitations

- The parser is designed for a particular Nginx access-log layout, not all custom log formats.
- Invalid lines are skipped; it does not yet count or report rejected lines.
- This is a batch CLI rather than a continuous monitoring service.

## Author

[Tao Sun](https://www.linkedin.com/in/tao-sun-3437462b6/) · [GitHub](https://github.com/SunTao2022)
