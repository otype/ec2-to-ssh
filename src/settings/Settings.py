import ConfigParser
import os
import sys

class Settings(object):
    if sys.platform == 'win32':
        home = os.path.expanduser('~')
    else:
        home = os.getenv("HOME")

    default_configuration_file_name = os.path.join(home, '.ec2ssh/settings.cfg')

    def read_configuration(self, configuration_file=None):
        """
            Read the configuration file
        """
        # Check if we have received a different configuration file name
        if configuration_file is None:
            configuration_file = self.default_configuration_file_name

        # Check if the file even exists! If not, we have to write a default configuration file.
        if not os.path.exists(configuration_file):
            sys.exit('Configuration file {0} not found!'.format(configuration_file))

        # Read the configuration file
        config = ConfigParser.RawConfigParser()
        config.read(configuration_file)

        return config
