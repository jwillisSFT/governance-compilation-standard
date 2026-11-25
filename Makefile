.PHONY: validate bounded all

validate:
	python tools/validate_repo.py

bounded:
	python validation/bounded-analytical-suite/run_bounded_validation.py

all: validate bounded
