from src_1.parser import parser_line, parser_file


def test_parse_line_success():
    line = '192.168.1.100 - - [18/Jul/2026:10:15:23 +0000] "GET /api/users HTTP/1.1" 200 1234'
    result = parser_line(line)
    assert result is not None
    assert result["ip"] == "192.168.1.100"
    assert result["time"] == "18/Jul/2026:10:15:23 +0000"
    assert result["method"] == "GET"
    assert result["status"] == 200
    assert result["size"] == 1234


def test_parse_line_invalid():
    assert parser_line(" ") is None
    assert parser_line("not a log line") is None

def test_parse_file_count():
    records = parser_file("sample_data/access.log")
    assert len(records) == 100