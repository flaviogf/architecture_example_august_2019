from easyagro.domain.budget.value_objects import (Delivery, FastDelivery,
                                                  NormalDelivery, Withdrawal)


class TestDelivery:
    def test_should_return_a_normal_delivery_when_normal_is_passed(self):
        delivery = Delivery.new('normal')

        assert isinstance(delivery, NormalDelivery)

    def test_should_return_a_fast_delivery_when_fast_is_passed(self):
        delivery = Delivery.new('fast')

        assert isinstance(delivery, FastDelivery)

    def test_should_return_withdrawal_when_nothing_is_passed(self):
        delivery = Delivery.new()

        assert isinstance(delivery, Withdrawal)


class TestNormalDelivery:
    def test_should_normal_delivery_has_default_value_equal_to_1000_cents(self):
        delivery = NormalDelivery()

        assert 1000 == delivery.value


class TestFastDelivery:
    def test_should_fast_delivery_has_default_value_equal_to_5000_cents(self):
        delivery = FastDelivery()

        assert 5000 == delivery.value


class TestWithdrawal:
    def test_should_fast_delivery_has_default_value_equal_to_0_cents(self):
        delivery = Withdrawal()

        assert 0 == delivery.value
