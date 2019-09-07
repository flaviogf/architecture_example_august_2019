from flask import Flask, render_template


def create_app(config='easyagro.config.Config'):
    app = Flask(__name__)

    app.config.from_object(config)

    from easyagro.extensions import db, mail, sms
    db.init_app(app)
    mail.init_app(app)
    sms.init_app(app)

    from easyagro import budgets
    app.register_blueprint(budgets.views.blueprint)

    @app.route('/')
    @app.route('/swagger')
    def swagger():
        return render_template('swagger.html')

    return app
