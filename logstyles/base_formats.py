# logstyles/base_formats.py

BASE_FORMATS = {
    'Column': {
        'parts_order': ['time_part', 'level_part', 'module_part', 'message_part'],
        'delimiter': ' | ',
    },
    'LeftAligned': {
        'parts_order': ['level_part', 'message_part'],
        'delimiter': ': ',
    },
    'Detailed': {
        'parts_order': ['time_part', 'level_part', 'module_part', 'function_part', 'line_part', 'message_part'],
        'delimiter': ' | ',
    },
    'Simple': {
        'parts_order': ['message_part'],
        'delimiter': '',
    },
    'Threaded': {
        'parts_order': ['time_part', 'level_part', 'thread_name_part', 'message_part'],
        'delimiter': ' | ',
    },
    'Process': {
        'parts_order': ['time_part', 'level_part', 'process_name_part', 'message_part'],
        'delimiter': ' | ',
    },
}
