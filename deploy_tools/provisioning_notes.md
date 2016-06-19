Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:
	sudo apt-get install nginx git python3 python3-pip
	sudo pip install virtualenv

## nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with , eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder Structure:
Assume we have a user account at /home/username

/home/username
|___Sites
    |___SITENAME
        |___database
        |___source
        |___static
        |___virtualenv
