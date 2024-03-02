@echo off & rem Desativar a exibição dos omandos no console
set "current_directory=%CD%"
set "get_in_directory=chapter_01"
set "get_in_directory=chapter_02"
set "get_in_directory=chapter_03"
set "get_in_directory=03_listas"


set "get_file=01_chapter_init.py"
rem set "get_file=02_strings.py"
rem set "get_file=03_numeros.py"
rem set "get_file=04_comentarios.py"

rem set "get_file=01_listas.py"
set "get_file=02_listas.py"
set "get_file=03_Organizando.py"

set "where=%current_directory%/%get_in_directory%/"
set "what=%get_file%"

python %where%%what%

rem pause

