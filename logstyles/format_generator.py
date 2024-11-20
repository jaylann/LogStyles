from .base_formats import BASE_FORMATS
from .themes import THEMES
from .utils import hex_to_ansi, reset_code


def generate_format(theme_name, format_name):
    """Generates the final format string for a given theme and format."""
    if theme_name not in THEMES:
        raise ValueError(f"Theme '{theme_name}' is not defined.")
    if format_name not in BASE_FORMATS:
        raise ValueError(f"Format '{format_name}' is not defined.")

    theme = THEMES[theme_name]
    base_format = BASE_FORMATS[format_name]

    format_str = base_format.format(
        time_color=hex_to_ansi(theme['time']),
        level_color=hex_to_ansi(theme['level']),
        module_color=hex_to_ansi(theme['module']),
        message_color=hex_to_ansi(theme['message']),
        reset=reset_code()
    )
    return format_str
