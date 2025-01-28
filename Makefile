install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_ *.py

build-container:
	docker build -t ingest_data .

refactor: format lint

		
all: install lint format build-container deploy