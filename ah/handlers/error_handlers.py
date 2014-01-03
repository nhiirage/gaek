import ah_settings

# HTTP errors will only be called when ah_settings.debug is True. 

context = {
    "appname": ah_settings.app.get("name")
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

# internal server error
def HTTP_500(request, response, exception):
    response.out.write("500 Internal Server Error")
    response.set_status(500)

    