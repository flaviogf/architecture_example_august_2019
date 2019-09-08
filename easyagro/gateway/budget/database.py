import logging

logger = logging.getLogger('easyagro')


class SqlAlchemyBudgetDatabaseGateway:
    def save(self, budget):
        logger.info(f'SqlAlchemyBudgetDatabaseGateway::save {budget.uid}')
