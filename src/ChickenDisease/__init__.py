### logging logic code will be written in "src/ChickenDisease/__init__.py" instead of making own seperate folder for simplicity.
### alternatively, you can create a separate folder named "logging" and place this code there.
# This is the logging configuration for the Chicken Disease Classification project.
# It initializes the logging configuration for the project, allowing for detailed tracking of events and errors.
# The logging configuration is set to log messages at the INFO level and above.
# The log messages will be formatted to include the timestamp, log level, module name, for better traceability.
# The logs will be written to a file named "running_logs.log" in the "logs" directory and also printed to the console.
# This setup is useful for debugging and monitoring the application's behavior during execution.
# It sets up logging to both a file and the console, allowing for easy tracking of events and errors during execution.
import os
import sys
import logging

## %(asctime)s:     The time when the log message was created, formatted as YYYY-MM-DD HH:MM:SS, e.g., 2023-10-01 12:34:56

    # -%:           This is a placeholder marker used in Python's logging format strings. It tells the logger to substitute the 
    #               value of a logging attribute.

    # -asctime:     This is a logging attribute that stands for "ASCII time". 
    #               It will be replaced by the timestamp of when the log record was created (e.g., 2025-06-25 14:30:00).

    # -s:           In this context, the 's' is not a standalone variable. 
    #               It is part of the format syntax: %(asctime)s. 
    #               The 's' at the end is required by the old-style Python string formatting to indicate that the value should be 
    #               formatted as a string.

## %(levelname)s: The severity level of the log message (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
## %(module)s: The name of the module (Python file) where the log message originated.
## %(message)s: The actual log message content.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Set up logging configuration
logging.basicConfig(level= logging.INFO,
                    format= logging_str,
                    handlers=[logging.FileHandler(filename=log_filepath),
                              logging.StreamHandler(sys.stdout)]) # StreamHandler(sys.stdout) allows logging to be printed to the console

# Create a logger object for the Chicken Disease Classification project                 
logger = logging.getLogger(name="ChickenDisease_Logger")