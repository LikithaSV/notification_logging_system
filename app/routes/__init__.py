from sanic import Blueprint
from app.routes.notifications_bp import notifications_bp

blueprint_group = Blueprint.group(
    notifications_bp
)
