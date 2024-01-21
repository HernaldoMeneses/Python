@echo off & rem Desativar a exibição dos omandos no console
set "current_directory=%CD%"
set "get_in_directory=chapter_02"

set "get_file=chapter_init.py"
set "get_file=strings.py"

set "where=%current_directory%/%get_in_directory%/"
set "what=%get_file%"

python %where%%what%

rem pause

rem 57/592 - Concatenar strings