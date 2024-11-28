# LogStyles

![PyPI](https://img.shields.io/pypi/v/logstyles)
![License](https://img.shields.io/pypi/l/logstyles)
![Python Versions](https://img.shields.io/pypi/pyversions/logstyles)
![Tests](https://github.com/jaylann/logstyles/actions/workflows/python-app.yml/badge.svg)


## 🌟 Introduction

**LogStyles** is a sleek and modern Python library designed to enhance your logging experience with **Loguru**. It offers a collection of customizable themes and formats that transform your log messages into visually appealing and structured outputs. Whether you're developing a small script or a large-scale application, LogStyles provides the flexibility and aesthetics to make your logs both informative and easy on the eyes.

## 🚀 Features

- **Multiple Predefined Themes**: Choose from a variety of stylish themes like **Latte**, **Frappé**, **Macchiato**, **Mocha**, and **Tokyo Night Light**.
- **Versatile Log Formats**: Utilize different log formats such as **Simple**, **Detailed**, **Threaded**, and **Process** to suit your needs.
- **Color Customization**: Easily customize colors for different log levels and components.
- **Seamless Integration with Loguru**: Effortlessly integrate LogStyles into your existing Loguru setup.
- **Extensible Design**: Add your own themes and formats with minimal effort.

## 📦 Installation

You can install LogStyles using `pip`:

```bash
pip install logstyles
```

## 🛠️ Usage

LogStyles is designed to work seamlessly with **Loguru**. Here's a quick guide to get you started.

### 📚 Basic Example

```python
import sys
from loguru import logger
from logstyles import LogStyles

def main():
    # Create a formatter with the desired theme and format
    formatter = LogStyles.get_formatter(
        theme_name='Mocha',          # Choose a theme
        format_name='Detailed',      # Choose a format
        delimiter=' | ',             # Optional: Customize delimiter
        timestamp_format='%Y-%m-%d %H:%M:%S'  # Optional: Customize timestamp format
    )
    
    # Configure the logger
    logger.remove()  # Remove the default logger
    logger.add(sys.stdout, format=formatter, colorize=False)  # Add LogStyles formatter
    
    # Log some messages
    logger.debug("Debug message with Mocha theme.")
    logger.info("Info message with Mocha theme.")
    logger.warning("Warning message with Mocha theme.")
    logger.error("Error message with Mocha theme.")
    logger.critical("Critical message with Mocha theme.")

if __name__ == '__main__':
    main()
```

### 🎨 Selecting Themes and Formats

LogStyles comes with a variety of themes and formats. Here's how you can explore and use them:

```python
# List of available themes
available_themes = LogStyles.get_available_themes()
print("Available Themes:", available_themes)

# List of available formats
available_formats = LogStyles.get_available_formats()
print("Available Formats:", available_formats)
```

## ⚙️ Configuration

### 🔧 Customizing the Formatter

You can customize the formatter by specifying different parameters:

- **`theme_name`**: The name of the theme you want to use (e.g., `'Latte'`, `'Frappé'`).
- **`format_name`**: The name of the log format (e.g., `'Simple'`, `'Detailed'`).
- **`delimiter`**: (Optional) A custom delimiter to separate log parts.
- **`timestamp_format`**: (Optional) Customize the timestamp format using `strftime` directives.


## 📂 Available Themes and Formats

### 🎨 Themes

- **Catpuccin Latte**
- **Catpuccin Frappe**
- **Catpuccin Macchiato**
- **Catpuccin Mocha**
- **Tokyo Night**
- **Tokyo Night Storm**
- **Tokyo Night Light**

### 📝 Formats

| **Format**       | **Example**                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **Simple**       | `This is a DEBUG message.`                                                                                                      |
| **Detailed**     | `2024-11-28 15:11:49 \| DEBUG \| main \| main \| 39 \| This is a DEBUG message.`                                             |
| **Threaded**     | `2024-11-28 15:11:49 \| DEBUG \| MainThread \| This is a DEBUG message.`                                                   |
| **Process**      | `2024-11-28 15:11:49 \| DEBUG \| MainProcess \| This is a DEBUG message.`                                                  |
| **Left Aligned** | `DEBUG   : This is a DEBUG message.`                                                                                           |
| **Column**       | `2024-11-28 15:11:49 \| DEBUG \| main \| This is a DEBUG message.`                                                         |

## 🧪 Testing

LogStyles includes a comprehensive test suite using `unittest`. To run the tests, navigate to the project directory and execute:

```bash
python -m unittest discover tests
```

## 📄 License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For any inquiries or feedback, feel free to reach out:

- **Email**: [Justin@Lanfermann.DEV](mailto:Justin@Lanfermann.dev)
- **GitHub**: [Justin Lanfermann](https://github.com/jaylann)