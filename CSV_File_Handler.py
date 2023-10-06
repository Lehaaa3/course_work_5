from Employer import Employer
import csv


class CSVFileHandler:
    """Класс для обработки CSV файлов"""

    def __init__(self, file_path: str):
        """
        Инициализация объекта CSVFileHandler.

        :param file_path: Путь к CSV файлу.
        """
        self.file_path = file_path

    def add_employer(self, employer: Employer) -> None:
        """
        Добавляет информацию о работодателе в CSV файл.

        :param employer: Работодатель для добавления.
        """
        with open(self.file_path, "a", encoding="windows-1251", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                employer.employer_id,
                employer.employer_name,
                employer.open_vacancies
            ])

    def add_vacancies(self, vacancies: list):
        """
        Добавляет информацию о вакансиях от работодателя в CSV файл.

        :param vacancies: Список вакансий.
        """
        for vac in vacancies:
            with open(self.file_path, "a", encoding="windows-1251", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    vac['employer']['id'],
                    vac['name'],
                    vac['salary']['from'] if vac['salary']['from'] is not None else vac['salary']['to'],
                    vac['area']['name'],
                    vac['alternate_url']
                ])
