WHEELS_DIR = 'dist/'

define help_banner
PyBase manager
==============

Usage:
    make [target]

Targets:

endef
export help_banner

help: ## Shows this help message.
	@printf "$$help_banner"
	egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "    \033[36m%-20s\033[0m %s\n", $$1, $$2}'


test: ## Run all test files.
	find tests/ -type f -name '*.py' | xargs -n1 python3


run: ## Run examples
	@printf "Running Flask usage example ...\nCtrl-C to exit"
	python3 examples/flask/to-do.py
	@printf "Running Discord.py usage example ...\nCtrl-C to exit"
	python3 examples/discord-py/hello.py


build: ## Build PyBase wheels
	@printf "Building wheels ...\n"
	python3 setup.py --quiet bdist_wheel
	@printf "Done, you can now install it from dist dir.\n"


install: ## Build PyBase wheel and install it
	@printf "Searching for old builds ...\n"
	if [ -d $(WHEELS_DIR) ]; then \
		rm -r $(WHEELS_DIR); \
		printf "Old builds were deleted.\n"; \
	fi
	make build
	@printf "Installing $(find dist/ -type f -name '*.whl') ...\n"
	find dist/ -type f -name '*.whl' | xargs python3 -m pip install --user -U


uninstall: ## Uninstall PyBase
	@printf "Uninstalling PyBase ...\n"
	python3 -m pip uninstall -y pybase_db
	@printf "Done, if you want to install it again just run 'make install'.\n"


reinstall: ## Reinstall PyBase, useful when there are changes to the source
	make uninstall
	make install

.PHONY: test run build install uninstall reinstall
.SILENT: help test run
