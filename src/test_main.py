import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_cities_with_informations_fail():
    # We make a test with a nonexistent code dep=96
    dep, surface, max_rent = 96, 55, 20
    url = f'/citiesWithMeanRentPerDepartement/{dep}?surface={surface}&max_rent={max_rent}'
    response = client.get(url)
    assert response.status_code == 400


def get_cities_with_informations_success():
    dep, surface, max_rent = 93, 55, 20
    url = f'/citiesWithMeanRentPerDepartement/{dep}?surface={surface}&max_rent={max_rent}'
    response = client.get(url)
    assert response.status_code == 200


