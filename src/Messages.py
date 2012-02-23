#
# REGULAR MESSAGES
#
#noinspection PyDictCreation
msg = {}


#
# ERROR MESSAGES
#
#noinspection PyDictCreation
err = {}
err['ERR_NO_EC2_ACCESS_KEYS'] = '''No AWS access keys found!

Please do one of the following:

Option #1: Set environment variables

  $ export EC2_AWS_ACCESS_KEY=<your_access_key>
  $ export EC2_AWS_SECRET_ACCESS_KEY=<your_secret_access_key>

Option #2: Add your credentials to ~/.ec2ssh/settings.cfg

  $ vi ~/.ec2ssh/settings.cfg

  [EC2]
  EC2_AWS_ACCESS_KEY = <your_access_key>
  EC2_AWS_SECRET_ACCESS_KEY = <your_secret_access_key>

'''

err['ERR_CANNOT_CONNECT_TO_AWS'] = '''Cannot connect to AWS!'''
err['ERR_NO_INSTANCES_FOUND'] = ''''No EC2 instances found! Make sure you are connecting to the right region!'''
