import ah_settings
from jinja2 import Environment, FileSystemLoader


class Jinja:
    def __init__(self, template):
        self.loader   = Environment(loader=FileSystemLoader(ah_settings.app.get("path")))
        self.template = self.loader.get_template("{0}.html".format(template))

    def render(self, context={}):
        return self.template.render(context)


# Sample 