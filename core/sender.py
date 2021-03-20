from configparser import ConfigParser
from pathlib import Path
import logging
import logstash

def config_reader():
    config_file = Path(__file__).parent / 'config.ini'
    parser = ConfigParser()
    parser.read(config_file)
    return parser

configuration = config_reader()


class Sender:

    """
    Running example
    send = Sender(hostname)
    send.error("Error!!!")
    """

    def __init__(self, host):
        self.host = host
        self.setup_sender()


    def setup_sender(self):
        self._logger = logging.getLogger(configuration["ELASTIC"]["Index"])
        self._logger.setLevel(logging.INFO)
        self._logger.addHandler(logstash.TCPLogstashHandler(self.host, 5000, version=1))
        print("Setup completed successfully")


    def error(self, msg: str, extra = None):
        self._logger.error(msg, extra=extra)


    def info(self, msg: str, extra = None):
        self._logger.info(msg, extra=extra)


    def warning(self, msg: str, extra = None):
        self._logger.warning(msg, extra=extra)
