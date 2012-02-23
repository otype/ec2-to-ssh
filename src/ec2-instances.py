#!/usr/bin/env python
import sys
from Messages import  err
from aws.EC2 import EC2
from loghandling.LogFacility import LogFacility
from settings import initialize_settings

####################################################################
#
# CONFIGURATION PARAMETERS
#
####################################################################

# Logger
log = LogFacility().get_logger()

# Global settings dictionary
SETTINGS = initialize_settings()

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

    ec2 = EC2(SETTINGS['EC2_AWS_ACCESS_KEY'], SETTINGS['EC2_AWS_SECRET_ACCESS_KEY'])
    instances = ec2.refresh_instances()

    if DEBUG:
        print('instances: {0}   - size: {1}'.format(instances, len(instances)))

    if not len(instances):
        sys.exit(err['ERR_NO_INSTANCES_FOUND'])

    for i in instances:
        try:
            name = i.tags['Name']
        except KeyError:
            continue

        ssh_port = SETTINGS['ssh_port']
        if name.startswith('lb-'):
            ssh_port = 2222
        print ''
        print 'Host', str(name).partition(' ')[0]
        print '  HostName', i.public_dns_name
        print '  Port', ssh_port
        print '  IdentityFile', SETTINGS['ssh_key_path']
        print '  User', SETTINGS['ssh_user']


####################################################################
#
# MAIN
#
####################################################################

if __name__ == "__main__":
    main()
