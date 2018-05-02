FROM jenkins:latest
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    wget \
    vim \
    ssh \
    python3-dev \
    python3-pip \
    python3-setuptools \
  && rm -rf /var/lib/apt/lists/*
