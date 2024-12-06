import re
import unittest
from io import StringIO

from loguru import logger

from logstyles import LogStyles
from logstyles.base_formats import BASE_FORMATS
from logstyles.themes import THEMES


class TestLogStylesIntegration(unittest.TestCase):
    def setUp(self):
        # Redirect logger output
        self.log_capture = StringIO()
        logger.remove()
        logger.add(self.log_capture, format="{message}", colorize=False)

    def tearDown(self):
        logger.remove()

    def test_sanity_all_themes_and_formats(self):
        """Check that logging a known test message appears in the output for all themes and formats."""
        test_message = "Test message for sanity check"
        for theme_name in THEMES.keys():
            for format_name in BASE_FORMATS.keys():
                with self.subTest(theme=theme_name, format=format_name):
                    formatter = LogStyles.get_formatter(theme_name, format_name)
                    logger.remove()
                    logger.add(self.log_capture, format=formatter, colorize=False)

                    # Log a known message
                    logger.info(test_message)

                    self.log_capture.seek(0)
                    line = self.log_capture.read()
                    self.log_capture.truncate(0)
                    self.log_capture.seek(0)

                    self.assertIn(test_message, line, "Message should appear in the output.")

    # tests/test_logstyles.py
    # tests/test_logstyles.py
    def test_angle_brackets_escaping(self):
        """Ensure angle brackets in module/function/thread/process are escaped."""
        test_message = "Angle brackets test"
        # We'll rely on 'Detailed' format which includes module/function/line/message by default.
        formatter = LogStyles.get_formatter('Tokyo Night', 'Detailed',
                                            included_parts=["module", "time", "level", "function", "line",
                                                            "thread_name", "process_name"])
        logger.remove()
        logger.add(self.log_capture, format=formatter, colorize=False)

        # Bind custom fields via .bind() so they appear in record['extra']
        logger.bind(
            module='module<with>brackets',
            function='func<with>brackets',
            line=999,
            thread_name='Main<Thread>',
            process_name='Main<Process>'
        ).info(test_message)

        self.log_capture.seek(0)
        line = self.log_capture.read().strip()
        print(line)  # For debugging purposes

        # Check that no raw angle brackets appear
        self.assertNotRegex(line, r'(?<!\\)<', "Unescaped '<' found in output.")
        self.assertNotRegex(line, r'(?<!\\)>', "Unescaped '>' found in output.")

        # Check that escaped sequences appear using HTML entities
        self.assertIn('module&lt;with&gt;brackets', line, "Escaped angle brackets not found for module field.")
        self.assertIn('func&lt;with&gt;brackets', line, "Escaped angle brackets not found for function field.")
        self.assertIn('Main&lt;Thread&gt;', line, "Escaped angle brackets not found for thread field.")
        self.assertIn('Main&lt;Process&gt;', line, "Escaped angle brackets not found for process field.")

    def test_custom_timestamp_format(self):
        """Test a custom timestamp format is applied."""
        # Use a custom timestamp format and check if it follows HH:MM:SS pattern
        formatter = LogStyles.get_formatter('Tokyo Night', 'Detailed', timestamp_format='%H:%M:%S')
        logger.remove()
        logger.add(self.log_capture, format=formatter, colorize=False)

        logger.info("Test timestamp format")
        self.log_capture.seek(0)
        line = self.log_capture.read().strip()

        # The line should contain a timestamp in HH:MM:SS format. Let's use a regex for that:
        time_pattern = r'\d{2}:\d{2}:\d{2}'
        self.assertRegex(line, time_pattern, "Custom timestamp format (HH:MM:SS) not found.")

    def test_included_parts_override(self):
        """Check that specifying included_parts only shows those fields."""
        # We override to only show time and message
        formatter = LogStyles.get_formatter('Tokyo Night', 'Detailed', included_parts=['time', 'message'])
        logger.remove()
        logger.add(self.log_capture, format=formatter, colorize=False)

        test_message = "Testing included parts"
        logger.info(test_message)
        self.log_capture.seek(0)
        line = self.log_capture.read().strip()

        # Split by delimiter which is " | " for Detailed
        parts = line.split(' | ')

        # Only time and message should remain
        # Since we know Detailed originally has time, level, module, function, line, message
        # With included_parts=['time','message'], only those 2 should appear.
        self.assertEqual(len(parts), 2, "Only time and message parts should be present.")
        self.assertIn(test_message, line, "Message should still appear.")
        # Ensure none of the other parts (like module/function) appear
        forbidden_fields = ['test_logstyles', 'func', 'INFO', '999']  # Potential leftover fields
        for ff in forbidden_fields:
            self.assertNotIn(ff, line, f"Field '{ff}' should not be included.")

    def test_dynamic_width_expansion(self):
        """Test that fields expand up to max width and do not remain oversized after very long values."""
        formatter = LogStyles.get_formatter('Tokyo Night', 'Detailed')
        logger.remove()
        logger.add(self.log_capture, format=formatter, colorize=False)

        # We'll test the module field width changes.
        # Start with a short module name:
        short_module = "mod"
        logger.bind(module=short_module, function='func', line=10).info("Short module")
        self.log_capture.seek(0)
        first_line = self.log_capture.read().strip()
        self.log_capture.truncate(0)
        self.log_capture.seek(0)

        # Check initial padding
        parts = first_line.split(' | ')
        # parts order: time, level, module, function, line, message
        module_part = parts[2]
        # Remove ANSI
        module_text = re.sub(r'\x1b\[[0-9;]*m', '', module_part)
        # Should be at least default width (20 chars)
        self.assertGreaterEqual(len(module_text), 20, "Module field not padded to default width for short value.")

        # Now log a longer module name within max width (max width=30):
        longer_module = "longer_module_name123"
        logger.bind(module=longer_module, function='func', line=11).info("Longer module")
        self.log_capture.seek(0)
        second_line = self.log_capture.read().strip()
        self.log_capture.truncate(0)
        self.log_capture.seek(0)

        parts = second_line.split(' | ')
        module_part = parts[2]
        module_text = re.sub(r'\x1b\[[0-9;]*m', '', module_part)
        # It should now fit the longer_module length exactly if less than 30 chars
        self.assertTrue(len(module_text) == len(longer_module),
                        "Module field did not expand to accommodate longer value.")

        # Log an extremely long module name > 30 chars
        very_long_module = "this_module_name_is_exceedingly_long_exceeding_max"
        logger.bind(module=very_long_module, function='func', line=12).info("Very long module")
        self.log_capture.seek(0)
        third_line = self.log_capture.read().strip()
        self.log_capture.truncate(0)
        self.log_capture.seek(0)

        parts = third_line.split(' | ')
        module_part = parts[2]
        module_text = re.sub(r'\x1b\[[0-9;]*m', '', module_part)
        # This line should display the full long module but not permanently increase the stored width
        self.assertEqual(len(module_text), len(very_long_module),
                         "Long module value should display fully for that line.")

        # Now log the short module again and ensure width returns to previously expanded length (not the max exceeded one)
        logger.bind(module=short_module, function='func', line=13).info("Back to short")
        self.log_capture.seek(0)
        fourth_line = self.log_capture.read().strip()
        parts = fourth_line.split(' | ')
        module_part = parts[2]
        print(module_part)
        module_text = re.sub(r'\x1b\[[0-9;]*m', '', module_part)
        print(module_text)
        # The width should be at least the length of 'longer_module_name' but not as large as the very_long_module
        self.assertGreaterEqual(len(module_text), len(longer_module),
                                "Module width should not shrink below the previously expanded width.")
        self.assertLess(len(module_text), len(very_long_module),
                        "Module width should not remain expanded to exceed the max width after one very long value.")


if __name__ == '__main__':
    unittest.main()
