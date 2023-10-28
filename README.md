# Passo a passo

#### Rode o docker compose
```bash
docker-compose up
```

#### Configure a API
```bash
python install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```