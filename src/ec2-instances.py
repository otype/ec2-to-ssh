#!/usr/bin/env python
import boto
import boto.ec2
import sys
from Messages import msg, err
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

def ec2_instances():
    """
        Get a list of all instances
    """
    if SETTINGS['EC2_AWS_ACCESS_KEY'] == '':
        sys.exit(err['ERR_NO_EC2_ACCESS_KEYS'])

    try:
        connection = boto.ec2.connect_to_region(
            'eu-west-1',
            aws_access_key_id=SETTINGS['EC2_AWS_ACCESS_KEY'],
            aws_secret_access_key=SETTINGS['EC2_AWS_SECRET_ACCESS_KEY']
        )
        log.debug(connection.__dict__)
    except boto.exception.EC2ResponseError, e:
        log.error(err['ERR_CANNOT_CONNECT_TO_AWS'])
        log.debug(e)
        sys.exit(err['ERR_CANNOT_CONNECT_TO_AWS'])

    reservations = connection.get_all_instances()
    instances = [i for r in reservations for i in r.instances]
    instances.sort()

    return instances


def main():
    instances = ec2_instances()

    if DEBUG:
        print('instances: {0}   - size: {1}'.format(instances, len(instances)))

    if not len(instances):
        sys.exit('No instances found!')

    for i in instances:
        if DEBUG:
            print(i.__dict__)

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
