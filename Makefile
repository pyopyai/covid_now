.PHONY: unittest install unistall

unittest:
	python3 -m unittest discover -v

install:
	python3 setup.py install

uninstall:
	pip3 uninstall covid-now -y

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -name "*pycache*" | xargs rm -rf