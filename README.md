Проект по БД postgresql

Подготовка:
1. Перед запуском программы необходимо создать базу данных в pgAdmin и назвать ее coarse_work_5 (CREATE DATABASE coarse_work_5;)

2. Установить зависимости из файла pyproject.toml

3. Также необходимо в переменной con в файле main.py функции main и в файле DBManager.py в классе DBManager 
заменить звездочки на свой пароль в параметре password
conn = psycopg2.connect(host='localhost', database='coarse_work_7', user='postgres', password='***')

Использование:
Необходимо запустить файл main.py, таблицы заполнятся данными о работодателях и вакансиях, 
затем можно пользоваться методами класса DBManager для получения данных из таблиц.