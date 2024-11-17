import jinja2
from jinja2_simple_tags import StandaloneTag

from src.config import CONFIG


class StaticExtension(StandaloneTag):
    """Extension that returns static file path"""

    tags = {'static'}

    @staticmethod
    def render(path):
        return f'http://localhost:{CONFIG.static_port}/{path}'


TEMPLATE_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(CONFIG.templates_dir),
    extensions=[StaticExtension],
)


def render(template_name, **context):
    """Render a template with the given context"""

    return TEMPLATE_ENV.get_template(template_name).render(**context)
