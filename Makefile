# kestrel (c) 2013 Ian Dennis Miller

install:
	python setup.py install
	crontab etc/crontab.txt
	mkdir -p ~/.getmail ~/sieve

clean:
	rm -rf build dist *.egg-info *.pyc

.PHONY: clean install
