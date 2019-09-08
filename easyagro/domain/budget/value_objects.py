class Customer:
    def __init__(self, name, email, phone):
        self._name = name
        self._email = email
        self._phone = phone

    @staticmethod
    def new(name, email, phone):
        return Customer(name=name,
                        email=email,
                        phone=phone)

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone


class Delivery:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @staticmethod
    def new(delivery='default'):
        return DELIVERY_TYPES[delivery]

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value


class NormalDelivery(Delivery):
    def __init__(self):
        super().__init__(name='normal', value=1000)


class FastDelivery(Delivery):
    def __init__(self):
        super().__init__(name='fast', value=5000)


class Withdrawal(Delivery):
    def __init__(self):
        super().__init__(name='withdrawal', value=0)


DELIVERY_TYPES = {
    'normal': NormalDelivery(),
    'fast': FastDelivery(),
    'default': Withdrawal()
}
