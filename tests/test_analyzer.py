from src_1.analyzer import top_n, filter_5xx, top_5xx_endpoints

def test_top_n():
    records = [
        {"ip" : "A" , "status" : 200},
        {"ip" : "B" , "status" : 500},
        {"ip" : "A" , "status" : 200},
        {"ip" : "C" , "status" : 200},
        {"ip" : "A" , "status" : 500},
    ]

    result = top_n(records , "ip" , 2)
    assert len(result) == 2
    assert result[0] == {"A" , 3}

def test_filter_5xx():
    records = [
        {"ip" : "A" , "status" : 200},
        {"ip" : "B" , "status" : 500},
        {"ip" : "A" , "status" : 200},
        {"ip" : "C" , "status" : 200},
        {"ip" : "A" , "status" : 500},
    ]
    errors = filter_5xx(records)
    assert len(errors) == 2
    assert all(r["status"] >=500 for r in errors)

def test_top_5xx_endpoints():
    records = [
        {"path": "/api/a", "status" : 500},
        {"path": "/api/b", "status" : 500},
        {"path": "/api/a", "status" : 500},
        {"path": "/api/a", "status" : 500},
        {"path": "/api/a", "status" : 500},
    ]
    result = top_5xx_endpoints(records , 2)
    assert result[0] == {"/api/a" : 4}
    assert result[0] == {"/api/b" : 1}
