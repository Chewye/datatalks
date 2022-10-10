FROM python:3.9.12-slim

RUN pip install pipenv

WORKDIR /app                                                                

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system

COPY ["hw.py", "model1.bin", "dv.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "hw:app"]