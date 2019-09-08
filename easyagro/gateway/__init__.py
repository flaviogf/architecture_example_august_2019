from flask import Flask, render_template


def create_app(config):
    app = Flask(__name__)

    from easyagro.gateway import budget
    app.register_blueprint(budget.views.blueprint)

    @app.route('/')
    @app.route('/swagger')
    def swagger():
        return render_template('swagger.html')

    return app
