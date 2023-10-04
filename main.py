import psycopg2
import csv
from CSVFileHandler import CSVFileHandler
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

emp_info = emp.get_employer_info('Бизнес-Азимут')
emp1_info = emp1.get_employer_info('РусЭкспресс')
emp2_info = emp2.get_employer_info('ООО АВ Софт')
emp3_info = emp3.get_employer_info('ООО Космос Про Медиа')
emp4_info = emp4.get_employer_info('ООО Компания Дилявер')
emp5_info = emp5.get_employer_info('IT-People.ru')
emp6_info = emp6.get_employer_info('ООО ЛингуаЛео')
emp7_info = emp7.get_employer_info('Герцен')
emp8_info = emp8.get_employer_info('ООО Варити+')
emp9_info = emp9.get_employer_info('АО Рут Код')

emp_csv = CSVFileHandler("csv_employer.csv").add_employer(emp)
emp1_csv = CSVFileHandler("csv_employer.csv").add_employer(emp1)
emp2_csv = CSVFileHandler("csv_employer.csv").add_employer(emp2)
emp3_csv = CSVFileHandler("csv_employer.csv").add_employer(emp3)
emp4_csv = CSVFileHandler("csv_employer.csv").add_employer(emp4)
emp5_csv = CSVFileHandler("csv_employer.csv").add_employer(emp5)
emp6_csv = CSVFileHandler("csv_employer.csv").add_employer(emp6)
emp7_csv = CSVFileHandler("csv_employer.csv").add_employer(emp7)
emp8_csv = CSVFileHandler("csv_employer.csv").add_employer(emp8)
emp9_csv = CSVFileHandler("csv_employer.csv").add_employer(emp9)

emp_vacs = Vacancies().search_vacancies(emp.employer_id)
emp1_vacs = Vacancies().search_vacancies(emp1.employer_id)
emp2_vacs = Vacancies().search_vacancies(emp2.employer_id)
emp3_vacs = Vacancies().search_vacancies(emp3.employer_id)
emp4_vacs = Vacancies().search_vacancies(emp4.employer_id)
emp5_vacs = Vacancies().search_vacancies(emp5.employer_id)
emp6_vacs = Vacancies().search_vacancies(emp6.employer_id)
emp7_vacs = Vacancies().search_vacancies(emp7.employer_id)
emp8_vacs = Vacancies().search_vacancies(emp8.employer_id)
emp9_vacs = Vacancies().search_vacancies(emp9.employer_id)

emp_vacs_csv = CSVFileHandler("csv_vacancies.csv").add_vacancies(emp_vacs)
emp1_vacs_csv = CSVFileHandler("csv_vacancies.csv").add_vacancies(emp1_vacs)
emp2_vacs_csv = CSVFileHandler("csv_vacancies.csv").add_vacancies(emp2_vacs)
emp3_vacs_csv = CSVFileHandler("csv_vacancies.csv").add_vacancies(emp3_vacs)
emp4_vacs_csv = CSVFileHandler("csv_vacancies.csv").add_vacancies(emp4_vacs)
emp5_vacs_csv = CSVFileHandler("csv_vacancies.csv").add_vacancies(emp5_vacs)
emp6_vacs_csv = CSVFileHandler("csv_vacancies.csv").add_vacancies(emp6_vacs)
emp7_vacs_csv = CSVFileHandler("csv_vacancies.csv").add_vacancies(emp7_vacs)
emp8_vacs_csv = CSVFileHandler("csv_vacancies.csv").add_vacancies(emp8_vacs)
emp9_vacs_csv = CSVFileHandler("csv_vacancies.csv").add_vacancies(emp9_vacs)


def main():
    conn = psycopg2.connect(host='localhost', database='coarse_work_5', user='postgres', password='Leha210900')
    try:
        with conn:
            with conn.cursor() as cur:
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
