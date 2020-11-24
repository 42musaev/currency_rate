# Currency rate

## Web-interface for receiving the currency rate from cbr.ru with the possibility of saving in the database


##### create a virtual environment
```sh
python3 -m venv venv
```
##### activate virtual environment
```sh
source venv/bin/activate
```
##### install dependencies
```sh
pip install -r requirements.txt
```
##### create a .env file and add the following variables to it
```sh
touch .env

SQLALCHEMY_DATABASE_URI="[URI_POSTGRES]"
SECRET_KEY="[EXAMPLE_SECRET_KEY]"
```
##### migrate
```sh
python3 manage.py db upgrade
```
##### run
```sh
python3 runner.py
```

add your currencies via admin-panel http://localhost:5000/admin/currency/

codes can be found <a href="http://www.cbr.ru/scripts/XML_val.asp?d=0">here</a>
