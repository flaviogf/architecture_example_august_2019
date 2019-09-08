from easyagro.domain.budget.entities import BudgetItem


class TestBudgetItem:
    def test_should_total_equal_to_10_when_quantity_equal_to_5_and_price_equal_to_2(self):
        coffee = BudgetItem.new(name='coffee', quantity=5, price=2)

        assert 10 == coffee.total
