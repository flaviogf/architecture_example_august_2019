import logging

logger = logging.getLogger('easyagro')


class SendGridEmailNotificationGateway:
    def notify(self, budget):
        logger.info(f'SendGridEmailNotificationGateway::notify {budget.uid}')


class SendGridSmsNotificationGateway:
    def notify(self, budget):
        logger.info(f'SendGridSmsNotificationGateway::notify {budget.uid}')
