# Passo a passo

#### Rode o docker compose
```bash
docker-compose up
```

#### Crie um ambiente virtual
```bash
python -m venv .venv
.venv/Scripts/activate
```

#### Configure a API
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```