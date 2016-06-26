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
 
RUN mkdir -p codebase && cd codebase
WORKDIR codebase
COPY test.mov .
COPY main.sh .
COPY convert.py .
RUN echo 'source /codebase/main.sh' >> /root/.bashrc 
RUN git clone https://github.com/senko/python-video-converter.git
WORKDIR python-video-converter
RUN python setup.py install
WORKDIR test 
RUN ./install-ffmpeg.sh
WORKDIR /codebase
#ENTRYPOINT ["convertma /codebase/test.mov"]
RUN /bin/bash -c "source /root/.bashrc && convertma /codebase/test.mov"
#RUN convertma /codebase/test.mov
