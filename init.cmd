@echo off & rem Desativar a exibição dos omandos no console
set "current_directory=%CD%"
set "get_in_directory=chapter_01"
set "get_file=chapter_init.py"
rem echo %current_directory%
rem echo %get_in_directory%
rem echo %current_directory%/%get_in_directory%/%get_file%
rem call %current_directory%/%get_in_directory%/%get_file%
python %current_directory%/%get_in_directory%/%get_file%
pause