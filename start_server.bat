@echo off
echo Starting local web server for Final Prototype at http://localhost:8000
echo Once the server is running, you can stop it by pressing Ctrl+C.
python -m http.server 8000
pause
