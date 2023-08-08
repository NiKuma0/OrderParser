from http import HTTPStatus
from typing import Generator

import pytest  # type: ignore
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

from .services import Parser, ParserCSVBytes

pytestmark = [pytest.mark.django_db]
DEALS_CONTENT: str = """customer,item,total,quantity,date
bellwether,Цаворит,612,6,2018-12-14 08:29:52.506166
resplendent,Сапфир,8502,6,2018-12-14 14:43:45.883282
buckaroo,Рубин,342,2,2018-12-15 15:00:59.858739
zygote4id3n,Яшма,264,3,2018-12-16 00:01:13.013713
nambypamby,Берилл,660,5,2018-12-16 01:58:57.047891
bellwether,Опал,3136,8,2018-12-16 03:35:54.925057
turophile,Изумруд,2228,2,2018-12-17 14:11:50.787893
nambypamby,Кварц,75,1,2018-12-18 11:41:47.643247
viperliamk0125,Спессартин,124,2,2018-12-18 19:43:49.082618"""
DEALS_DATA: list[dict[str, str]] = [
    {
        "customer": "bellwether",
        "item": "Цаворит",
        "total": "612",
        "quantity": "6",
        "date": "2018-12-14 08:29:52.506166",
    },
    {
        "customer": "resplendent",
        "item": "Сапфир",
        "total": "8502",
        "quantity": "6",
        "date": "2018-12-14 14:43:45.883282",
    },
    {"customer": "buckaroo", "item": "Рубин", "total": "342", "quantity": "2", "date": "2018-12-15 15:00:59.858739"},
    {"customer": "zygote4id3n", "item": "Яшма", "total": "264", "quantity": "3", "date": "2018-12-16 00:01:13.013713"},
    {"customer": "nambypamby", "item": "Берилл", "total": "660", "quantity": "5", "date": "2018-12-16 01:58:57.047891"},
    {"customer": "bellwether", "item": "Опал", "total": "3136", "quantity": "8", "date": "2018-12-16 03:35:54.925057"},
    {
        "customer": "turophile",
        "item": "Изумруд",
        "total": "2228",
        "quantity": "2",
        "date": "2018-12-17 14:11:50.787893",
    },
    {"customer": "nambypamby", "item": "Кварц", "total": "75", "quantity": "1", "date": "2018-12-18 11:41:47.643247"},
    {
        "customer": "viperliamk0125",
        "item": "Спессартин",
        "total": "124",
        "quantity": "2",
        "date": "2018-12-18 19:43:49.082618",
    },
]


@pytest.fixture(autouse=True, name="client")
def _client() -> Generator[APIClient, None, None]:
    api_client = APIClient(format="json")
    yield api_client
    api_client.logout()


@pytest.fixture(autouse=True, name="file")
def _file() -> SimpleUploadedFile:
    return SimpleUploadedFile("order.csv", bytes(DEALS_CONTENT, "UTF-8"))


@pytest.fixture(autouse=True, name="empty_file")
def _empty_file() -> SimpleUploadedFile:
    return SimpleUploadedFile("order.csv", content=None)


@pytest.fixture(autouse=True, name="csv_parser")
def _csv_parser() -> ParserCSVBytes:
    return ParserCSVBytes()


def test_csv_parser(csv_parser: Parser, file: SimpleUploadedFile) -> None:
    if not file.file:
        raise
    assert list(csv_parser.get_deals_data(file.file)) == DEALS_DATA


def test_create_deals(client: APIClient, file: SimpleUploadedFile) -> None:
    data = {
        "deals": file,
    }
    response = client.post("/api/deals/", data=data)
    assert response.status_code == HTTPStatus.CREATED
    assert response.data == {}


def test_create_deals_with_empty_file(client: APIClient, empty_file: SimpleUploadedFile) -> None:
    data = {
        "deals": empty_file,
    }
    response = client.post("/api/deals/", data=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_customer(client: APIClient) -> None:
    response = client.get("/api/customer/")
    assert response.status_code == HTTPStatus.OK
    assert response.data == []


def test_create_deals_and_customer(client: APIClient, file: SimpleUploadedFile) -> None:
    data = {
        "deals": file,
    }
    response = client.post("/api/deals/", data=data)
    assert response.status_code == HTTPStatus.CREATED
    assert response.data == {}

    response = client.get("/api/customer/")
    assert response.status_code == HTTPStatus.OK
    assert len(response.data) == 5
