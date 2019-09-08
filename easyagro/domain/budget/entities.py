import uuid


class BudgetItem:
    def __init__(self, name, quantity, price, uid):
        self._uid = uid
        self._name = name
        self._quantity = quantity
        self._price = price

    @staticmethod
    def new(name, quantity, price, uid=None):
        return BudgetItem(name=name,
                          quantity=quantity,
                          price=price,
                          uid=uid or str(uuid.uuid4()))

    @property
    def total(self):
        return self._price * self._quantity
