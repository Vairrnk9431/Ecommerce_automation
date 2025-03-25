@echo off
pytest -s -v -m "regression" --html=reports.html --browser chrome
pause

