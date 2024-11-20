# logstyles/__init__.py

from .base_formats import BASE_FORMATS
from .formatter import create_formatter
from .themes import THEMES

class LogStyles:
    @staticmethod
    def get_formatter(theme_name, format_name, delimiter=None, included_parts=None, timestamp_format=None):
        """Public method to get the formatter function."""
        if theme_name not in THEMES:
            raise ValueError(f"Theme '{theme_name}' is not defined.")
        if format_name not in BASE_FORMATS:
            raise ValueError(f"Format '{format_name}' is not defined.")

        theme = THEMES[theme_name].copy()  # Copy to avoid mutating the original theme
        base_format = BASE_FORMATS[format_name]

        # Override included_parts if provided
        if included_parts is not None:
            theme['included_parts'] = included_parts

        # Override timestamp_format if provided
        if timestamp_format is not None:
            theme['timestamp_format'] = timestamp_format

        # Allow the user to set the delimiter
        if delimiter is not None:
            base_format = base_format.copy()
            base_format['delimiter'] = delimiter

        return create_formatter(theme, base_format)

    @staticmethod
    def list_themes():
        """Lists all available themes."""
        return list(THEMES.keys())

    @staticmethod
    def list_formats():
        """Lists all available formats."""
        return list(BASE_FORMATS.keys())
