from .auth import bp


def init_app(app):
    """register blueprints"""
    app.register_blueprint(bp)
