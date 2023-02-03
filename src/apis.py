import requests


def get_commune(code: int) -> dict:

    url = f'https://geo.api.gouv.fr/communes/{code}?fields=codesPostaux,population&format=json&geometry=centre'
    response = requests.get(url)
    if response.status_code != 200:
        return {}

    data = response.json()
    code_postal = data['codesPostaux'][0]
    population = data['population']

    return {"code_postal": code_postal, "population": population}


def get_commune_note(code: int) -> dict:
    fake_url = 'https://note.de.maville?code_postal='

    url = fake_url + code
    # fake_response = requests.get(url)

    #  Since we don't have an api for note, I will define a note based on the first digit of the code insee of the city

    return str(code)[-1]


def get_mean_rent_amount_per_department(dep: int, surface: int, max_rent: int) -> list:
    url = f'https://immobilier-carte-interactive.vercel.app/api/recupData?dep={dep}'
    output = []
    field = 'prixLocationMoyenPourAppartement' + str(surface) + 'M2'  # ex: prixLocationAppartementPour50M2

    response = requests.get(url)
    status_code = response.status_code
    if status_code != 200:
        raise Exception('Server problem')

    data = response.json()['features']
    for item in data:
        item = item['properties']
        code = item['code']
        note = get_commune_note(code=code)
        res = get_commune(code=code)
        code_postal = res['code_postal']
        population = res['population']
        element = {
            field: item['prixM2Location_appartement'] * surface,
            "note": note,
            'nom': item['nom'],
            'code_postal': code_postal,
            'population': population
        }
        output.append(element)

    return output
