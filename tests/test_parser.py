from src.parser import parse_line, parse_file


def test_parse_line_success():
    """正常日志行应该正确解析"""
    line = '192.168.1.100 - - [18/Jul/2026:10:15:23 +0000] "GET /api/users HTTP/1.1" 200 1234'
    result = parse_line(line)
    assert result is not None
    assert result["ip"] == "192.168.1.100"
    assert result["method"] == "GET"
    assert result["path"] == "/api/users"
    assert result["status"] == 200
    assert result["size"] == 1234


def test_parse_line_invalid():
    """无效行应该返回 None"""
    assert parse_line("") is None
    assert parse_line("not a log line") is None


def test_parse_file_count():
    """解析文件应该返回正确的行数"""
    records = parse_file("sample_data/access.log")
    assert len(records) == 100
