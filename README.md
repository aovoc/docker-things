## Dockerfiles

### gpu-py3-caffe-tf
```
CUDA 8
cuDNN 6
Caffe 1.0
TensorFlow r1.4
```

### gpu-py3-caffe
Ref: https://github.com/BVLC/caffe/tree/master/docker
```
CUDA 8
cuDNN 6
Caffe 1.0
```

### Command
```
nvidia-docker build -t test .
nvidia-docker run --name test -v /opt/workspace:/workspace -p 18888:8888 -td <IMAGE_ID>
nvidia-docker exec -it <IMAGE_ID> /bin/bash
```
