SHELL:=bash

.PHONY: run-local
run-local:
	bash -c "source .env && reflex run"