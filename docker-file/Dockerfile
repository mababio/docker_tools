FROM python
RUN apt-get update && apt-get install -y \
    git \
    libxml2-dev \
    build-essential \
    make \
    gcc \
    python-dev \
    locales \
    apt-utils \
    vim \
    man 

RUN cd 
RUN mkdir -p codebase && cd codebase
COPY test.mov .
RUN git clone https://github.com/senko/python-video-converter.git
