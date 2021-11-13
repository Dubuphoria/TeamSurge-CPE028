#!/bin/bash

mkdir tempdir               # Create temdir directory
mkdir tempdir/templates     # Create templates directory inside tempdir
mkdir tempdir/static        # Create static directory inside tempdir

cp ip_flask.py tempdir/.    # Copy ip_flask.py in tempdir
cp ip_api.py tempdir/.      # Copy ip_api.py in tempdir
cp test_ip_api.py tempdir/. # Copy test_ip_api.py in tempdir
cp test_ip_flask.py tempdir/.   # Copy test_ip_flask.py in tempdir
cp requirements.txt tempdir/.   # Copy requirements.txt in tempdir
cp -r templates/* tempdir/templates/.   # Copy all contents of templates in tempdir
cp -r static/* tempdir/static/.     # Copy all contents of static in tempdir

# Creating Dockerfile
echo "FROM python" > tempdir/Dockerfile
echo "COPY ./requirements.txt /home/myapp/" >> tempdir/Dockerfile               # Copy requirements.txt
echo "RUN pip install -r /home/myapp/requirements.txt" >> tempdir/Dockerfile    # Install packages listed in requirements.txt
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile                  # Copy static directory
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile            # Copy templates directory
echo "COPY ./ip_flask.py /home/myapp/" >> tempdir/Dockerfile                    # Copy ip_flask.py
echo "COPY ./ip_api.py /home/myapp/" >> tempdir/Dockerfile                      # Copy ip_api.py
echo "COPY ./test_ip_api.py /home/myapp/" >> tempdir/Dockerfile                 # Copy test_ip_api.py
echo "COPY ./test_ip_flask.py /home/myapp/" >> tempdir/Dockerfile               # Copy test_ip_flask.py
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/test_ip_api.py" >> tempdir/Dockerfile             # Run test_ip_api.py
echo "CMD python3 /home/myapp/test_ip_flask.py" >> tempdir/Dockerfile           # Run test_ip_flask.py
echo "CMD python3 /home/myapp/ip_flask.py" >> tempdir/Dockerfile                # Run ip_flask.py
cd tempdir
docker build -t apiapplication .
docker run -t -d -p 5050:5050 --name apprun apiapplication
docker ps -a