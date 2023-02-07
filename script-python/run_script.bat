@REM @echo off
@REM call .\venv_376\Scripts\activate.bat .\venv_376
@REM ".\venv_376\Scripts\python.exe" ".\my_watchdog.py"

@REM @echo off
@REM call "C:\Program Files\Anaconda3\Scripts\activate.bat" "C:\Program Files\Anaconda3"
@REM "C:\Program Files\Anaconda3\python.exe" "C:\Users\x627619\OneDrive - Santander Office 365\Documentos\development\script-python\my_watchdog.py"
@REM pause

@REM @echo off
@REM call conda activate base
@REM "C:\Program Files\Anaconda3\python.exe" "C:\Users\x627619\OneDrive - Santander Office 365\Documentos\development\script-python\my_watchdog.py"
@REM pause

cmd "/c conda activate && python my_watchdog.py"