FROM python
COPY ./requirements.txt /home/myapp/
RUN pip install -r /home/myapp/requirements.txt
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY ./ip_flask.py /home/myapp/
COPY ./ip_api.py /home/myapp/
COPY ./test_ip_api.py /home/myapp/
COPY ./test_ip_flask.py /home/myapp/
EXPOSE 5050
CMD python3 /home/myapp/test_ip_api.py
CMD python3 /home/myapp/test_ip_flask.py
CMD python3 /home/myapp/ip_flask.py
