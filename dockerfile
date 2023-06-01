FROM python:3

ADD 6.py .

RUN pip install requests matplotlib
RUN pip install requests numpy

CMD [ "python", "./6.py" ]