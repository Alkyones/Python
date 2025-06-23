@echo off
setlocal enabledelayedexpansion

set command=%1
shift

REM Check if no command is provided
IF "%command%"=="" (
  set command=list
)

IF "%command%"=="list" (
  FOR %%I IN (C:\Users\lifeo\Desktop\Codes\Python\Scripts\*.py) DO (
    echo %%~nI
  )
) ELSE (
  REM Prepare the arguments string
  set args=

  REM Collect all remaining arguments
  :collect_args
  IF "%~1"=="" (
    REM No more arguments
    goto run_script
  )
  set args=!args! "%~1"
  shift
  goto collect_args

  :run_script
  REM Run the Python script with the collected arguments
  py C:\Users\lifeo\Desktop\Codes\Python\Scripts\%command%.py !args!
)