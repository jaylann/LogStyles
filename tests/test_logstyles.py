import unittest
import sys
from io import StringIO
from unittest import mock
from loguru import logger
from logstyles import LogStyles
from logstyles.themes import THEMES
from logstyles.base_formats import BASE_FORMATS
from logstyles.utils import hex_to_ansi, reset_code

class TestLogStyles(unittest.TestCase):
    def setUp(self):
        # Redirect logger output to a StringIO buffer
        self.log_capture = StringIO()
        logger.remove()  # Remove any existing handlers
        logger.add(self.log_capture, format="{message}", colorize=False)

    def tearDown(self):
        # Reset logger after each test
        logger.remove()

    def get_expected_color_code(self, hex_color, bg_hex=None):
        """Convert hex color to ANSI escape code."""
        return hex_to_ansi(hex_color, bg_hex)

    def parse_ansi_codes(self, text):
        """Extract ANSI escape codes from the text."""
        import re
        ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
        return ansi_escape.findall(text)

    def test_all_themes_and_formats(self):
        """Dynamically test all themes with all base formats."""
        for theme_name, theme in THEMES.items():
            for format_name, base_format in BASE_FORMATS.items():
                with self.subTest(theme=theme_name, format=format_name):
                    # Generate formatter without relying on 'included_parts' from themes
                    formatter = LogStyles.get_formatter(
                        theme_name=theme_name,
                        format_name=format_name,
                        delimiter=None,  # Use base format's delimiter
                    )

                    # Reconfigure logger with the new formatter
                    logger.remove()
                    logger.add(self.log_capture, format=formatter, colorize=False)

                    # Log a test message
                    test_message = f"Test log message for {format_name} with {theme_name}"
                    logger.info(test_message)

                    # Retrieve the log output
                    self.log_capture.seek(0)
                    log_output = self.log_capture.read().strip()
                    self.log_capture.truncate(0)
                    self.log_capture.seek(0)

                    # Determine which parts are actually included based on base_format
                    parts_order = base_format['parts_order']
                    actual_included_parts = [
                        part.replace('_part', '') for part in parts_order
                    ]

                    # Create a mapping of part to its expected color and content
                    part_contents = {}

                    # Create mock_record to simulate the formatter's behavior
                    mock_level = mock.Mock()
                    mock_level.name = 'INFO'

                    mock_thread = mock.Mock()
                    mock_thread.name = 'MainThread'

                    mock_process = mock.Mock()
                    mock_process.name = 'MainProcess'

                    mock_time = mock.Mock()
                    mock_time.strftime.return_value = theme.get('timestamp_format', '%Y-%m-%d %H:%M:%S')

                    mock_record = {
                        'time': mock_time,
                        'level': mock_level,
                        'module': 'test_module',
                        'function': 'test_function',
                        'line': 42,
                        'thread': mock_thread,
                        'process': mock_process,
                        'message': test_message
                    }

                    # Apply formatter to mock_record to get the expected formatted message
                    formatted_message = formatter(mock_record).strip()

                    # Now, parse the formatted_message to verify colors and content
                    import re
                    ansi_color_pattern = re.compile(r'\x1b\[[0-9;]*m')
                    ansi_codes = ansi_color_pattern.findall(formatted_message)

                    # Split the formatted message into parts based on delimiter
                    delimiter = base_format.get('delimiter', '')
                    if delimiter:
                        parts = formatted_message.split(delimiter)
                    else:
                        parts = [formatted_message]

                    # Create a mapping of part to its content
                    for part in parts:
                        # Extract the color code and the actual text
                        match = re.match(r'(\x1b\[[0-9;]*m)(.*?)\x1b\[0m', part)
                        if match:
                            color_code, text = match.groups()
                            # Determine which part this text corresponds to
                            for part_key in actual_included_parts:
                                # Depending on part_key, the text would differ
                                if part_key == 'time' and text == mock_record['time'].strftime(mock_record['time'].strftime.call_args[0][0]):
                                    part_contents['time'] = (color_code, text)
                                elif part_key == 'level' and text.strip() == mock_record['level'].name:
                                    part_contents['level'] = (color_code, text)
                                elif part_key == 'module' and text == mock_record['module']:
                                    part_contents['module'] = (color_code, text)
                                elif part_key == 'function' and text == mock_record['function']:
                                    part_contents['function'] = (color_code, text)
                                elif part_key == 'line' and text == str(mock_record['line']):
                                    part_contents['line'] = (color_code, text)
                                elif part_key == 'thread_name' and text == mock_record['thread'].name:
                                    part_contents['thread_name'] = (color_code, text)
                                elif part_key == 'process_name' and text == mock_record['process'].name:
                                    part_contents['process_name'] = (color_code, text)
                                elif part_key == 'message' and text == mock_record['message']:
                                    part_contents['message'] = (color_code, text)

                    # Now, verify each included part's color
                    for part in actual_included_parts:
                        if part == 'time':
                            color_hex = theme.get('time_color', '#FFFFFF')
                        elif part == 'level':
                            color_hex = theme['styles'][mock_record['level'].name].get('level_fg', '#FFFFFF')
                        elif part == 'module':
                            color_hex = theme.get('module_color', '#FFFFFF')
                        elif part == 'function':
                            color_hex = theme.get('function_color', '#FFFFFF')
                        elif part == 'line':
                            color_hex = theme.get('line_color', '#FFFFFF')
                        elif part == 'thread_name':
                            color_hex = theme.get('thread_color', '#FFFFFF')
                        elif part == 'process_name':
                            color_hex = theme.get('process_color', '#FFFFFF')
                        elif part == 'message':
                            color_hex = theme['styles'][mock_record['level'].name].get('message_fg', '#FFFFFF')
                        else:
                            continue  # Unknown part

                        expected_color_code = self.get_expected_color_code(color_hex)
                        if part in part_contents:
                            actual_color_code, actual_text = part_contents[part]
                            self.assertEqual(
                                actual_color_code,
                                expected_color_code,
                                msg=f"Color code for '{part}' is incorrect in theme '{theme_name}' with format '{format_name}'."
                            )
                            # Additionally, verify that the text matches
                            if part == 'time':
                                expected_text = mock_record['time'].strftime(theme.get('timestamp_format', '%Y-%m-%d %H:%M:%S'))
                                self.assertEqual(actual_text, expected_text, msg=f"Time format is incorrect for theme '{theme_name}' with format '{format_name}'.")
                            elif part == 'level':
                                self.assertEqual(actual_text.strip(), mock_record['level'].name, msg=f"Log level text is incorrect for theme '{theme_name}' with format '{format_name}'.")
                            elif part == 'message':
                                self.assertEqual(actual_text, mock_record['message'], msg=f"Log message text is incorrect for theme '{theme_name}' with format '{format_name}'.")
                            # Add more text verifications as needed for other parts
                        else:
                            self.fail(f"Expected part '{part}' not found in log output for theme '{theme_name}' with format '{format_name}'.")

                    # Finally, ensure the log ends with the reset code
                    self.assertTrue(
                        formatted_message.endswith(reset_code()),
                        msg="Reset code is missing at the end of the log message."
                    )

    def test_invalid_theme(self):
        """Test that an invalid theme name raises a ValueError."""
        with self.assertRaises(ValueError):
            LogStyles.get_formatter(
                theme_name='InvalidTheme',
                format_name='Simple'
            )

    def test_invalid_format(self):
        """Test that an invalid format name raises a ValueError."""
        with self.assertRaises(ValueError):
            LogStyles.get_formatter(
                theme_name='Catpuccin Mocha',
                format_name='InvalidFormat'
            )

    def test_escape_angle_brackets(self):
        """Test that angle brackets are properly escaped."""
        formatter = LogStyles.get_formatter(
            theme_name='Catpuccin Mocha',
            format_name='Simple'
        )
        # Create a mock record with angle brackets in the message
        mock_level = mock.Mock()
        mock_level.name = 'INFO'

        mock_record = {
            'time': mock.Mock(),
            'level': mock_level,
            'module': 'test_module',
            'function': 'test_function',
            'line': 42,
            'thread': mock.Mock(name='MainThread'),
            'process': mock.Mock(name='MainProcess'),
            'message': 'Message with <angle> brackets'
        }
        mock_record['time'].strftime.return_value = '2024-04-27 12:00:00'

        formatted = formatter(mock_record).strip()

        # Use regex to ensure that all '<' and '>' are properly escaped
        import re
        # Pattern to find any '<' not preceded by a backslash
        unescaped_less_than = re.search(r'(?<!\\)<', formatted)
        # Pattern to find any '>' not preceded by a backslash
        unescaped_greater_than = re.search(r'(?<!\\)>', formatted)

        # Assert that there are no unescaped '<' or '>' characters
        self.assertFalse(
            unescaped_less_than,
            "Unescaped '<' found in formatted message."
        )
        self.assertFalse(
            unescaped_greater_than,
            "Unescaped '>' found in formatted message."
        )

        # Additionally, verify that escaped sequences are present
        self.assertIn('\\<angle\\>', formatted, "Escaped angle brackets are not present as expected.")

    def test_custom_delimiter(self):
        """Test that a custom delimiter is applied correctly."""
        formatter = LogStyles.get_formatter(
            theme_name='Catpuccin Mocha',
            format_name='Process',
            delimiter=' || '
        )
        # Create a mock record
        mock_level = mock.Mock()
        mock_level.name = 'INFO'

        mock_record = {
            'time': mock.Mock(),
            'level': mock_level,
            'process': mock.Mock(name='MainProcess'),
            'message': 'Test message with custom delimiter'
        }
        mock_record['time'].strftime.return_value = '12:00:00'
        formatted = formatter(mock_record).strip()
        self.assertIn(' || ', formatted)
        self.assertIn('Test message with custom delimiter', formatted)


if __name__ == '__main__':
    unittest.main()
