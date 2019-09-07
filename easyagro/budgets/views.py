import uuid

from flask import Blueprint, jsonify, request

from easyagro.budgets.schemas import store_budget
from easyagro.decorators import transational
from easyagro.extensions import db, mail, sms
from easyagro.models import Budget, BudgetItem, DeliveryType

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

    delivery_type = (DeliveryType
                     .query
                     .filter(DeliveryType.name == request.json.get('delivery_type'))
                     .first())

    delivery_value = delivery_type.value if delivery_type else 0

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
