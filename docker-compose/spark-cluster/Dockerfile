FROM ubuntu:16.04
LABEL maintainer centrifugal4@gmail.com

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        wget \
        vim \ 
        ssh \
        scala \
        rsync \
        software-properties-common \
        python3-dev \
        python3-pip \
        python3-setuptools

# java install
# oracle-java9-installer not work for pyspark
RUN add-apt-repository ppa:webupd8team/java && apt-get update && \
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
    apt-get install -y --no-install-recommends oracle-java8-installer && \
    apt-get install -y --no-install-recommends oracle-java8-set-default && \
    rm -rf /var/lib/apt/lists/*

# spark install
ENV SPARK_INSTALL_ROOT=/opt/spark
WORKDIR $SPARK_INSTALL_ROOT

RUN wget http://mirror.navercorp.com/apache/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz && \
    tar xvf *.tgz && \
    rm -rf *.tgz && \
    find ./ -maxdepth 1 -name "spark*" -exec mv {} spark \; && \
    rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/oracle-jdk8-installer

# pyspark install
RUN pip3 install pyspark findspark
  
ENV SPARK_HOME=$SPARK_INSTALL_ROOT/spark
ENV PYSPARK_PYTHON=python3
ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /spark/logs
ENV PATH="${SPARK_HOME}/bin:${PATH}"
EXPOSE 8080 7077 6066 22

WORKDIR /workspace
