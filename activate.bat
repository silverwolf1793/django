@echo off
cd /d .\Scripts & activate & cd /d ../crm1 & python manage.py runserver 192.168.1.253:80
pause