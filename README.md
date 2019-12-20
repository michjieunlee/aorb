# Aorb

## Backend

```json
# create virtual env
virtualenv -p python3 env

# activate env
source env/bin/activate

# install packages
pip install -r requirements.txt

# db migrate
cd server && python manage.py migrate
python server/manage.py migrate

# run server
cd server && python manage.py runserver
python server/manage.py runserver
```

## Frontend

```json
# Installation
npm i

# Run
npm start

# build
npm run build

# Available scripts
https://create-react-app.dev/docs/available-scripts
```
