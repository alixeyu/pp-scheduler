FROM python:3.10-slim

RUN groupadd -r webuser && useradd --no-log-init -r -m -g webuser webuser

USER webuser

COPY ./requirements /app/

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./ ./

CMD [ "python", "-m", "uvicorn", "main:app", "--reload" ]
