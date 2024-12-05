# logstyles/formatter.py
import threading

from .utils import hex_to_ansi, reset_code

def escape_angle_brackets(text):
    """Escapes '<' and '>' characters in the given text."""
    return text.replace('<', '\\<').replace('>', '\\>')

def create_formatter(theme, base_format, delimiter=None, override_included_parts=None):
    timestamp_format = theme.get('timestamp_format', '%Y-%m-%d %H:%M:%S')
    styles = theme['styles']
    delimiter = delimiter or base_format['delimiter']
    parts_order = base_format['parts_order']

    included_parts = [
        part.replace('_part', '') for part in parts_order
    ]

    if override_included_parts is not None:
        included_parts = override_included_parts

    # Default and maximum widths for fields
    field_widths_config = {
        'time': {'default': len(timestamp_format), 'max': len(timestamp_format)},  # Fixed timestamp length
        'level': {'default': 8, 'max': 8},   # Fixed level name length
        'module': {'default': 20, 'max': 30},
        'function': {'default': 20, 'max': 30},
        'line': {'default': 3, 'max': 6},
        'thread_name': {'default': 15, 'max': 25},
        'process_name': {'default': 15, 'max': 25},
        # Add other fields as needed
    }

    # Initialize current widths with default values for included parts
    current_field_widths = {}
    for part_key in included_parts:
        config = field_widths_config.get(part_key)
        if config:
            current_field_widths[part_key] = config['default']
        else:
            current_field_widths[part_key] = None  # For fields like 'message' without width settings

    # Lock for thread safety
    field_widths_lock = threading.Lock()

    def formatter(record):
        nonlocal current_field_widths

        # Apply timestamp format
        time_str = record['time'].strftime(timestamp_format)
        reset = reset_code()
        level_name = record['level'].name
        level_styles = styles.get(level_name, {})

        fields = {}

        # Prepare field values
        for part in parts_order:
            part_key = part.replace('_part', '')
            if part_key == 'time' and 'time' in included_parts:
                fields['time'] = time_str
            elif part_key == 'level' and 'level' in included_parts:
                fields['level'] = level_name
            elif part_key == 'module' and 'module' in included_parts:
                module_name = escape_angle_brackets(record['module'])
                fields['module'] = module_name
            elif part_key == 'function' and 'function' in included_parts:
                function_name = escape_angle_brackets(record['function'])
                fields['function'] = function_name
            elif part_key == 'line' and 'line' in included_parts:
                line_str = str(record['line'])
                fields['line'] = line_str
            elif part_key == 'thread_name' and 'thread_name' in included_parts:
                thread_name = escape_angle_brackets(record['thread'].name)
                fields['thread_name'] = thread_name
            elif part_key == 'process_name' and 'process_name' in included_parts:
                process_name = escape_angle_brackets(record['process'].name)
                fields['process_name'] = process_name
            elif part_key == 'message' and 'message' in included_parts:
                message = escape_angle_brackets(record['message'])
                fields['message'] = message

        # Update current field widths up to maximums
        with field_widths_lock:
            for field, value in fields.items():
                config = field_widths_config.get(field)
                if config is None:
                    continue  # Skip fields without width settings (e.g., 'message')

                max_width = config['max']
                current_width = current_field_widths.get(field, 0)
                value_length = len(value)

                if current_width < max_width and value_length > current_width:
                    if value_length <= max_width:
                        # Update current width permanently
                        current_field_widths[field] = value_length
                    else:
                        # Exceeds max, do not update current width
                        pass

        # Prepare parts with appropriate widths
        parts_list = []

        for part in parts_order:
            part_key = part.replace('_part', '')
            if part_key in fields:
                value = fields[part_key]
                config = field_widths_config.get(part_key)
                current_width = current_field_widths.get(part_key)
                max_width = config['max'] if config else None

                # Determine the width for this field
                if config and len(value) > max_width:
                    # Value exceeds max width, use full length for this line
                    width = len(value)
                else:
                    width = current_width

                # Pad the value to the width if width is specified
                if width is not None:
                    if part_key == 'line':
                        # Right-justify line numbers
                        padded_value = value.rjust(width)
                    else:
                        # Left-justify other fields
                        padded_value = value.ljust(width)
                else:
                    # For fields without width settings (e.g., 'message')
                    padded_value = value

                # Apply color
                if part_key == 'time':
                    time_color = hex_to_ansi(theme.get('time_color', '#FFFFFF'))
                    colored_value = f"{time_color}{padded_value}{reset}"
                elif part_key == 'level':
                    level_fg = level_styles.get('level_fg', '#FFFFFF')
                    level_bg = level_styles.get('level_bg')
                    level_color = hex_to_ansi(level_fg, level_bg)
                    colored_value = f"{level_color}{padded_value}{reset}"
                elif part_key == 'module':
                    module_color = hex_to_ansi(theme.get('module_color', '#FFFFFF'))
                    colored_value = f"{module_color}{padded_value}{reset}"
                elif part_key == 'function':
                    function_color = hex_to_ansi(theme.get('function_color', '#FFFFFF'))
                    colored_value = f"{function_color}{padded_value}{reset}"
                elif part_key == 'line':
                    line_color = hex_to_ansi(theme.get('line_color', '#FFFFFF'))
                    colored_value = f"{line_color}{padded_value}{reset}"
                elif part_key == 'thread_name':
                    thread_color = hex_to_ansi(theme.get('thread_color', '#FFFFFF'))
                    colored_value = f"{thread_color}{padded_value}{reset}"
                elif part_key == 'process_name':
                    process_color = hex_to_ansi(theme.get('process_color', '#FFFFFF'))
                    colored_value = f"{process_color}{padded_value}{reset}"
                elif part_key == 'message':
                    msg_fg = level_styles.get('message_fg', '#FFFFFF')
                    msg_bg = level_styles.get('message_bg')
                    msg_color = hex_to_ansi(msg_fg, msg_bg)
                    colored_value = f"{msg_color}{padded_value}{reset}"
                else:
                    colored_value = padded_value

                parts_list.append(colored_value)

        formatted_message = delimiter.join(parts_list)
        return formatted_message + '\n'

    return formatter
