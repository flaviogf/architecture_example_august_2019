import pytest

from easyagro.models import Budget, Delivery


class TestStore:
    @pytest.fixture(autouse=True)
    def normal_delivery(self, db):
        normal = Delivery(uid='xpto', name='normal', value=1000)
        db.session.add(normal)
        db.session.commit()
        return normal

    def test_should_return_status_201_when_budget_is_created(self, client):
        data = {
            "name": "Barry",
            "email": "flash@dc.com",
            "phone": "16999999999",
            "items": [
                {
                     "name": "coffee",
                     "quantity": 5,
                    "price": 500
                }
            ],
            "delivery": "normal"
        }

        response = client.post('/api/v1/budgets', json=data)

        assert 201 == response.status_code

    def test_should_add_budget_on_database_when_budget_is_created(self, client):
        data = {
            "name": "Barry",
            "email": "flash@dc.com",
            "phone": "16999999999",
            "items": [
                {
                     "name": "coffee",
                     "quantity": 5,
                    "price": 500
                }
            ],
            "delivery": "normal"
        }

        client.post('/api/v1/budgets', json=data)

        budget = Budget.query.first()
        assert 1 == Budget.query.count()
        assert 'Barry' == budget.name
        assert 'flash@dc.com' == budget.email
        assert 2500 == budget.subtotal
        assert 'normal' == budget.delivery_name
        assert 1000 == budget.delivery_value
        assert 3500 == budget.total

        budget_item = budget.items[0]
        assert 1 == len(budget.items)
        assert 'coffee' == budget_item.name
        assert 5 == budget_item.quantity
        assert 500 == budget_item.price
        assert 2500 == budget_item.total

    def test_should_return_status_400_when_request_is_invalid(self, client):
        data = {
            "name": "",
            "email": "flash@dc.com",
            "phone": "16999999999",
            "items": [
                {
                     "name": "coffee",
                     "quantity": 5,
                    "price": 500
                }
            ],
            "delivery": "normal"
        }

        response = client.post('/api/v1/budgets', json=data)

        assert 400 == response.status_code
