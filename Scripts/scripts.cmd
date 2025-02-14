@echo off
setlocal enabledelayedexpansion
set command=%1

REM Check if no command is provided
IF "%command%"=="" (
  set command=list
)

IF "%command%"=="list" (
  FOR %%I IN (C:\Users\lifeo\Desktop\Codes\Python\Scripts\*.py) DO (
    echo %%~nI
  )
) ELSE (
  py C:\Users\lifeo\Desktop\Codes\Python\Scripts\%command%.py
)