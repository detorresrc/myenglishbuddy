#!/bin/sh
cd /home/detorresrc/Projects/python/myenglishbuddy/venv/lib/python3.11/site-packages
zip -r ../../../../my_deployment_package.zip .

cd /home/detorresrc/Projects/python/myenglishbuddy

zip my_deployment_package.zip *.py 
