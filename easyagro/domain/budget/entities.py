import uuid

from easyagro.domain.budget.value_objects import Delivery


class Entity:
    def __init__(self, uid):
        self._uid = uid

    @property
    def uid(self):
        return self._uid


class Budget(Entity):
    def __init__(self, customer, items, delivery, uid):
        super().__init__(uid=uid)
        self._customer = customer
        self._items = tuple(items)
        self._delivery = delivery

    @staticmethod
    def new(customer, items, delivery=None, uid=None):
        return Budget(customer=customer,
                      items=items,
                      delivery=delivery or Delivery.new(),
                      uid=uid or str(uuid.uuid4()))

    @property
    def customer(self):
        return self._customer

    @property
    def items(self):
        return self._items

    @property
    def delivery(self):
        return self._delivery

    @property
    def subtotal(self):
        return sum([item.total for item in self._items])

    @property
    def total(self):
        return self.subtotal + self.delivery.value


class Item(Entity):
    def __init__(self, name, quantity, price, uid):
        super().__init__(uid=uid)
        self._name = name
        self._quantity = quantity
        self._price = price

    @staticmethod
    def new(name, quantity, price, uid=None):
        return Item(name=name,
                    quantity=quantity,
                    price=price,
                    uid=uid or str(uuid.uuid4()))

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    @property
    def price(self):
        return self._price

    @property
    def total(self):
        return self._price * self._quantity
