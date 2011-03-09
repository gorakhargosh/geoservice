#!/bin/sh

killall geoservice
bin/geoservice -p 8080 -a 127.0.0.1 &
bin/geoservice -p 8081 -a 127.0.0.1 &
bin/geoservice -p 8082 -a 127.0.0.1 &
