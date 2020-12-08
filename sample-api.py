import logging

from datetime import datetime
from flask import Flask, request


# Configure logger to show ALL messages
logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger()

logger.info('API initialized')

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def get_date(change_format=False):
    """
    Returns current date
    Args:
        change_format: if True, date is returned in YYYY-MM-DD-HH:MM:SS
                       if False, YYYY-MM-DD is used
    """
    date_format = '%Y-%m-%d'

    # reads parameter as python boolean for the following if statement
    change_format = eval(request.args.get('change_format'))

    logger.info(f'Parameter received: {change_format}')

    # if requested by the user: return with hh:mm:ss
    if change_format:
        date_format = '%Y-%m-%d-%H:%M:%S'

    curr_date = datetime.today().strftime(date_format)

    logger.info(f'Using format: {date_format}')
    logger.info(f'Current date: {curr_date}')

    return curr_date


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
