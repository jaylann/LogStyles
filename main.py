import sys
from loguru import logger
from logstyles import LogStyles

def main():
    """
    Iterates through all themes and formats defined in the logstyles library,
    and logs sample messages at various levels to visualize each combination.
    Utilizes the LogStyles class's list methods for better encapsulation.
    """
    themes = LogStyles.list_themes()
    formats = LogStyles.list_formats()

    for theme_name in themes:
        for format_name in formats:
            # Print header for the current theme and format
            print("\n" + "=" * 80)
            print(f"Theme: '{theme_name}' | Format: '{format_name}'")
            print("=" * 80 + "\n")

            try:
                # Generate the formatter using the LogStyles class
                formatter = LogStyles.get_formatter(
                    theme_name=theme_name,
                    format_name=format_name,
                    timestamp_format='%Y-%m-%d %H:%M:%S'  # Default timestamp format
                )
            except ValueError as ve:
                print(f"Error: {ve}")
                print("-" * 80 + "\n")
                continue  # Skip to the next format if there's an error

            # Remove any existing handlers to prevent duplicate logs
            logger.remove()

            # Add a new handler with the generated formatter and enable colorization
            logger.add(sys.stdout, format=formatter, colorize=True)

            # Log sample messages at different levels
            logger.debug("This is a DEBUG message.")
            logger.info("This is an INFO message.")
            logger.warning("This is a WARNING message.")
            logger.error("This is an ERROR message.")
            logger.critical("This is a CRITICAL message.")

            # Optional: Add some spacing after each combination
            print("\n" + "-" * 80 + "\n")

    # Remove all handlers after logging is complete
    logger.remove()

if __name__ == '__main__':
    main()
