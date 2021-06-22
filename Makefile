# Use shell as default (allow use source)
SHELL := /bin/bash
.PHONY: prepare

ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
VENV_DIR:=$(ROOT_DIR)/gilfoyle-vnev
VENV_ACTIVATION_PATH:=$(VENV_DIR)/bin/activate

prepare : 
	@echo "Working dir: ${ROOT_DIR}";
	@if [ -d ${VENV_DIR} ]; then \
	(\
		echo "Venv alread created - entering in venv"; \
		source ${VENV_ACTIVATION_PATH}; \
		pip install -r requirements.txt;\
		echo "Work done - you can now use gilfoyle without breaking you python instalation!";\
	)\
	else \
	(\
		echo "Venv not created yet - starting Venv creation"; \
		python3 --version; \
		pip --version; \
		echo "Installing virtual env for puthon..."; \
		python3 -m pip install --user virtualenv; \
		python3 -m venv ${VENV_DIR}; \
		make prepare;\
	)\
	fi


pip-freeze: 
	@python3 -m pip freeze > requirements.txt

test: 
	@ cd src && python -m pytest tests && cd ..

