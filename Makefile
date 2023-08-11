.DEFAULT_GOAL := help
.PHONY: help
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Formatters

format-black: ## run black (code formatter)
	@black .

format-isort: ## run isort (imports formatter)
	@isort .

##@ Linters

lint-black: ## run black in linting mode
	@black . --check

lint-isort: ## run isort in linting mode
	@isort . --check

lint-flake8: ## run flake8 (code linter)
	@flake8 .

lint-mypy: ## run mypy (static-type checker)
	@mypy ./car_rental

lint-mypy-report: # run mypy & create report
	@mypy ./car_rental --html-report ./mypy_html

##@ Tests
unit-tests: ## run tests
	@pytest 
unit-tests-cov: ## run tests coverage
	@pytest --cov=car_rental --cov-report term-missing --cov-report=html
unit-tests-cov-fail: ## run tests coverage and fail under 80
	@pytest --cov=car_rental --cov-report term-missing --cov-report=html --cov-fail-under=80
clean-cov: ## clean coverage
	@rm -rf .coverage
	@rm -rf htmlcov
	@rm -rf pytest.xml
	@rm -rf pytest-coverage.txt

##@ Documentation
docs-build: ## build documentation locally
	@mkdocs build

docs-deploy: ## build & deploy documentation to "gh-pages" branch
	@mkdocs gh-deploy -m "docs: update documentation" -v --force

clean-docs: ## remove output files from mkdocs
	@rm -rf site

format: format-black format-isort ## run all formatters
lint: lint-black lint-isort lint-flake8 ## run all linters
