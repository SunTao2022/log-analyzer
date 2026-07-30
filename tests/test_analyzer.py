from src.analyzer import top_n, filter_5xx, top_5xx_endpoints


def test_top_n():
    """应该返回出现次数最多的前 N 个"""
    records = [
        {"ip": "A", "status": 200},
        {"ip": "B", "status": 500},
        {"ip": "A", "status": 200},
        {"ip": "C", "status": 200},
        {"ip": "A", "status": 500},
    ]
    result = top_n(records, "ip", 2)
    assert len(result) == 2
    assert result[0] == ("A", 3)
    assert result[1][0] in ("B", "C")


def test_filter_5xx():
    """应该只保留 status >= 500 的记录"""
    records = [
        {"ip": "A", "status": 200},
        {"ip": "B", "status": 500},
        {"ip": "C", "status": 404},
        {"ip": "D", "status": 503},
    ]
    errors = filter_5xx(records)
    assert len(errors) == 2
    assert all(r["status"] >= 500 for r in errors)


def test_top_5xx_endpoints():
    """应该在 5xx 错误中返回最多的接口"""
    records = [
        {"path": "/api/a", "status": 500},
        {"path": "/api/b", "status": 500},
        {"path": "/api/a", "status": 500},
        {"path": "/api/a", "status": 500},
        {"path": "/api/b", "status": 500},
    ]
    result = top_5xx_endpoints(records, 2)
    assert result[0] == ("/api/a", 3)
    assert result[1] == ("/api/b", 2)
