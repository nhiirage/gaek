import app_config

# HTTP errors will only be called when app_config.debug is True. 

context = {
    "appname": app_config.app.get("name")
}

# bad request
def HTTP_400(request, response, exception):
    response.out.write("400")
    response.set_status(400)

# unauthorized
def HTTP_401(request, response, exception):
    response.out.write("401 Unauthorized")
    response.set_status(401)

# forbidden
def HTTP_403(request, response, exception):
    response.out.write("403 Forbidden")
    response.set_status(403)

# not found
def HTTP_404(request, response, exception):
    response.out.write("404 Not Found")
    response.set_status(404)

# not allowed
def HTTP_405(request, response, exception):
    response.out.write("405 Not Allowed")
    response.set_status(405)


# internal server error
def HTTP_500(request, response, exception):
    response.out.write("500 Internal Server Error")
    response.set_status(500)

    