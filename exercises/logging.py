import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a file handler
fileHandler = logging.FileHandler('logging_exercise.log')
fileHandler.setLevel(logging.DEBUG)

# create stream handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

# create a logging format
fileformatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s')
consoleformatter = logging.Formatter('%(levelname)s - %(message)s')
fileHandler.setFormatter(fileformatter)
consoleHandler.setFormatter(consoleformatter)

# add the handlers to the logger
logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)


def f(x):
    if x > 0:
        raise ValueError("x >= 0, expects negative numbers only!")
    return x**3


if __name__ == "__main__":
    logger.info("Starting Program...")
    try:
        f(-2)
        f(44)
        f(-1)
    except ValueError as ex:
        logger.exception("Value Error!")
    else:
        logger.debug("tests passed!")
    finally:
        logger.warning("Try clause completed")
    logger.info("program finished running.")
