from dataclasses import dataclass
from typing import List

from easyagro.domain.budget.entities import Budget, Item
from easyagro.domain.budget.value_objects import Customer, Delivery


class CreateBudget:
    def __init__(self, budget_database_gateway, budget_notifications_gateway):
        self._budget_database_gateway = budget_database_gateway
        self._budget_notifications_gateway = budget_notifications_gateway

    def execute(self, input_values):
        customer = Customer.new(name=input_values.name,
                                email=input_values.email,
                                phone=input_values.phone)

        items = [Item.new(name=item['name'],
                          quantity=item['quantity'],
                          price=item['price']) for item in input_values.items]

        delivery = Delivery.new(delivery=input_values.delivery)

        budget = Budget.new(customer=customer,
                            items=items,
                            delivery=delivery)

        self._budget_database_gateway.save(budget)

        for notification_gateway in self._budget_notifications_gateway:
            notification_gateway.notify(budget)

        return CreateBudget.OutputValues(budget=budget)

    @dataclass
    class InputValues:
        name: str
        email: str
        phone: str
        items: List
        delivery: str

    @dataclass
    class OutputValues:
        budget: Budget
