.DEFAULT_GOAL := help
include *.mk

.PHONY: help
help: ## Print Makefile help
	@grep -Eh '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## Remove build and run artifacts
	-rm -rf .pytest_cache
	-rm -rf .tox
	-rm -rf tests/__pycache__
	-rm -rf *.egg-info/

.PHONY: test
test: ## Run tests
	tox
