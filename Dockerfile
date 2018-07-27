FROM ubuntu:18.04

ADD tracker/requirements.txt /tmp/requirements.txt

# roundup doesn't allow running as root
RUN useradd -ms /bin/bash tracker && \
    echo "tracker ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN apt-get update && \
    apt-get install -y \
        python-dev \
        python-psycopg2 \
        python-pip \
        libffi-dev \
        libssl-dev \
        curl && \
    rm -rf /var/lib/apt/lists/* && \
    # install python requirements
    pip install -r /tmp/requirements.txt

USER tracker