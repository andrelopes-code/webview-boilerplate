import jinja2
from src.config import CONFIG
from jinja2_simple_tags import StandaloneTag


class StaticExtension(StandaloneTag):
    tags = {'static'}

    def render(self, path):
        return f'http://{CONFIG.static_addr}:{CONFIG.static_port}/{path}'


TEMPLATE_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(CONFIG.templates_dir),
    extensions=[StaticExtension],
)


def render(template_name, **context):
    return TEMPLATE_ENV.get_template(template_name).render(**context)
