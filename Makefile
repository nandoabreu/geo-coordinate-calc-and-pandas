.ONESHELL:

.PHONY: test clean

virtualenv:
	@echo "Creating virtualenv..."
	virtualenv .venv
	@echo "Ready."

setup: virtualenv
	@echo "Installing requirements..."
	. .venv/bin/activate
	python3 -m pip install -r requirements.txt
	@echo "Ready."

test: setup
	@echo "\n### Running unittests... ###########"
	. .venv/bin/activate
	python3 -m unittest tests/test_*
	@echo "Done."
	$(MAKE) clean

clean:
	@echo "Cleaning up..."
	find . -type d -name '__pycache__' -exec rm -rf {} +
#	find . -type d -name '.venv' -exec rm -rf {} + >/dev/null 2>&1
	@echo "Done."

up: test
run: test
default: test

