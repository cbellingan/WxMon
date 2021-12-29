run: venv/bin/activate
	PYTHONPATH=$PYTHONPATH:./src:./ ./venv/bin/python3 src/ui/wxmon.py

server: venv/bin/activate
	PYTHONPATH=$PYTHONPATH:./src:./  ./venv/bin/python3 src/ui/image_server.py

install:
	python3 -m pip install -r requirements.txt

debug:
	PYTHONPATH=$PYTHONPATH:./src:./:/usr/local/lib/python3.7/dist-packages ./venv/bin/python3 -m IPython	

test-integ: venv/bin/activate
	PYTHONPATH=$PYTHONPATH:./src:./:/usr/local/lib/python3.7/dist-packages  ./venv/bin/python3 -m unittest test_integ/*.py

test: venv/bin/activate
	PYTHONPATH=$PYTHONPATH:./src:/usr/local/lib/python3.7/dist-packages  ./venv/bin/python3 -m unittest tests/*.py

clean:
	rm -rf __pycache__
	rm -rf venv

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt