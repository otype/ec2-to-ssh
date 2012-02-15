import logging

class LogFacility(object):
    log_levels   = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

    logger       = 'main'
    log_format   = '%(asctime)-15s %(name)s %(levelname)s %(message)s'
    log_dir      = './log'
    log_filename = '{0}.log'.format(logger)


    def __init__(self):
        """
            Initialize LogFacility
        """
        super(LogFacility, self).__init__()

        self.log_formatter = logging.Formatter(self.log_format)
        self.log_file      = '{0}/{1}'.format(self.log_dir, self.log_filename)
        self.log_handler   = logging.FileHandler(self.log_file)
        self.log_handler.setFormatter(self.log_formatter)


    def get_logger(self, logger=None):
        """
            Create the logger object and return it back
        """
        if logger is None:
            logger = self.logger

        log = logging.getLogger(logger)
        log.addHandler(self.log_handler)
        log.setLevel(logging.DEBUG)

        return log
