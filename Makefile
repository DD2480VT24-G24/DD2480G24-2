PYTHON = python3
PYRIGHT = pyright

.PHONY: docs test build

build:
	$(PYRIGHT) src/ tests/

test:
	cd tests && $(PYTHON) -m unittest

docs:
	cd docs && $(MAKE) html
	cd docs && sphinx-build -b pdf source build/pdf


