import requests

from fastapi import FastAPI

from .apis import get_mean_rent_amount_per_department

app = FastAPI()

cached_data = {}


@app.get("/citiesWithMeanRentPerDepartement/{dep}")
def get_cities_with_informations(dep: int, surface: int, max_rent: int):
    code_dep = 'dep-' + str(dep)
    if code_dep not in cached_data:
        try:
            data = get_mean_rent_amount_per_department(dep=dep, surface=surface, max_rent=max_rent)
        except:
            return {"A problem occur, try later"}, 400
        #  We will cache data
        cached_data[code_dep] = data

    data = cached_data[code_dep]

    return data, 200
