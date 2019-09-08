from flask import Flask, render_template

import logging
import logging.config

logging.config.fileConfig('log.ini')


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    from easyagro.gateway import budget
    app.register_blueprint(budget.views.blueprint)

    from easyagro.gateway.extensions import db, mail, sms
    db.init_app(app)
    mail.init_app(app)
    sms.init_app(app)

    @app.route('/')
    @app.route('/swagger')
    def swagger():
        return render_template('swagger.html')

    return app
