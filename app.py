"""Example of flask main file with logging."""
import os
import logging
from flask import Flask

# Ensure the log directory exists
os.makedirs('/tmp/logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    filename='/tmp/logs/app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

app = Flask(__name__)

@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    logging.info('Hello, EDP! endpoint was called')
    return 'Hello, EDP!'

if __name__ == '__main__':
    app.run()
