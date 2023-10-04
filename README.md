Проект по БД postgresql

Подготовка:
Перед запуском программы необходимо создать таблицы employers и vacancies с помощью следующего sql кода в pgAdmin 

CREATE DATABASE coarse_work_5;

CREATE TABLE employers
(
    employer_id int PRIMARY KEY,
    employer_name varchar(100) NOT NULL,
    open_vacancies int
);

CREATE TABLE vacancies
(
	employer_id int REFERENCES employers(employer_id) NOT NULL,
	vacancy_name text,
	salary int,
	city varchar (100),
	url text
)

Также необходимо в переменной con в файле main.py функции main и в файле DBManager.py в классе DBManager 
изменить значения параметров подключения под свои

Использование:
Необходимо запустить файл main.py, таблицы заполнятся данными о работодателях и вакансиях, 
затем можно пользоваться методами класса DBManager для получения данных из таблиц.