from handlers import *
from ah.handlers import *
from webapp2 import WSGIApplication, Route
from webapp2_extras.routes import PathPrefixRoute, RedirectRoute, DomainRoute
import app_config

# DO NOT OVERRIDE 
# These are cms specific routes
ah_routes = [
    RedirectRoute(r'/ah/', admin_handler.AdminHandler, 'admin', strict_slash=True),
    PathPrefixRoute(r'/ah', 
        [
            RedirectRoute(r'/auth/', auth_handler.AuthHandler, 'auth', strict_slash=True),
            PathPrefixRoute(r'/<page>',
                [
                    RedirectRoute(r'/', admin_handler.AdminHandler, 'page', strict_slash=True),
                    RedirectRoute(r'/<kind>', admin_handler.AdminHandler, 'page-kind', strict_slash=True),
                    RedirectRoute(r'/<kind>/<id>', admin_handler.AdminHandler, 'page-kind-id', strict_slash=True),
                ]
            )
        ]
    ),
]

# APP ROUTES GOES HERE
app_routes = [
    Route(r'/', home_handler.HomeHandler, 'home'),
]

if app_config.enable_admin:
    app_routes.extend(ah_routes)

app = WSGIApplication(
    app_routes,
    debug = app_config.debug,
    config = app_config.config
)

if not app_config.debug:
    # bad request
    app.error_handlers[400] = error_handlers.HTTP_400
    # unauthorized 
    app.error_handlers[401] = error_handlers.HTTP_401
    # forbidden
    app.error_handlers[403] = error_handlers.HTTP_403
    # not found
    app.error_handlers[404] = error_handlers.HTTP_404
    # not allowed
    app.error_handlers[405] = error_handlers.HTTP_405
    # internal server error
    app.error_handlers[500] = error_handlers.HTTP_500