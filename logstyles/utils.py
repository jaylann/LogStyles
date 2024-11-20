# logstyles/utils.py

def hex_to_ansi(fg_hex_color, bg_hex_color=None):
    """Converts hex color codes to ANSI escape codes for foreground and background colors."""
    fg_color = fg_hex_color.lstrip('#')
    fg_r, fg_g, fg_b = tuple(int(fg_color[i:i+2], 16) for i in (0, 2, 4))
    ansi_code = f'\x1b[38;2;{fg_r};{fg_g};{fg_b}m'

    if bg_hex_color:
        bg_color = bg_hex_color.lstrip('#')
        bg_r, bg_g, bg_b = tuple(int(bg_color[i:i+2], 16) for i in (0, 2, 4))
        ansi_code += f'\x1b[48;2;{bg_r};{bg_g};{bg_b}m'

    return ansi_code

def reset_code():
    """Returns the ANSI escape code to reset color formatting."""
    return '\x1b[0m'
