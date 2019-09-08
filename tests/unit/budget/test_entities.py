import pytest

from easyagro.domain.budget.entities import Budget, Item
from easyagro.domain.budget.value_objects import Customer, Delivery, Withdrawal


class TestBudget:
    @pytest.fixture
    def barry(self):
        return Customer.new(name='Barry',
                            email='flash@dc.com',
                            phone='16999999999')

    @pytest.fixture
    def coffee(self):
        return Item.new(name='coffee',
                        quantity=5,
                        price=200)

    @pytest.fixture
    def tea(self):
        return Item.new(name='tea',
                        quantity=5,
                        price=1000)

    @pytest.fixture
    def normal_delivery(self):
        return Delivery.new('normal')

    def test_should_budget_have_a_customer(self, barry, coffee):
        budget = Budget.new(customer=barry,
                            items=[coffee])

        assert budget.customer.name == barry.name

    def test_should_budget_have_a_coffee_on_items(self, barry, coffee):
        budget = Budget.new(customer=barry,
                            items=[coffee])

        assert 1 == len(budget.items)
        assert 'coffee' == budget.items[0].name
        assert 5 == budget.items[0].quantity
        assert 200 == budget.items[0].price

    def test_should_budget_have_a_subtotal_equal_to_sum_of_total_items(self, barry, coffee, tea):
        items = [coffee, tea]

        budget = Budget.new(customer=barry,
                            items=items)

        assert budget.subtotal == sum([item.total for item in items])

    def test_should_budget_have_default_delivery_as_withdrawal(self, barry, coffee):
        budget = Budget.new(customer=barry,
                            items=[coffee])

        assert isinstance(budget.delivery, Withdrawal)

    def test_should_budget_have_total_equal_to_subtotal_plus_delivery_value(self, barry, coffee, normal_delivery):
        budget = Budget.new(customer=barry,
                            items=[coffee],
                            delivery=normal_delivery)

        assert budget.total == budget.subtotal + normal_delivery.value


class TestItem:
    def test_should_item_have_a_total_equal_to_1000_cents_when_quantity_equal_to_5_and_price_equal_to_200_cents(self):
        coffee = Item.new(name='coffee',
                          quantity=5,
                          price=200)

        assert 1000 == coffee.total
