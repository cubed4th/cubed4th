@echo off
del dist\*.* /F /Q /S /Y 2> nul
del build\*.* /F /Q /S /Y 2> nul
python setup.py clean
python setup.py install

attrib /d +h dist > nul
attrib /d +h build > nul
attrib /d +h cubed4th.egg-info > nul

pytest
