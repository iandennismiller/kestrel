# kestrel (c) 2013 Ian Dennis Miller

SHELL=/bin/bash

install:
	python setup.py install
	crontab etc/crontab.txt
	mkdir -p ~/.getmail ~/sieve

clean:
	rm -rf build dist *.egg-info *.pyc

depend:
	mkvirtualenv kestrel

.PHONY: clean install depend
