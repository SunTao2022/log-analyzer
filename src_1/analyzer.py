from collections import Counter


def analyze_status_code(records: list[dict]) -> dict:
    counter = Counter(record["status"] for record in records)
    total = len(records)
    return {
        "total": total,
        "counts": dict(counter.most_common()),
        "percentages": {
            status: round(count / total * 100, 1) if total else 0.0
            for status, count in counter.items()
        },
    }


def top_n(records: list[dict], field: str, n: int = 5) -> list[tuple]:
    counter = Counter(record[field] for record in records)
    return counter.most_common(n)


def filter_5xx(records: list[dict]) -> list[dict]:
    return [record for record in records if record["status"] >= 500]


def top_5xx_endpoints(records: list[dict], n: int = 3) -> list[tuple]:
    errors = filter_5xx(records)
    counter = Counter(record["path"] for record in errors)
    return counter.most_common(n)
