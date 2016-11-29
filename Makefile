all:
	python3 mmeter/mmeter.py

test:
	python3 -m unittest tests/test_sanity.py