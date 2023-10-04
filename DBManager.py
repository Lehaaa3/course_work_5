import psycopg2


class DBManager:
    """Класс для получения информации о работодателях и вакансиях с помощью библиотеки psycopg2"""

    def __init__(self):
        """Инициализация класса DBManager"""
        self.conn = psycopg2.connect(host='localhost', database='coarse_work_5', user='postgres', password='Leha210900')

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        companies_and_vacancies_list = []
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM employers")
                rows = cur.fetchall()
                for row in rows:
                    companies_and_vacancies_list.append([f"Компания {row[1]} - {2} открытых вакансии"])
        return companies_and_vacancies_list

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        all_vacancies = []
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM employers JOIN vacancies USING(employer_id) ")
                rows = cur.fetchall()
                for row in rows:
                    all_vacancies.append(
                        [f"Компания - {row[1]}, Вакансия - {row[3]}, Зарлпата - {row[4]}, url - {row[5]}"])
        return all_vacancies

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям."""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT AVG(salary) FROM vacancies")
                avg_salary = cur.fetchall()
                return avg_salary[0][0]

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies)")
                vacancies_with_higher_salary = cur.fetchall()
                return vacancies_with_higher_salary

    def get_vacancies_with_keyword(self):
        """"получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM vacancies WHERE vacancy_name LIKE '%Python%'")
                vacancies_with_keyword = cur.fetchall()
                return vacancies_with_keyword
