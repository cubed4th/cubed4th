@echo off
python setup.py sdist bdist_wheel
python -m twine upload --verbose dist/*
