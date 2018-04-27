## Dockerfiles

### caffe-tf
```
CUDA 8
cuDNN 6
Caffe 1.0
TensorFlow r1.4
```
### caffe
Ref: https://github.com/BVLC/caffe/tree/master/docker
```
CUDA 8
cuDNN 6
Caffe 1.0
```
### hadoop
```
hadoop 3.1.0
protobuf 2.5.0
```
### spark
```
spark 2.2.1 with pre-built hadoop 2.7 and later 
```
### jenkins
```
jenkins latest LTS (https://hub.docker.com/r/jenkins/jenkins/)
```

### Command
```
nvidia-docker build -t <IMAGE_ID> .
nvidia-docker run --name <CONTAINER_ID> -v /opt/workspace:/workspace -p 18888:8888 -td <IMAGE_ID>
nvidia-docker exec -it <CONTAINER_ID> /bin/bash
```

### Dockerfile command
#### CMD
```
# Can not use shell variables format. ex. $HOME
CMD ["executable", "arg1", "arg2", ...]

CMD command arg1 arg2 ...

#Require ENTRYPOINT to specify executable
CMD ["arg1", "arg2"...]
```
