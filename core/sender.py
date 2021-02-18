import logging
import logstash

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
        self._logger = logging.getLogger('python-logstash-logger')
        self._logger.setLevel(logging.INFO)
        self._logger.addHandler(logstash.TCPLogstashHandler(self.host, 5000, version=1))
        print("Setup completed successfully")


    def error(self, msg: str, extra = None):
        self._logger.error(msg, extra=extra)


    def info(self, msg: str, extra = None):
        self._logger.info(msg, extra=extra)


    def warning(self, msg: str, extra = None):
        self._logger.warning(msg, extra=extra)