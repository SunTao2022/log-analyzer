from src_1.parser import parse_line, parse_file


def test_parse_line_success():
    line = '192.168.1.100 - - [18/Jul/2026:10:15:23 +0000] "GET /api/users HTTP/1.1" 200 1234'
    result = parse_line(line)
    assert result is not None
    assert result["ip"] == "192.168.1.100"
    assert result["data"] == "18/Jul/2026:10:15:23 +0000"
    assert result["method"] == "GET"
    assert result["status"] == "200"
    assert result["size"] == "1234"


def test_parse_line_invalid():
    assert parse_line(" ") is None
    assert parse_line("not a log line") is None

def test_parse_file_count():
    records = parse_file("sample_data/access.log")
    assert len(records) == 100