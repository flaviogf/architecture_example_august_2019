from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/swagger')
    def swagger():
        return render_template('swagger.html')

    return app
