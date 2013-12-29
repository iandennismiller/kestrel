# turkr (c) 2013 Ian Dennis Miller

SHELL=/bin/bash

install:
	python setup.py install
	kestrel_crontab.sh

clean:
	rm -rf build dist *.egg-info *.pyc

depend:
	mkvirtualenv kestrel

.PHONY: clean install depend
