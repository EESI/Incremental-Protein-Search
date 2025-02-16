# select base image
FROM ubuntu:20.04

# packages setting
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    bash \
    && rm -rf /var/lib/apt/lists/*

# set Python3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# set work directory
WORKDIR /app

# clone GitHub repo
#RUN git clone https://github.com/ece303/Incremental-Protein-Search.git

# copy current git repo
COPY . /app/

# move to working directory -> already in workdir
#WORKDIR /app/Incremental-Protein-Search

# install requirements.txt
RUN pip3 install -r requirements.txt

# set chmod +x
RUN chmod +x run_merge.sh

# set run command
ENTRYPOINT ["./run_merge.sh"]
