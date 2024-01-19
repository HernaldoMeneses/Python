@echo off & rem Desativar a exibição dos omandos no console
set "current_directory=%CD%"
set "get_in_directory=chapter_02"
set "get_file=chapter_init.py"

set "where=%current_directory%/%get_in_directory%/"
set "what=%get_file%"

python %where%%what%
pause
