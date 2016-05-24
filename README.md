WhatsAPP Share
==================================

Share web data on whatsapp.

# Installation

## Install OS (Ubuntu) Requirements

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install vim-gnome build-essential git-core python-dev python-virtualenv python-MySQLdb

## Clone Project

    git clone https://github.com/agnihotri/whatsapp_share.git

## Virtual Envirnoment and requirements

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Sync database.

    python manage.py syncdb

## Running Development Server

    python manage.py runserver

**Note:** Never forget to enable virtual environment (`source env/bin/activate`) before running above command and use settings accordingly.
