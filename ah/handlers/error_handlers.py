# HTTP errors will only be called when ah_settings.debug is True. 

def HTTP_404(request, response, exception):
    response.out.write("404")
    response.set_status(404)

def HTTP_500(request, response, exception):
    response.out.write("500")
    response.set_status(500)

    