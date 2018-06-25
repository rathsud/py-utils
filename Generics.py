BASE_PYTHON_LAYOUT = '''import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.disabled = False

try:
    import MessageBundle
except ImportError as ie:
    logger.log(level=logging.critical('UnableToImportMessageBundle', ie))
    sys.exit(1)


def main():
    
    return


if __name__ == '__main__':
    main()
'''