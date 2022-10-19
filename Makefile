install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' streamlit_run.py

format:
	black *.py

all: install lint format