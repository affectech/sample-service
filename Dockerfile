FROM python:3.13-alpine

WORKDIR /service/sample

COPY . .

RUN chmod +x ./run

# кэширование pip-зависимостей
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

CMD [ "./run" ]
