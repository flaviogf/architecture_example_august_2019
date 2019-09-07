from flask import Flask, render_template


def create_app(config='easyagro.config.Config'):
    app = Flask(__name__)

    app.config.from_object(config)

    from easyagro.extensions import db
    db.init_app(app)

    @app.route('/')
    @app.route('/swagger')
    def swagger():
        return render_template('swagger.html')

    return app
