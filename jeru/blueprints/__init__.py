from .auth import bp
from .product import bp as p_bp


def init_app(app):
    """register blueprints"""
    app.register_blueprint(bp)
    app.register_blueprint(p_bp)
