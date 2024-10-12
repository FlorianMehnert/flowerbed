## Installation

### Clone
```bash
git clone https://github.com/FlorianMehnert/flowerbed.git
cd flowerbed
```

### Pure Python
- setup virtualenv
```bash
python3 -m venv venv-flowerbed
source venv-flowerbed/bin/activate
pip install -r requirements.txt
```
- setup django project and start
```bash
python manage.py tailwind build
python manage.py migrate
python manage.py runserver
```

### Docker
- build and start the docker container
```bash
docker build -t flowerbed .
docker run -p 8000:8000 -v $(pwd):/app flowerbed
```
- stop the docker container
