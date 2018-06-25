import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.disabled = False

try:
    import Generics
except ImportError as ie:
    logger.log(level=logging.critical('UnableToImportGenerics', ie))
    sys.exit(1)


def main():
    logging.debug(len(sys.argv))
    if len(sys.argv) == 3:
        _, output_, msgbndl_ = sys.argv
        logging.debug(output_, msgbndl_)
    else:
        output_ = 'output.py'
        msgbndl_ = 'MessageBundle.py'

    with open(output_, 'w') as f:
        f.write(Generics.BASE_PYTHON_LAYOUT)

    try:
        open(msgbndl_, 'x')
    except FileExistsError:
        logger.log(level=logging.critical('FileExistsCannotCreateNew'))
        sys.exit(1)

    return


if __name__ == '__main__':
    main()
