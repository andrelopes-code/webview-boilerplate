import jinja2
from jinja2_simple_tags import StandaloneTag

from src.config import CONFIG
from src.core.static import static_server


class StaticExtension(StandaloneTag):
    """Extension that returns static file path"""

    tags = {'static'}

    @staticmethod
    def render(path):
        return static_server.get_url(path)


_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(CONFIG.templates_dir),
    extensions=[StaticExtension],
)


def render(template_name, context=None):
    """Render a template with the given context"""

    return _env.get_template(template_name).render(
        **{**CONFIG.BASE_CONTEXT, **(context or {})}
    )
