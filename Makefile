# Makefile
format-black:
	@black .
format-isort:
	@isort .
lint-black:
	@black . --check
lint-isort:
	@isort . --check
lint-flake8:
	@flake8 .
lint-mypy:
	@mypy ./src
lint-mypy-report:
	@mypy ./src --html-report ./mypy_html

format: format-black format-isort
lint: lint-black lint-isort lint-flake8 lint-mypy

##@ Documentation
#docs-build: ## build documentation locally
#   @mkdocs build

#docs-deploy: ## build & deploy documentation to "gh-pages" branch
#   @mkdocs gh-deploy -m "docs: update documentation" -v --force

#clean-docs: ## remove output files from mkdocs
#   @rm -rf site
