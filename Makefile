.PHONY: test clean

virtualenv:
	@echo "Creating virtualenv..."
	virtualenv .venv >/dev/null 2>&1
	source .venv/bin/activate
	@echo "Ready."

setup: virtualenv
	@echo "Installing requirements..."
	python3 -m pip install -r requirements.txt >/dev/null 2>&1
	@echo "Ready."

test: setup
	@echo "\n### Running unittests... ###########"
	python3 -m unittest tests/test_*
	@echo "Done."
	$(MAKE) clean

clean:
	@echo "Cleaning up..."
	#find . -not -path '*/\.*' -name __pycache__ -exec ls {} +
	@echo "Done."

up: test
run: test
default: test

