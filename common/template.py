from jinja2 import Environment, FileSystemLoader
import app_config


class Jinja:
    def __init__(self, template, file_type="html"):
        self.loader   = Environment(loader=FileSystemLoader(app_config.app.get("path")))
        self.template = self.loader.get_template("{0}.{1}".format(template, file_type))

    def render(self, context={}):
        return self.template.render(context)