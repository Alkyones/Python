@echo off
setlocal enabledelayedexpansion
set command=%1


IF "%command%"=="list" (
  FOR %%I IN (C:\Users\lifeo\Desktop\Python\Scripts\*.py) DO (
    echo %%~nI
  )
) ELSE (
  py C:\Users\lifeo\Desktop\Python\Scripts/%command%.py
)

