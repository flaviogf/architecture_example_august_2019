import logging

from easyagro.gateway.extensions import mail, sms

logger = logging.getLogger('easyagro')


class SendGridEmailNotificationGateway:
    def notify(self, budget):
        mail.send(from_='',
                  to='',
                  subject='',
                  content='')

        logger.info(f'SendGridEmailNotificationGateway::notify {budget.uid}')


class SendGridSmsNotificationGateway:
    def notify(self, budget):
        sms.send(from_='',
                 to='',
                 content='')

        logger.info(f'SendGridSmsNotificationGateway::notify {budget.uid}')
