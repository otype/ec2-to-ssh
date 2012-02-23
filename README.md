# ec2-to-ssh

This is the EC2-to-SSH tool.

## Latest version

The latest is `0.1-pre_alpha`.

## Motivation

Got tired of updating my SSH configuration over and over again. This here simply reads out all *running* EC2 instances
and prints them out to screen.

## Setting up ec2-to-ssh

1. Install via `pip`:

	$ easy_install pip
	$ pip install git+ssh://git@github.com/otype/ec2-to-ssh.git@0.1-pre_alpha

2. Clone this project and simply run:

	$ python setup.py install

## Configuring ec2-to-ssh

Before you can run `ec2-to-ssh` you must configure the configuration file `${HOME}/.ec2ssh/settings.cfg` and fill
 in appropriate values:

    [SSH_CONFIG]
    SSH_KEY = /Users/hgschmidt/.ssh/<your_ec2_ssh_key>
    SSH_PORT = 22
    SSH_USER = ubuntu

## Using ec2-to-ssh

You can either set environment variables and call `ec2-to-ssh`:

	$ EC2_ACCESS_KEY=ABCDEFGHIJK EC2_SECRET_ACCESS_KEY=ALONGSECRETKEY ec2-to-ssh

Or you can set your Access Keys in the configuration file `${HOME}/.ec2ssh/settings.cfg`:

	[EC2]
    EC2_AWS_ACCESS_KEY = <put_your_key_key>
    EC2_AWS_SECRET_ACCESS_KEY = <put_your_secret_key_here>

