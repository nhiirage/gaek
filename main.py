import ah_settings
from handlers import *
from ah.handlers import *
from webapp2 import WSGIApplication, Route
from webapp2_extras.routes import PathPrefixRoute, RedirectRoute, DomainRoute

ah_routes = [
    Route(r'/admin', handler=admin_handler.AdminHandler, name='admin'),
]

app_routes = [   
    Route(r'/', handler=home_handler.HomeHandler, name='home'),
]


app_routes.extend(ah_routes)

app = WSGIApplication(
    app_routes,
    debug = ah_settings.debug,
    config = ah_settings.config
) 

if not ah_settings.debug:
    # bad request
    app.error_handlers[400] = error_handlers.HTTP_400
    # unauthorized 
    app.error_handlers[401] = error_handlers.HTTP_401
    # forbidden
    app.error_handlers[403] = error_handlers.HTTP_403
    # not found
    app.error_handlers[404] = error_handlers.HTTP_404
    # internal server error
    app.error_handlers[500] = error_handlers.HTTP_500