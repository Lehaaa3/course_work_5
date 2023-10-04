import requests


class Vacancies:
    """Класс для получения вакансий от определенного работодателя с помощью HeadHunter API"""

    url: str = 'https://api.hh.ru/vacancies'

    def __init__(self, url: str = url):
        """
        Инициализация класса Vacancies.

        :param url: URL для запросов к HeadHunter API.
        """
        self.url = url
        self.employer_id = None

    def search_vacancies(self, employer_id: str):
        """
        Поиск вакансий на HeadHunter API.

        :param employer_id: ID Компании
        :return: Список найденных вакансий.
        """
        params = {
            'per_page': 100,
            'only_with_salary': True,
            'employer_id': employer_id
        }

        response = requests.get(url=self.url, params=params)
        response_json = response.json()

        return response_json.get("items", [])
