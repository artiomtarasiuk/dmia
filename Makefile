.PHONY: format check_format test
.ONESHELL:

check_dirs := dmia

format:
	black $(check_dirs)
	isort $(check_dirs)

check_format:
	black --check $(check_dirs)
	isort --check-only $(check_dirs)

test: check_format
	safety check