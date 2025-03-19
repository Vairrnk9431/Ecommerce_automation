@echo off
cd /d "C:\Users\vairo\OneDrive\Desktop\Selenium\nopcommerce"  REM Change to project directory
call ..\.venv\Scripts\activate  REM Go up one level to activate venv
pytest -s -v -m "regression" --html=reports.html --browser chrome
pause

