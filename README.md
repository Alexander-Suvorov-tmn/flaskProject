# Приложение для отслеживания google документа и внесения данных в БД postgresql, а так же рассылки сообщений в ТГ бота, если срок поставки просрочен
## СТЕК:
    * linux
    * python
    * flask
    * sqlalchemy
    * postgresql
    * python-telegram-bot
    * marshmello
1. Создать БД:
```angular2html
sudo -u postgres psql
CREATE DATABASE datatest;
```
создать пользователя с правами:
```angular2html
CREATE USER testt WITH password 'testt';
GRANT ALL ON DATABASE test_database TO testt;
```
2. Скопировать репозиторий при помощи команды ```git clone https://github.com/Alexander-Suvorov-tmn/flaskProject.git```
3. перейти в рабочию директорию, выполнив команду ``` cd flaskProject```
4. В корне проекта создать файл ```.env``` в котором записать:
```
DB="postgresql+psycopg2://testt:testt@localhost:5432/datatest"
SHEET_ID="1O_NkvV7nfA1dxexgQBIMUxlCl1Ogr4-mbDZFR_p7FlE"
TG_ID='5392050846:AAHZX0sAYIpScJz_l5WieJEdD3-p_9m-YAo'
```

5. Установить все необходимые зависимости командой ```pip install -r requirements.txt```
4. перейти в директорию приложения командом ```cd test_app```

5. Инициализируйте Alembic командой ```alembic init migrations```
   
6. Для проведения миграций необходимо:
- в файле ```alembic.ini``` указать путь к БД, напрмер ```sqlalchemy.url = postgresql+psycopg2://testt:testt@localhost:5432/datatest```
- в папке ```migration``` в файле ```env.py```  изменить 
```
from database.models import OrderData
from database.connected import Base
target_metadata = Base.metadata
```
7. Провести первую миграцию командой ```alembic revision --autogenerate -m "init"```
8. Применить миграцию командой ```alembic upgrade head"```
9. вернитесь в рабочию директорию, выполнив команду ``` cd ..```
10. Запустите приложение командой ```python run.py```

11. приложение запускается по адресу: ```http://127.0.0.1:5000``` на этом адресе выводятся данные из БД в формате json

12. Телеграм бот:
* найдите в телеграмме бота по имени ```@ex_suv_bot```
* после запуска приложения введите в телеграмме (в боте) команду ```/start```
* через непродолжительное время будут приходить уведомления о просроченных поставках
13. ссылка на google документ ```https://docs.google.com/spreadsheets/d/1O_NkvV7nfA1dxexgQBIMUxlCl1Ogr4-mbDZFR_p7FlE/edit?usp=sharing```
* доступ к документу у всех, у кого есть ссылка