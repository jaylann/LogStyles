# logstyles/formatter.py

from .utils import hex_to_ansi, reset_code

def escape_angle_brackets(text):
    """Escapes '<' and '>' characters in the given text."""
    return text.replace('<', '\\<').replace('>', '\\>')

def create_formatter(theme, base_format, delimiter=None, override_included_parts=None):
    """
    Creates a formatter function based on the given theme and base format.

    Parameters:
        theme (dict): The theme configuration.
        base_format (dict): The base format configuration.
        delimiter (str, optional): Custom delimiter. Defaults to base_format's delimiter.
        override_included_parts (list, optional): Parts to include, overriding base_format's parts_order.

    Returns:
        function: A formatter function for loguru.
    """
    timestamp_format = theme.get('timestamp_format', '%Y-%m-%d %H:%M:%S')
    styles = theme['styles']
    delimiter = delimiter or base_format['delimiter']
    parts_order = base_format['parts_order']

    # Determine included parts based on parts_order
    # Each part in parts_order corresponds to a specific part in the log
    # e.g., 'time_part' corresponds to 'time'
    included_parts = [
        part.replace('_part', '') for part in parts_order
    ]

    # If override_included_parts is provided, use it instead
    if override_included_parts is not None:
        included_parts = override_included_parts

    def formatter(record):
        # Apply timestamp format
        time_str = record['time'].strftime(timestamp_format)
        reset = reset_code()
        level_name = record['level'].name
        level_styles = styles.get(level_name, {})
        parts_list = []

        # Prepare parts based on parts_order
        for part in parts_order:
            part_key = part.replace('_part', '')
            if part_key == 'time' and 'time' in included_parts:
                time_color = hex_to_ansi(theme.get('time_color', '#FFFFFF'))
                parts_list.append(f"{time_color}{time_str}{reset}")
            elif part_key == 'level' and 'level' in included_parts:
                level_fg = level_styles.get('level_fg', '#FFFFFF')
                level_bg = level_styles.get('level_bg')
                level_color = hex_to_ansi(level_fg, level_bg)
                parts_list.append(f"{level_color}{level_name:<8}{reset}")
            elif part_key == 'module' and 'module' in included_parts:
                module_color = hex_to_ansi(theme.get('module_color', '#FFFFFF'))
                module_name = escape_angle_brackets(record['module'])
                parts_list.append(f"{module_color}{module_name}{reset}")
            elif part_key == 'function' and 'function' in included_parts:
                function_color = hex_to_ansi(theme.get('function_color', '#FFFFFF'))
                function_name = escape_angle_brackets(record['function'])
                parts_list.append(f"{function_color}{function_name}{reset}")
            elif part_key == 'line' and 'line' in included_parts:
                line_color = hex_to_ansi(theme.get('line_color', '#FFFFFF'))
                parts_list.append(f"{line_color}{record['line']}{reset}")
            elif part_key == 'thread_name' and 'thread_name' in included_parts:
                thread_color = hex_to_ansi(theme.get('thread_color', '#FFFFFF'))
                thread_name = escape_angle_brackets(record['thread'].name)
                parts_list.append(f"{thread_color}{thread_name}{reset}")
            elif part_key == 'process_name' and 'process_name' in included_parts:
                process_color = hex_to_ansi(theme.get('process_color', '#FFFFFF'))
                process_name = escape_angle_brackets(record['process'].name)
                parts_list.append(f"{process_color}{process_name}{reset}")
            elif part_key == 'message' and 'message' in included_parts:
                msg_fg = level_styles.get('message_fg', '#FFFFFF')
                msg_bg = level_styles.get('message_bg')
                msg_color = hex_to_ansi(msg_fg, msg_bg)
                message = escape_angle_brackets(record['message'])
                parts_list.append(f"{msg_color}{message}{reset}")
            else:
                # Part is not included or not applicable
                pass


        # Combine parts with delimiter
        formatted_message = delimiter.join(parts_list)
        return formatted_message + '\n'

    return formatter
