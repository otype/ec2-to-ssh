# ec2-to-ssh

This is the EC2-to-SSH tool.

## Latest version

The latest is `0.2`.

## Motivation

Got tired of updating my SSH configuration over and over again. This here simply reads out all *running* EC2 instances
and prints them out to screen.

## Installing ec2-to-ssh

Install via `pip`:

	$ easy_install pip
	$ pip install git+ssh://git@github.com/otype/ec2-to-ssh.git@0.2

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


## Auto-update your SSH configuration

Simply create a shell function and add that to your shell configuration file (e.g. `~/.bashrc`):

	function update-ssh() {
	    EC2_AWS_ACCESS_KEY=<LIVE_KEY> EC2_AWS_SECRET_ACCESS_KEY=<LIVE_SECRET_KEY> ec2-to-ssh > ${HOME}/.ssh/config.liveplatform
	    EC2_AWS_ACCESS_KEY=<DEV_KEY> EC2_AWS_SECRET_ACCESS_KEY=<DEV_SECRET_KEY> ec2-to-ssh > ${HOME}/.ssh/config.devplatform

	    touch ${HOME}/.ssh/config
	    mv ${HOME}/.ssh/config ${HOME}/.ssh/config_old

		for f in ${HOME}/.ssh/config.*
		do
	        cat $f >> ${HOME}/.ssh/config
	    done
	}

Now, all I need to do before logging in into an EC2 instance is to call `update-ssh`.

*NOTE:* `ec2-to-ssh` needs to be in your path when calling `update-ssh` (which might not be if you are using `virtualenv`).

This way I don't overwrite all my other SSH configurations as these are simply in different files (`~/.ssh/config.<filename>`).


## TODO

- Provide DEV, LIVE, STAGE section in `settings.cfg` so that different configurations can be managed