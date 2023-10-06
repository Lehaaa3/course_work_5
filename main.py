import psycopg2
import csv
from CSV_File_Handler import CSVFileHandler
from Employer import Employer
from Vacancies import Vacancies

emp = Employer()
emp1 = Employer()
emp2 = Employer()
emp3 = Employer()
emp4 = Employer()
emp5 = Employer()
emp6 = Employer()
emp7 = Employer()
emp8 = Employer()
emp9 = Employer()

employers = [emp, emp1, emp3, emp4, emp5, emp6, emp7, emp8, emp9]
companies = ['Бизнес-Азимут', 'РусЭкспресс', 'ООО АВ Софт', 'ООО Космос Про Медиа', 'ООО Компания Дилявер',
             'IT-People.ru', 'ООО ЛингуаЛео', 'Герцен', 'ООО Варити+', 'АО Рут Код']

company_number = 0
for e in employers:
    e.get_employer_info(companies[company_number])
    company_number += 1
    CSVFileHandler("csv_employer.csv").add_employer(e)
    emp_vacs = Vacancies().search_vacancies(e.employer_id)
    CSVFileHandler("csv_vacancies.csv").add_vacancies(emp_vacs)


def main():
    conn = psycopg2.connect(host='localhost', database='coarse_work_5', user='postgres', password='***')
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("CREATE TABLE employers(employer_id int PRIMARY KEY, employer_name varchar(100) NOT NULL, "
                            "open_vacancies int);")
                cur.execute(
                    "CREATE TABLE vacancies(employer_id int REFERENCES employers("
                    "employer_id) NOT NULL, vacancy_name "
                    "text, salary int, city varchar (100), url text)")
                with open('csv_employer.csv') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        cur.execute("INSERT INTO employers VALUES (%s, %s, %s)", (
                            row['employer_id'], row['employer_name'], row['open_vacancies']))
                with open('csv_vacancies.csv') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        cur.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)", (row['employer_id'],
                                                                                          row['vacancy_name'],
                                                                                          row['salary'], row['city'],
                                                                                          row['url']))
    finally:
        conn.close()


main()
