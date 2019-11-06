FROM python:3

RUN pip install pymongo

RUN pip install --upgrade pip

ADD insert_number.py .

CMD [ "python", "insert_number.py" ]

