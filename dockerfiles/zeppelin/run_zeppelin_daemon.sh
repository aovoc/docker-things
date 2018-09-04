#!/bin/bash
#
# Reference:
# https://zeppelin.apache.org/docs/0.7.0/install/docker.html
#
# centrifugal4@gmail.com
# ==============================================================================
docker pull apache/zeppelin:0.8.0

# Run Zeppelin in daemon mode Mounting logs and notebooks zeppelin to folders 
# on your host machine
docker run -p 7077:7077 -p 8080:8080 --privileged=true -v $PWD/logs:/logs \
           -v $PWD/notebook:/notebook -e ZEPPELIN_NOTEBOOK_DIR='/notebook' \
           -e ZEPPELIN_LOG_DIR='/logs' --name='zeppelin-on-mac-c' \
           -d apache/zeppelin:0.8.0
