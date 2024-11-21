# logstyles/themes.py

THEMES = {
    # New Tokyo Night Storm theme
    'Tokyo Night Storm': {
        'timestamp_format': '%Y-%m-%d %H:%M:%S',
        'time_color': '#7982a9',  # From "foreground"
        'module_color': '#6183bb',  # From "settings.headerForeground"
        'function_color': '#7aa2f7',  # From "terminal.ansiBlue"
        'line_color': '#7dcfff',     # From "terminal.ansiCyan"
        'thread_color': '#bb9af7',   # From "terminal.ansiMagenta"
        'process_color': '#73daca',  # From "terminal.ansiGreen"
        'styles': {
            'DEBUG': {
                'level_fg': '#7dcfff',  # 'terminal.ansiCyan'
                'message_fg': '#7dcfff',
            },
            'INFO': {
                'level_fg': '#73daca',  # 'terminal.ansiGreen'
                'message_fg': '#a9b1d6',  # 'terminal.ansiBrightWhite'
            },
            'WARNING': {
                'level_fg': '#e0af68',  # 'terminal.ansiYellow'
                'message_fg': '#e0af68',
            },
            'ERROR': {
                'level_fg': '#f7768e',  # 'terminal.ansiRed'
                'message_fg': '#f7768e',
            },
            'CRITICAL': {
                'level_fg': '#bb9af7',  # 'terminal.ansiMagenta'
                'message_fg': '#232634',
                'message_bg': '#bb9af7',
            },
        },
    },
    # New Tokyo Night Light theme
    'Tokyo Night Light': {
        'timestamp_format': '%Y-%m-%d %H:%M:%S',
        'time_color': '#707280',     # From "descriptionForeground"
        'module_color': '#8f5e15',   # From "terminal.ansiYellow"
        'function_color': '#2959aa', # From "terminal.ansiBlue"
        'line_color': '#006c86',     # From "terminal.ansiCyan"
        'thread_color': '#7b43ba',   # From "terminal.ansiMagenta"
        'process_color': '#33635c',  # From "terminal.ansiGreen"
        'styles': {
            'DEBUG': {
                'level_fg': '#006c86',  # 'terminal.ansiCyan'
                'message_fg': '#006c86',
            },
            'INFO': {
                'level_fg': '#33635c',  # 'terminal.ansiGreen'
                'message_fg': '#343b58',  # From "variable"
            },
            'WARNING': {
                'level_fg': '#8f5e15',  # 'terminal.ansiYellow'
                'message_fg': '#8f5e15',
            },
            'ERROR': {
                'level_fg': '#8c4351',  # 'terminal.ansiRed'
                'message_fg': '#8c4351',
            },
            'CRITICAL': {
                'level_fg': '#7b43ba',  # 'terminal.ansiMagenta'
                'message_fg': '#e6e7ed',  # From "editor.background"
                'message_bg': '#7b43ba',
            },
        },
    },
    # New Tokyo Night theme
    'Tokyo Night': {
        'timestamp_format': '%Y-%m-%d %H:%M:%S',
        'included_parts': ['time', 'level', 'message'],
        'time_color': '#787c99',     # From "foreground"
        'module_color': '#6183bb',   # From "settings.headerForeground"
        'function_color': '#7aa2f7', # From "terminal.ansiBlue"
        'line_color': '#7dcfff',     # From "terminal.ansiCyan"
        'thread_color': '#bb9af7',   # From "terminal.ansiMagenta"
        'process_color': '#73daca',  # From "terminal.ansiGreen"
        'styles': {
            'DEBUG': {
                'level_fg': '#7dcfff',  # 'terminal.ansiCyan'
                'message_fg': '#7dcfff',
            },
            'INFO': {
                'level_fg': '#73daca',  # 'terminal.ansiGreen'
                'message_fg': '#a9b1d6',  # 'terminal.ansiBrightWhite'
            },
            'WARNING': {
                'level_fg': '#e0af68',  # 'terminal.ansiYellow'
                'message_fg': '#e0af68',
            },
            'ERROR': {
                'level_fg': '#f7768e',  # 'terminal.ansiRed'
                'message_fg': '#f7768e',
            },
            'CRITICAL': {
                'level_fg': '#bb9af7',  # 'terminal.ansiMagenta'
                'message_fg': '#232634',
                'message_bg': '#bb9af7',
            },
        },
    },
    'Latte': {
        'timestamp_format': '%Y-%m-%d %H:%M:%S',
        'time_color': '#9ca0b0',  # Overlay0
        'module_color': '#df8e1d',  # Yellow
        'function_color': '#1e66f5',  # Blue
        'line_color': '#04a5e5',  # Sky
        'thread_color': '#7287fd',  # Lavender
        'process_color': '#179299',  # Teal
        'styles': {
            'DEBUG': {
                'level_fg': '#8839ef',  # Mauve
                'message_fg': '#8839ef',
            },
            'INFO': {
                'level_fg': '#40a02b',  # Green
                'message_fg': '#4c4f69',  # Text
            },
            'WARNING': {
                'level_fg': '#df8e1d',  # Yellow
                'message_fg': '#df8e1d',
            },
            'ERROR': {
                'level_fg': '#d20f39',  # Red
                'message_fg': '#d20f39',
            },
            'CRITICAL': {
                'level_fg': '#e64553',  # Maroon
                'message_fg': '#eff1f5',  # Base
                'message_bg': '#e64553',
            },
        },
    },
    'Frappe': {
        'timestamp_format': '%Y-%m-%d %H:%M:%S',
        'time_color': '#737994',  # Overlay0
        'module_color': '#e5c890',  # Yellow
        'function_color': '#8caaee',  # Blue
        'line_color': '#99d1db',  # Sky
        'thread_color': '#babbf1',  # Lavender
        'process_color': '#81c8be',  # Teal
        'styles': {
            'DEBUG': {
                'level_fg': '#ca9ee6',  # Mauve
                'message_fg': '#ca9ee6',
            },
            'INFO': {
                'level_fg': '#a6d189',  # Green
                'message_fg': '#c6d0f5',  # Text
            },
            'WARNING': {
                'level_fg': '#ef9f76',  # Peach
                'message_fg': '#ef9f76',
            },
            'ERROR': {
                'level_fg': '#e78284',  # Red
                'message_fg': '#e78284',
            },
            'CRITICAL': {
                'level_fg': '#ea999c',  # Maroon
                'message_fg': '#232634',  # Crust
                'message_bg': '#ea999c',
            },
        },
    },
    'Macchiato': {
        'timestamp_format': '%Y-%m-%d %H:%M:%S',
        'time_color': '#6e738d',  # Overlay0
        'module_color': '#eed49f',  # Yellow
        'function_color': '#8aadf4',  # Blue
        'line_color': '#91d7e3',  # Sky
        'thread_color': '#b7bdf8',  # Lavender
        'process_color': '#8bd5ca',  # Teal
        'styles': {
            'DEBUG': {
                'level_fg': '#c6a0f6',  # Mauve
                'message_fg': '#c6a0f6',
            },
            'INFO': {
                'level_fg': '#a6da95',  # Green
                'message_fg': '#cad3f5',  # Text
            },
            'WARNING': {
                'level_fg': '#f5a97f',  # Peach
                'message_fg': '#f5a97f',
            },
            'ERROR': {
                'level_fg': '#ed8796',  # Red
                'message_fg': '#ed8796',
            },
            'CRITICAL': {
                'level_fg': '#ee99a0',  # Maroon
                'message_fg': '#cad3f5',  # Text
                'message_bg': '#ee99a0',
            },
        },
    },
    'Mocha': {
        'timestamp_format': '%Y-%m-%d %H:%M:%S',
        'time_color': '#6c7086',  # Overlay0
        'module_color': '#f9e2af',  # Yellow
        'function_color': '#89b4fa',  # Blue
        'line_color': '#89dceb',  # Sky
        'thread_color': '#b4befe',  # Lavender
        'process_color': '#94e2d5',  # Teal
        'styles': {
            'DEBUG': {
                'level_fg': '#cba6f7',  # Mauve
                'message_fg': '#cba6f7',
            },
            'INFO': {
                'level_fg': '#a6e3a1',  # Green
                'message_fg': '#cdd6f4',  # Text
            },
            'WARNING': {
                'level_fg': '#fab387',  # Peach
                'message_fg': '#fab387',
            },
            'ERROR': {
                'level_fg': '#f38ba8',  # Red
                'message_fg': '#f38ba8',
            },
            'CRITICAL': {
                'level_fg': '#eba0ac',  # Maroon
                'message_fg': '#cdd6f4',  # Text
                'message_bg': '#eba0ac',
            },
        },
    },
}
