## Installation


### 0: Clone
```bash
git clone https://github.com/FlorianMehnert/flowerbed.git
cd flowerbed
```

### 1a: Docker
- build and start the docker container
```bash
docker build -t flowerbed .
docker run -p 8000:8000 flowerbed
```

### 1b: Local Install
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

