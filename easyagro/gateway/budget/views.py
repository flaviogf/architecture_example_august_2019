from flask import Blueprint, jsonify, request

from easyagro.domain.budget.use_cases import CreateBudget
from easyagro.gateway.budget.database import SqlAlchemyBudgetDatabaseGateway
from easyagro.gateway.budget.notification import (
    SendGridEmailNotificationGateway, SendGridSmsNotificationGateway)
from easyagro.gateway.budget.schemas import store_budget

blueprint = Blueprint('budget', __name__)


@blueprint.route('/api/v1/budgets', methods=['POST'])
def store():
    errors = store_budget.validate(request.json)

    if errors:
        return jsonify({'data': None, 'errors': errors}), 400

    budget_database_gateway = SqlAlchemyBudgetDatabaseGateway()

    budget_notifications_gateway = [SendGridEmailNotificationGateway(),
                                    SendGridSmsNotificationGateway()]

    use_case = CreateBudget(budget_database_gateway=budget_database_gateway,
                            budget_notifications_gateway=budget_notifications_gateway)

    input_values = CreateBudget.InputValues(name=request.json.get('name'),
                                            email=request.json.get('email'),
                                            phone=request.json.get('phone'),
                                            items=request.json.get('items'),
                                            delivery=request.json.get('delivery'))

    output_values = use_case.execute(input_values=input_values)

    return jsonify({'data': output_values.budget.uid, 'errors': []}), 201
