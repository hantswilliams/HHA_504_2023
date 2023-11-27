import logging

# create a logger, this is the object that will write to the log file
logger = logging.getLogger(__name__)

# create a file handler; this is the object that will write to the log file
handler = logging.FileHandler('WK9/code/python_logger_output/error.log')

# create a logging format; this is the format that will be used to write to the log file
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s \n \n')

# set the handler's format to the format we just created
handler.setFormatter(formatter)

# add the handler to the logger object
logger.addHandler(handler)

# set the logger's level // this is the level that will be written to the log file
# different levels are: DEBUG, INFO, WARNING, ERROR, CRITICAL
# for this example, we only want to log errors, but if we wanted to 
# log everything, we would set the level to DEBUG
logger.setLevel(logging.ERROR)

# create a function that throws an error
def error():
    try:
        1/0
    except Exception as e:
        print(e)
        logger.error(e, exc_info=True)

# call the function
error()