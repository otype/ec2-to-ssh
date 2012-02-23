#!/usr/bin/env python
import sys
from Messages import  err
from aws.EC2SSH import EC2SSH
from loghandling.LogFacility import LogFacility

####################################################################
#
# CONFIGURATION PARAMETERS
#
####################################################################

# Logger
from settings.Settings import Settings

log = LogFacility().get_logger()

# Global settings dictionary
SETTINGS = Settings().settings

# If set to True, additional debug messages will be printed out
DEBUG = SETTINGS['DEBUGGING']

####################################################################
#
# FUNCTIONS
#
####################################################################


def main():
    if SETTINGS['EC2_AWS_ACCESS_KEY'] == '':
        sys.exit(err['ERR_NO_EC2_ACCESS_KEYS'])

    ec2ssh = EC2SSH(SETTINGS['EC2_AWS_ACCESS_KEY'], SETTINGS['EC2_AWS_SECRET_ACCESS_KEY'])

    print ec2ssh.print_instances()


####################################################################
#
# MAIN
#
####################################################################

if __name__ == "__main__":
    main()
