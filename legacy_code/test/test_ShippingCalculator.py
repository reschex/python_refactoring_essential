from legacy_code.src.ShippingCalculator import ShippingCalculator, TestOrderGetter


def test_order_1001():
    calc=ShippingCalculator(TestOrderGetter)
    assert calc.calculate_shipping(1001) == 2.5

def test_order_1002():
    calc=ShippingCalculator(TestOrderGetter)
    assert calc.calculate_shipping(1002) == 36.8
