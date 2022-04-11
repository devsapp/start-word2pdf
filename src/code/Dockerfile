
FROM rsonghuster/libreoffice-stretch

RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install oss2 -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN chmod 777 /tmp

# Create app directory
WORKDIR /code

COPY . .

EXPOSE 9000

ENTRYPOINT [ "python", "-u", "app.py" ]