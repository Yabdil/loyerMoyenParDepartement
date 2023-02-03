import requests

from fastapi import FastAPI


from .apis import get_mean_rent_amount_per_department

app = FastAPI()


@app.get("/citiesWithMeanRentPerDepartement/{dep}")
def get_cities_with_informations(dep: int, surface: int, max_rent: int):
    try:
        data = get_mean_rent_amount_per_department(dep=dep, surface=surface, max_rent=max_rent)
    except:
        return {"A problem occur, try later"}, 400

    return data, 200
