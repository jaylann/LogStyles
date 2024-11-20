# logstyles/themes.py

THEMES = {
    'Catpuccin': {
        'timestamp_format': '%Y-%m-%d %H:%M:%S',
        'included_parts': ['time', 'level', 'message'],
        'time_color': '#A3BE8C',
        'module_color': '#EBCB8B',
        'function_color': '#88C0D0',
        'line_color': '#81A1C1',
        'thread_color': '#B48EAD',
        'process_color': '#5E81AC',
        'styles': {
            'DEBUG': {
                'level_fg': '#8BE9FD',
                'message_fg': '#8BE9FD',
            },
            'INFO': {
                'level_fg': '#50FA7B',
                'message_fg': '#F8F8F2',
            },
            'WARNING': {
                'level_fg': '#F1FA8C',
                'message_fg': '#F1FA8C',
            },
            'ERROR': {
                'level_fg': '#FF5555',
                'message_fg': '#FF5555',
            },
            'CRITICAL': {
                'level_fg': '#FF79C6',
                'message_fg': '#F8F8F2',
                'message_bg': '#FF79C6',
            },
        },
    },
    'TokyoNight': {
        'timestamp_format': '%Y-%m-%d %H:%M:%S',
        'included_parts': ['time', 'level', 'message'],
        'time_color': '#81A1C1',
        'module_color': '#A3BE8C',
        'function_color': '#88C0D0',
        'line_color': '#81A1C1',
        'thread_color': '#B48EAD',
        'process_color': '#5E81AC',
        'styles': {
            'DEBUG': {
                'level_fg': '#7AA2F7',
                'message_fg': '#7AA2F7',
            },
            'INFO': {
                'level_fg': '#9ECE6A',
                'message_fg': '#A9B1D6',
            },
            'WARNING': {
                'level_fg': '#E0AF68',
                'message_fg': '#E0AF68',
            },
            'ERROR': {
                'level_fg': '#F7768E',
                'message_fg': '#F7768E',
            },
            'CRITICAL': {
                'level_fg': '#BB9AF7',
                'message_fg': '#A9B1D6',
                'message_bg': '#BB9AF7',
            },
        },
    },
}
