.PHONY: all

all: prepare run eval

prepare:
	@echo "Running bootstrap.sh..."
	@bash bootstrap.sh

run:
	@echo "activating venv"
	@. ./venv/bin/activate && bash run.sh



eval:
	@echo "Running eval.py..."
	@python3 eval.py
