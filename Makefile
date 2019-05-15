
wheel:
	python3 setup.py bdist_wheel

install:
	python3 -m pip install ./dist/*.whl