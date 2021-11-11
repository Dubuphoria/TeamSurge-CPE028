#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp ip_flask.py tempdir/.
cp ip_api.py tempdir/.
cp requirements.txt tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.


echo "FROM python" > tempdir/Dockerfile
echo "COPY ./requirements.txt /home/myapp/" >> tempdir/Dockerfile
echo "RUN pip install -r /home/myapp/requirements.txt" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY ./ip_flask.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY ./ip_api.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/ip_flask.py" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/test_ip_api.py" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/test_ip_flask.py" >> tempdir/Dockerfile
cd tempdir
docker build -t apiapplication .
docker run -t -d -p 5050:5050 --name apprun apiapplication
docker ps -a