from src_1.analyzer import analyze_status_code
from src_1.report import generate_report


def test_report_respects_top_ips():
    records = [
        {"ip": "10.0.0.1", "path": "/a", "status": 200},
        {"ip": "10.0.0.1", "path": "/a", "status": 200},
        {"ip": "10.0.0.2", "path": "/b", "status": 500},
        {"ip": "10.0.0.3", "path": "/c", "status": 404},
    ]
    report = generate_report(records, top_ips=1)
    assert "Top 1 client IPs" in report
    assert "10.0.0.1" in report
    assert "10.0.0.2" not in report
    assert "10.0.0.3" not in report


def test_empty_log_status_and_report():
    result = analyze_status_code([])
    assert result == {"total": 0, "counts": {}, "percentages": {}}
    report = generate_report([])
    assert "Total requests: 0" in report
