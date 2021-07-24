@echo off
:main
cls
q cubed4th\FORTH.py cubed4th\WORDS\F_CORE.py cubed4th\WORDS\*.py cubed4th\*.py
rem python -m cProfile -s ncalls forth.py | list /s
python forth.py
if errorlevel 1 goto end
goto main
:end
