from dataclasses import dataclass
from .backend.utils import resource_path
from pathlib import Path

TEMPLATES_DIR = Path(resource_path('frontend/templates'))


@dataclass
class Config:
    title: str
    width: int
    height: int
    debug: bool
    port: int
    resizable: bool
    min_size: tuple[int, int]
    static_dir: Path
    static_port: int
    templates_dir: Path


CONFIG = Config(
    title='Contracts',
    width=800,
    height=600,
    resizable=True,
    min_size=(400, 300),
    debug=True,
    port=9876,
    templates_dir=TEMPLATES_DIR,
    # STATIC
    static_dir=TEMPLATES_DIR / 'static',
    static_port=6789,
)
