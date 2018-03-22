## Dockerfiles

### gpu-py3-caffe-tf
```
CUDA 8
cuDNN 6
Caffe 1.0
TensorFlow r1.4
```
dfgfdsgdfsgsdfg
### gpu-py3-caffe
Ref: https://github.com/BVLC/caffe/tree/master/docker
```
CUDA 8sdfsdafsdaf
cuDNN 6
Caffe 1.0
```

### Command
```
nvidia-docker build -t <IMAGE_ID> .
nvidia-docker run --name <CONTAINER_ID> -v /opt/workspace:/workspace -p 18888:8888 -td <IMAGE_ID>
nvidia-docker exec -it <CONTAINER_ID> /bin/bash
```
