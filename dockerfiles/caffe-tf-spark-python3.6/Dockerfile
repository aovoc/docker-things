FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04
LABEL maintainer seo@algorigo.com

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        pkg-config \
        vim \
        ssh \
        libssl-dev zlib1g-dev libbz2-dev \
        libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
        xz-utils tk-dev libffi-dev && \
    rm -rf /var/lib/apt/lists/*

ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PATH:$PYENV_ROOT/bin:$PYENV_ROOT/shims

# CUDA
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/lib/x86_64-linux-gnu:/usr/local/cuda/lib64:/opt/boost/lib

# pyenv
WORKDIR $HOME
COPY requirements.txt requirements.txt
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.6.4 && pyenv global 3.6.4 && \
    pip3 install -r requirements.txt

# boost
COPY project-config.jam project-config.jam
RUN wget https://dl.bintray.com/boostorg/release/1.67.0/source/boost_1_67_0.tar.gz && \
    mkdir boost && tar zxf boost*.tar.gz -C boost --strip-components=1 && rm boost*.tar.gz && \
    cd boost && ./bootstrap.sh && mv ../project-config.jam . && ./b2 --prefix=/opt/boost install -j $(($(nproc) + 1)) && cd .. && rm -r boost

# NCCL and caffe
ENV CAFFE_ROOT=/opt/caffe
WORKDIR $CAFFE_ROOT
RUN git clone --depth 1 https://github.com/BVLC/caffe.git
COPY Makefile.config Makefile.config
RUN git clone https://github.com/NVIDIA/nccl.git && \
    cd nccl && make -j install && cd .. && rm -rf nccl
RUN make all -j $(($(nproc) + 1)) && make pycaffe -j $(($(nproc) + 1)) && make distribute -j $(($(nproc) + 1))
ENV PYCAFFE_ROOT $CAFFE_ROOT/python
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

# java install
# oracle-java9-installer not work for pyspark
RUN add-apt-repository ppa:webupd8team/java && apt-get update && \
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
    apt-get install -y --no-install-recommends oracle-java8-installer && \
    apt-get install -y --no-install-recommends oracle-java8-set-default && \
    rm -rf /var/lib/apt/lists/*

# spark install
ENV SPARK_INSTALL_ROOT=/opt/spark
ENV SPARK_HOME=$SPARK_INSTALL_ROOT/spark
WORKDIR $SPARK_INSTALL_ROOT
RUN wget http://mirror.navercorp.com/apache/spark/spark-2.2.1/spark-2.2.1-bin-hadoop2.7.tgz && \
    tar xvf *.tgz && \
    rm -rf *.tgz && \
    find ./ -maxdepth 1 -name "spark*" -exec mv {} spark \; && \
    rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/oracle-jdk8-installer

# pyspark install
RUN pip3 install --upgrade pip && \
    pip3 install pyspark findspark

# run jupyter server
RUN jupyter notebook --generate-config 
COPY jupyter_notebook_config.py $HOME/.jupyter/

WORKDIR /workspace
CMD jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root
