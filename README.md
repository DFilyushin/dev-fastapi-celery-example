# dev-fastapi-celery-example

## Запуск

```python
uvicorn main:app --host 0.0.0.0 --reload

celery -A worker.celery worker --loglevel=info --logfile=logs/celery.log

celery -A worker.celery worker --loglevel=info --logfile=logs/celery.log -P eventlet # запуск на Windows

celery -A worker.celery flower
```


Запуск на Windows потребует установки `eventlet`.

```python
poetry add eventlet
```

## Мониторинг

```
http://localhost:8000/ - сервис

http://localhost:5555/ - Flower
```