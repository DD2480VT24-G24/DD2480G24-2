.PHONY: docs

docs:
	cd docs && $(MAKE) html
	cd docs && sphinx-build -b pdf source build/pdf
