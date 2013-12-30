kestrel
=======

Collect email from POP/IMAP servers and apply sorting rules; a simple framework for getmail4 and procmail/sieve.

Usage
=====

First, make sure kestrel is installed.  See installation instructions for more information.

Start inside an empty directory called 'kestrel-myname-conf' and create a blank kestrel project.

    workon kestrel
    mkdir kestrel-myname-conf && cd kestrel-myname-conf
    kestrel_init.py

This directory might be useful to manage with version control, like with git.

Kestrel uses getmail to periodically download email from your mail servers.  If you place a getmail configuration file in `kestrel-myname-conf/getmail/0015.d`, it will run every 15 minutes.  The various folders are named after military time, such that 2400.d runs every 24 hours (i.e. once per day), 0100.d runs once per hour, and 0001.d runs every minute.

So let's set up kestrel to check gmail every 15 minutes.  Once we've created the file, we will open it set the hostname, username, and password.

    kestrel_newconf.py getmail/0015.d/myself_at_gmail_com.conf
    vi getmail/0015.d/myself_at_gmail_com.conf

Next, let's create some mail sorting rules.

    vi sieve/default.sieve

Now that everything is configured, we update getmail with our settings and wait for cron to call getmail.

    kestrel_update.py
    ln -s ~/sieve/default.sieve ~/.dovecot.sieve

Installation
============

    apt-get install getmail4 procmail spamassassin virtualenvwrapper daemontools
    git clone git@github.com:iandennismiller/kestrel
    cd kestrel
    mkvirtualenv kestrel
    make install

Credits
=======

[OS_X_Mail_app_rules_to_sieve_filters](http://mechanicalcat.net/richard/log/Python/OS_X_Mail_app_rules_to_sieve_filters)
