import os
from settings.Settings import Settings

DEFAULT_CONFIG_FILE = os.path.join(os.environ['HOME'], '.ec2ssh/settings.cfg')
CONFIG = Settings().read_configuration(DEFAULT_CONFIG_FILE)

def initialize_settings():
    """
        Read in ~/.ec2ssh/settings.cfg into settings dictionary
    """
    #noinspection PyDictCreation
    s = {}

    s['ssh_key_path'] = CONFIG.get('SSH_CONFIG', 'SSH_KEY')
    if s['ssh_key_path'] is None or not os.path.exists(s['ssh_key_path']):
        s['ssh_key_path'] = os.path.join(os.environ['HOME'], '.ssh/id_rsa')

    s['ssh_port'] = '22'
    if CONFIG.has_option('SSH_CONFIG', 'SSH_PORT'):
        s['ssh_port'] = CONFIG.get('SSH_CONFIG', 'SSH_PORT')

    s['ssh_user'] = 'ubuntu'
    if CONFIG.has_option('SSH_CONFIG', 'SSH_USER'):
        s['ssh_user'] = CONFIG.get('SSH_CONFIG', 'SSH_USER')

    s['EC2_AWS_ACCESS_KEY'] = ''
    if os.environ.has_key('EC2_AWS_ACCESS_KEY'):
        s['EC2_AWS_ACCESS_KEY'] = os.environ['EC2_AWS_ACCESS_KEY']
    else:
        if CONFIG.has_option('EC2', 'EC2_AWS_ACCESS_KEY'):
            s['EC2_AWS_ACCESS_KEY'] = CONFIG.get('EC2', 'EC2_AWS_ACCESS_KEY')

    s['EC2_AWS_SECRET_ACCESS_KEY'] = ''
    if os.environ.has_key('EC2_AWS_SECRET_ACCESS_KEY'):
        s['EC2_AWS_SECRET_ACCESS_KEY'] = os.environ['EC2_AWS_SECRET_ACCESS_KEY']
    else:
        if CONFIG.has_option('EC2', 'EC2_AWS_SECRET_ACCESS_KEY'):
            s['EC2_AWS_SECRET_ACCESS_KEY'] = CONFIG.get('EC2', 'EC2_AWS_SECRET_ACCESS_KEY')

    s['DEBUGGING'] = False
    if CONFIG.has_option('DEBUG', 'DEBUGGING'):
        s['DEBUGGING'] = CONFIG.get('DEBUG', 'DEBUGGING')

    return s
