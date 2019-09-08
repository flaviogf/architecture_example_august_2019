import uuid

from flask import Blueprint, jsonify, request

from easyagro.budgets.schemas import store_budget
from easyagro.decorators import transational
from easyagro.extensions import db, mail, sms
from easyagro.models import Budget, BudgetItem, Delivery

blueprint = Blueprint('budgets', __name__)


@blueprint.route('/api/v1/budgets', methods=['POST'])
@transational()
def store():
    errors = store_budget.validate(request.json)

    if errors:
        return jsonify({'data': '', 'errors': errors}), 400

    uid = str(uuid.uuid4())
    name = request.json.get('name')
    email = request.json.get('email')
    phone = request.json.get('phone')
    items = request.json.get('items')

    delivery = (Delivery
                .query
                .filter(Delivery.name == request.json.get('delivery'))
                .first())

    delivery_name, delivery_value = ((delivery.name, delivery.value)
                                     if delivery else
                                     ('withdrawal', 0))

    items = [BudgetItem(uid=str(uuid.uuid4()),
                        name=item.get('name'),
                        quantity=item.get('quantity'),
                        price=item.get('price'),
                        total=item.get('quantity') * item.get('price'))
             for item in items]

    subtotal = sum([item.total for item in items])

    budget = Budget(uid=uid,
                    name=name,
                    email=email,
                    phone=phone,
                    subtotal=subtotal,
                    delivery_name=delivery_name,
                    delivery_value=delivery_value,
                    total=subtotal + delivery_value)

    budget.items.extend(items)

    db.session.add(budget)

    mail.send(from_='',
              to='',
              subject='',
              content='')

    sms.send(from_='',
             to='',
             content='')

    return jsonify({'data': budget.uid, 'errors': []}), 201
