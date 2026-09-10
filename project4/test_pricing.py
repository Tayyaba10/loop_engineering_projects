from pricing import apply_discount

def test_apply_discount():
    # 200 total, 10% off -> should be 180
    assert apply_discount(200, 10) == 180
