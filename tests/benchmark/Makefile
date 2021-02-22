OLD_BENCHS_DIR = '.benchmarks'

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
	

benchmark: ## Run benchmark tests (REQUIRES PYTEST-BENCHMARK)
	@printf "Cleaning old benchmark test files and residual data if they exists ...\n"
	if [ -d $(OLD_BENCHS_DIR) ]; then \
		rm -r db tmp __pycache__ ; \
	fi
	@printf "Running benchmark test ...\n"
	py.test --benchmark-min-time=0.1 --benchmark-autosave test_benchmark.py

.PHONY: benchmark
.SILENT: help
