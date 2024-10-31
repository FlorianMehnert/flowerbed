## Installation


### 0: Clone
```bash
git clone https://github.com/FlorianMehnert/flowerbed.git
cd flowerbed
```

### 1a: Docker-compose
- build and start the docker container
```bash
docker-compose up --build
docker-compose down
```

### 1b: Local install
- setup virtualenv
```bash
python3 -m venv venv-flowerbed
source venv-flowerbed/bin/activate
pip install -r requirements.txt
```
- setup django project and start
```bash
python manage.py migrate
python manage.py runserver
```

### 2a:
- create a superuser for the django application
```bash
docker-compose exec web python manage.py createsuperuser
```
