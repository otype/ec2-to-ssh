import boto.ec2
import sys
from Messages import err
from loghandling.LogFacility import LogFacility

####################################################################
# CONFIGURATION PARAMETERS
####################################################################

# Logger
from settings.Settings import Settings

log = LogFacility().get_logger()

# Global settings dictionary
SETTINGS = Settings().settings

####################################################################
# CLASS
####################################################################

class MissingAWSCredentialsException(Exception):
    def __init__(self, *args, **kwargs):
        super(MissingAWSCredentialsException, self).__init__(*args, **kwargs)

    def __str__(self):
        return super(MissingAWSCredentialsException, self).__str__()


class EC2SSH():
    # EC2 access keys
    ec2_aws_access_key = ''
    ec2_aws_secret_key = ''

    # list of EC2 instances
    instances = {}

    # the connection to Amazon
    connection = None

    def __init__(self, access_key, secret_key):
        if access_key is None or secret_key is None:
            raise MissingAWSCredentialsException(err['ERR_NO_EC2_ACCESS_KEYS'])

        self.ec2_aws_access_key = access_key
        self.ec2_aws_secret_key = secret_key
        self._connect()
        self._refresh_instances()

    def _connect(self):
        try:
            self.connection = boto.ec2.connect_to_region(
                region_name='eu-west-1',
                aws_access_key_id=self.ec2_aws_access_key,
                aws_secret_access_key=self.ec2_aws_secret_key
            )
        except boto.exception.EC2ResponseError, e:
            log.error(err['ERR_CANNOT_CONNECT_TO_AWS'])
            log.debug(e)
            sys.exit(err['ERR_CANNOT_CONNECT_TO_AWS'])

        return self.connection

    def _refresh_instances(self):
        """
        Get a list of all instances
        """
        reservations = self.connection.get_all_instances()
        instances = [i for r in reservations for i in r.instances]
        instances.sort()

        self.instances = instances

        #noinspection PySimplifyBooleanCheck
        if len(instances) == 0:
            sys.exit(err['ERR_NO_INSTANCES_FOUND'])

        return self.instances

    def print_instances(self):
        ssh_config = ''
        for instance in self.instances:
            if instance.state == 'running':
                try:
                    name = instance.tags['Name']
                except KeyError:
                    continue

                ssh_port = SETTINGS['ssh_port']
                if name.startswith('lb-') or name.startswith('loadbalancer-'):
                    ssh_port = 2222

                ssh_config += """
Host {hostname}
  HostName {public_dns_name}
  Port {ssh_port}
  IdentityFile {id_file}
  User {user}
""".format(
                    hostname=str(name).partition(' ')[0],
                    public_dns_name=instance.public_dns_name,
                    ssh_port=ssh_port,
                    id_file=SETTINGS['ssh_key_path'],
                    user=SETTINGS['ssh_user']
                )

        return ssh_config