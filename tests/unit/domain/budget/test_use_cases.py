from unittest.mock import Mock

from easyagro.domain.budget.entities import Budget
from easyagro.domain.budget.use_cases import CreateBudget


class TestCreateBudget:
    def test_should_return_output_values_with_a_new_budget_when_budget_is_created(self):
        budget_database_gateway = Mock()

        budget_notification_gateway = Mock()

        use_case = CreateBudget(budget_database_gateway=budget_database_gateway,
                                budget_notifications_gateway=[budget_notification_gateway])

        input_values = CreateBudget.InputValues(name='Barry',
                                                email='flash@dc.com',
                                                phone='16999999999',
                                                items=[
                                                    {
                                                        'name': 'coffee',
                                                        'quantity': 10,
                                                        'price': 500
                                                    }
                                                ],
                                                delivery='normal')

        output_values = use_case.execute(input_values=input_values)

        budget = output_values.budget

        assert isinstance(budget, Budget)
        assert 'Barry' == budget.customer.name
        assert 'flash@dc.com' == budget.customer.email
        assert '16999999999' == budget.customer.phone
        assert 1 == len(budget.items)
        assert 'coffee' == budget.items[0].name
        assert 10 == budget.items[0].quantity
        assert 500 == budget.items[0].price
        assert 'normal' == budget.delivery.name

    def test_should_save_budget_on_database(self):
        budget_database_gateway = Mock()

        budget_notification_gateway = Mock()

        use_case = CreateBudget(budget_database_gateway=budget_database_gateway,
                                budget_notifications_gateway=[budget_notification_gateway])

        input_values = CreateBudget.InputValues(name='Barry',
                                                email='flash@dc.com',
                                                phone='16999999999',
                                                items=[
                                                    {
                                                        'name': 'coffee',
                                                        'quantity': 10,
                                                        'price': 500
                                                    }
                                                ],
                                                delivery='normal')

        output_values = use_case.execute(input_values=input_values)

        budget = output_values.budget

        budget_database_gateway.save.assert_called_with(budget)

    def test_should_notify_budget_creation(self):
        budget_database_gateway = Mock()

        budget_notification_gateway = Mock()

        use_case = CreateBudget(budget_database_gateway=budget_database_gateway,
                                budget_notifications_gateway=[budget_notification_gateway])

        input_values = CreateBudget.InputValues(name='Barry',
                                                email='flash@dc.com',
                                                phone='16999999999',
                                                items=[
                                                    {
                                                        'name': 'coffee',
                                                        'quantity': 10,
                                                        'price': 500
                                                    }
                                                ],
                                                delivery='normal')

        output_values = use_case.execute(input_values=input_values)

        budget = output_values.budget

        budget_notification_gateway.notify.assert_called_with(budget)
