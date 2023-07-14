from lxml import etree
import requests
from response import Response


class MeasoftApi:
    API_URL = "https://home.courierexe.ru/api/"

    def __init__(self, login, password, extracode):
        self.login = login
        self.password = password
        self.extracode = extracode
        self.http_client = requests.Session()

    def request(self, xml, with_auth=True):
        if with_auth:
            auth = xml.find("auth")
            auth.set("login", self.login)
            auth.set("pass", self.password)
            auth.set("extra", self.extracode)

        try:
            response = self.http_client.post(
                self.API_URL,
                data=etree.tostring(xml, encoding="utf-8"),
                headers={"Content-Type": "text/xml; charset=UTF8"},
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return Response(False, None, str(e))

        try:
            xml = etree.fromstring(response.content)
        except etree.XMLSyntaxError:
            return Response(False, None, "Неверный формат полученных данных")

        error = int(xml.get("error", 0))
        if error:
            return Response(False, xml, self.get_error_message(error, xml.text))

        return Response(True, xml)

    def get_error_message(self, code, alternative):
        errors = {
            0: "OK",
            1: "Неверный xml",
            2: "Широта не указана",
            3: "Долгота не указана",
            4: "Дата и время запроса не указаны",
            5: "Точность не указана",
            6: "Идентификатор телефона не указан",
            7: "Идентификатор телефона не найден",
            8: "Неверная широта",
            9: "Неверная долгота",
            10: "Неверная точность",
            11: "Заказы не найдены",
            12: "Неверные дата и время запроса",
            13: "Ошибка mysql",
            14: "Неизвестная функция",
            15: "Тариф не найден",
            18: "Город отправления не указан",
            19: "Город назначения не указан",
            20: "Неверная масса",
            21: "Город отправления не найден",
            22: "Город назначения не найден",
            23: "Масса не указана",
            24: "Логин не указан",
            25: "Ошибка авторизации",
            26: "Логин уже существует",
            27: "Клиент уже существует",
            28: "Адрес не указан",
            29: "Более не поддерживается",
            30: "Настройка sip не выполнена",
            31: "Телефон не указан",
            32: "Телефон курьера не указан",
            33: "Ошибка соединения",
            34: "Неверный номер",
            35: "Неверный номер",
            36: "Ошибка определения тарифа",
            37: "Ошибка определения тарифа",
            38: "Тариф не найден",
            39: "Тариф не найден",
        }
        return errors.get(code, alternative)
