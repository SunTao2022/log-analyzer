from src_1.parser import parser_file
from src_1.analyzer import top_n , top_5xx_endpoints , analyze_status_code

def generate_report(records:list[dict]) -> str:
    status = analyze_status_code(records)
    top_ips = top_n(records , "ip", 5)
    top_endpoints = top_n(records , "path", 5)
    top_errors = top_5xx_endpoints(records , 3)

    lines = []
    lines.append("log analysis report")
    lines.append("=" * 40)
    lines.append(f"total of request:{status['total']}")

    lines.append("status code distribution")
    for code, count in status["counts"].items():
        pct = status["percentages"][code]
        bar = "█" * int(pct//5)
        lines.append(f"{code}:{count:4d} ({pct:5.1f}%) {bar}")
    lines.append(" ")

    lines.append("TOP 5 ips source")
    for ip, count in top_ips:
        lines.append(f"{ip:15s} - {count}times")

    lines.append("Top 5 api request")
    for path, count in top_endpoints:
        lines.append(f"{path:20s} - {count}times")

    lines.append("most api port with 5xx")
    for port, count in top_errors:
        lines.append(f"{port:20s} - {count}times")

    return "\n".join(lines)
    
