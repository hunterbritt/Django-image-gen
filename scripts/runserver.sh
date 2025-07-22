#!/bin/bash


cd .. && cd core/ && \
python manage.py check && \
python manage.py runserver --verbosity 3 && \ 
cd ..

