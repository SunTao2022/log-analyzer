from src.parser import parse_file
from src.analyzer import analyzer_status_codes , top_n , top_5xx_endpoints

def generate_report(records: list[dict]) -> str:
    status = analyzer_status_codes(records)
    top_ips = top_n(records , "ip" , 5)
    top_endpoints = top_n(records , "path" , 5)
    top_errors = top_5xx_endpoints(records, 3)

    lines = []
    lines.append("log analyze report")
    lines.append("=" * 40)
    lines.append(f"total:{status['total']}")
    lines.append("")

    lines.append("status code:")
    for code, count in status["counts"].items():
        pct = status["percentages"][code]
        bar = "█" * int(pct//5)
        lines.append(f"  {code}:{count:4d} ({pct:5.1f}%) {bar}")
    lines.append("")

    lines.append("top 5 ip")
    for ip , count in top_ips:
        lines.append(f"{ip:15s} - {count} times")
    lines.append("")

    lines.append("top 5 api request")
    for path, count in top_endpoints:
        lines.append(f"{path:20s} - {count} times")
    lines.append("")

    lines.append("5xx the api with most errors")
    for path, count in top_errors:
        lines.append(f"{path:20s} - {count} times")

    
    return "\n".join(lines)
