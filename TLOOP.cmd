@echo off
:main
cls
call TESTS.cmd
pause
q tests\*.py
goto main
:end
