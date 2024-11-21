Для комфортной разработки поставьте virtualenv:
```sh
python -m venv venv/
./venv/bin/activate
# Если пользуетесь VSCode и уже выбрали интерпретатор, терминал в редакторе будет уже настроен на virtualenv

# внутри venv
pip install -r requirements.txt
```
чтобы запустить это, вам нужен Docker Desktop и если он есть, то:
```sh
docker compose up
```
если нет, внутри virtual environment
```
fastapi dev ./service/main.py
```

для тестирования, запускаем команду в virtualenv:
```sh
pytest
```
