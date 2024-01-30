rem creat scredule
rem schtasks /create /sc second /mo 1 /tn "MinhaTarefa" /tr "L:\GitHub\LineBy_Python\init.cmd"
rem to remove later
rem schtasks /delete /tn "MinhaTarefa" /f
rem to list all task created
rem schtasks /query
rem poque o windows não suporta intervalos curtos para agendar task
python schedule_config.py
pause

rem 57/592 - Concatenar strings