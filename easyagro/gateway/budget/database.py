import logging

from easyagro.gateway.extensions import db
from easyagro.gateway.models import Budget, BudgetItem

logger = logging.getLogger('easyagro')


class SqlAlchemyBudgetDatabaseGateway:
    def save(self, budget):
        items = [BudgetItem(uid=item.uid,
                            name=item.name,
                            quantity=item.quantity,
                            price=item.price,
                            total=item.total)
                 for item in budget.items]

        budget = Budget(uid=budget.uid,
                        name=budget.customer.name,
                        email=budget.customer.email,
                        phone=budget.customer.phone,
                        subtotal=budget.subtotal,
                        delivery_name=budget.delivery.name,
                        delivery_value=budget.delivery.value,
                        total=budget.total)

        budget.items.extend(items)

        db.session.add(budget)

        logger.info(f'SqlAlchemyBudgetDatabaseGateway::save {budget.uid}')
