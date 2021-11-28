run: 
	python src/cli/wxmon.py

install:
	python3 -m pip install -r requirements.txt

clean:
	rm -rf __pycache__
