run: venv/bin/activate
	./venv/bin/python3 src/cli/wxmon.py

install:
	python3 -m pip install -r requirements.txt

debug:
	./venv/bin/python3 -m IPython	

clean:
	rm -rf __pycache__
	rm -rf venv

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt