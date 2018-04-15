FROM ubuntu:16.04
LABEL maintainer centrifugal4@gmail.com

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        openjdk-8-jdk \
        maven \
        autoconf \
        automake \
        libtool \
        curl \
        make \
        g++ \
        unzip \
        cmake \
        wget \
        vim \ 
        ssh \
        software-properties-common \
        python3-dev \
        python3-pip \
        python3-setuptools

# protobuf. https://github.com/google/protobuf/tree/master/src
# Use protobuf v2.50. Check 'hadoop-project/pom.xml'
# RUN wget https://github.com/google/protobuf/archive/v3.2.0.tar.gz && \
RUN wget https://github.com/google/protobuf/releases/download/v2.5.0/protobuf-2.5.0.tar.gz && \
        tar zxvf protobuf-2.5.0.tar.gz && \
        cd protobuf-2.5.0 && \
        ./configure && \
        make && \
        make install && \
        ldconfig && \
        cd .. && \
        rm -rf protobuf-2.5.0.tar.gz && \
        rm -rf protobuf-2.5.0

## Reference. http://wiki.lofarolabs.com/index.php/Compile_Hadoop_Source_Code
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
RUN wget http://mirror.navercorp.com/apache/hadoop/common/hadoop-3.1.0/hadoop-3.1.0-src.tar.gz && \
       tar zxvf hadoop-3.1.0-src.tar.gz && \
       cd hadoop-3.1.0-src && \
       mvn package -Pdist -Pdoc -Psrc -Dtar -DskipTests && \
       cp hadoop-dist/target/hadoop-3.1.0.tar.gz /workspace/

WORKDIR /workspace
