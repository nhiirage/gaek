import ah_settings
from handlers import *
from ah.handlers import *
from webapp2 import WSGIApplication, Route
from webapp2_extras.routes import PathPrefixRoute, RedirectRoute, DomainRoute

app = WSGIApplication(
    [
        Route(r'/', handler=home_handler.HomeHandler, name='home'),
    ],
    debug = ah_settings.debug,
    config = ah_settings.config
)

if not ah_settings.debug:
    app.error_handlers[404] = 