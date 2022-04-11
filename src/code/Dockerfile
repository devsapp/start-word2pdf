
FROM python:3.7.11-slim-stretch

RUN apt-get update && apt-get install -y \
  wget \
  unzip\
  fonts-wqy-zenhei \
  fonts-wqy-microhei \
  libglib2.0-dev \
  python3-uno \
  libreoffice \
  --no-install-recommends && rm -r /var/lib/apt/lists/*

RUN mkdir -p /usr/share/man/man1
RUN apt-get update && apt-get install -y \
  openjdk-8-jdk \
  imagemagick \
  --no-install-recommends && rm -r /var/lib/apt/lists/*

RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install oss2 -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN chmod 777 /tmp
RUN chmod 755 /usr/bin/soffice

# Create app directory
WORKDIR /code

COPY . .

EXPOSE 9000

ENTRYPOINT [ "python", "-u", "app.py" ]