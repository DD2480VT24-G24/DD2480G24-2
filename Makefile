PYTHON = python3
PYRIGHT = pyright
INSTALL = pip install

.PHONY: docs test build install 

install:
	$(INSTALL) -r requirements.txt

build:
	$(PYRIGHT) src/ tests/

test:
	$(PYTHON) -m unittest discover -s tests

docs:
	cd docs && $(MAKE) html
	cd docs && sphinx-build -b pdf source build/pdf

.DEFAULT_GOAL := all

all: install build test docs