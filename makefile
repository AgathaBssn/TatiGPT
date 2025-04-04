SHELL:=bash

.PHONY: run-local
run-local:
	bash -c "source .env && reflex run"

.PHONY: pre-commit
pre-commit:
	pre-commit run --all-files
