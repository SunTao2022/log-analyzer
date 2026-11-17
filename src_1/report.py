from src_1.analyzer import analyze_status_code, top_5xx_endpoints, top_n


def generate_report(records: list[dict], top_ips: int = 5) -> str:
    """Generate an Nginx log summary; top_ips controls only the client IP list."""
    status = analyze_status_code(records)
    common_ips = top_n(records, "ip", top_ips)
    top_endpoints = top_n(records, "path", 5)
    top_errors = top_5xx_endpoints(records, 3)

    lines = [
        "Nginx log analysis report",
        "=" * 40,
        f"Total requests: {status['total']}",
        "",
        "Status code distribution",
    ]
    for code, count in status["counts"].items():
        pct = status["percentages"][code]
        bar = "█" * int(pct // 5)
        lines.append(f"{code}: {count:4d} ({pct:5.1f}%) {bar}")

    lines.extend(["", f"Top {top_ips} client IPs"])
    for ip, count in common_ips:
        lines.append(f"{ip:15s} - {count} times")

    lines.extend(["", "Top 5 requested endpoints"])
    for path, count in top_endpoints:
        lines.append(f"{path:20s} - {count} times")

    lines.extend(["", "Top 3 endpoints returning 5xx"])
    for path, count in top_errors:
        lines.append(f"{path:20s} - {count} times")
    return "\n".join(lines)
