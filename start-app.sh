#!/bin/bash


cd /opt/kurohai.com

# activate virtual env
source ./bin/activate

# start nginx
uwsgi --emperor ./vassals --master --enable-threads
