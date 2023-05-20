test:
	@echo "Running default pytest"
	PYTHONDONTWRITEBYTECODE=1 pytest

test-debug:
	@echo "Running pytest in debug mode: -s -v -x"
	PYTHONDONTWRITEBYTECODE=1 pytest -s -v -x
