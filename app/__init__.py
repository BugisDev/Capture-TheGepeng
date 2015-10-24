from app.core.helper import create_app
from app.core.db import db
from app.user.views import user_views
from app.home.views import home_views
from app.user.loginmanager import login_manager

# Development Config
config = 'config.dev'
# Production Config
# config = 'config.Prod'

app = create_app(config)
db.init_app(app)
login_manager.init_app(app)

# register blueprint
app.register_blueprint(user_views)
app.register_blueprint(home_views)