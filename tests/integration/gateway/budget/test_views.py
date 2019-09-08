class TestStore:
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
