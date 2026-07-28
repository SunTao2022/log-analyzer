from collections import Counter
from src.parser import parse_file

def analyzer_status_codes(records: list[dict]) -> dict:
    counter = Counter(r["status"] for r in records)
    total = len(records)
    return{
        "total" : total , 
        "counts" : dict(counter.most_common()),
        "percentages" : {k: round(v/total * 100,1) for k, v in counter.items()}
    }

def top_n(records: list[dict], field: str , n: int = 5) -> list[tuple]:
    counter = Counter(r[field] for r in records)
    return counter.most_common(n)

def filter_5xx(records: list[dict]) -> list[dict]:
    return [r for r in records if r["status"] >=500]

def top_5xx_endpoints(records: list[dict] , n: int = 3) -> list[tuple]:
    errors = filter_5xx(records)
    counter = Counter(r["path"] for r in errors)
    return counter.most_common(n)