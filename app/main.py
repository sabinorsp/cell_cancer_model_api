from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from model.model import predict
import numpy as np
 

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/submit")
def submit_form(
    texture_mean: float = Form(18.66),
    smoothness_mean: float = Form(0.1158),
    compactness_mean: float = Form(0.1231),
    concavity_mean: float = Form(0.1226),
    concave_points_mean: float = Form(0.0734),
    symmetry_mean: float = Form(0.2128),
    fractal_dimension_mean: float = Form(0.06777),
    texture_se: float = Form(0.8937),
    perimeter_se: float = Form(1.897),
    area_se: float = Form(24.25),
    smoothness_se: float = Form(0.006532),
    compactness_se: float = Form(0.02336),
    concavity_se: float = Form(0.02905),
    concave_points_se: float = Form(0.01215),
    symmetry_se: float = Form(0.01743),
    fractal_dimension_se: float = Form(0.003643),
    texture_worst: float = Form(27.95),
    area_worst: float = Form(759.4),
    smoothness_worst: float = Form(0.1786),
    compactness_worst: float = Form(0.4166),
    concavity_worst: float = Form(0.5006),
    concave_points_worst: float = Form(0.2088),
    symmetry_worst: float = Form(0.39),
    fractal_dimension_worst: float = Form(0.1179),
):
    data = np.array([
            texture_mean,
            smoothness_mean,
            compactness_mean,
            concavity_mean,
            concave_points_mean,
            symmetry_mean,
            fractal_dimension_mean,
            texture_se,
            perimeter_se,
            area_se,
            smoothness_se,
            compactness_se,
            concavity_se,
            concave_points_se,
            symmetry_se,
            fractal_dimension_se,
            texture_worst,
            area_worst,
            smoothness_worst,
            compactness_worst,
            concavity_worst,
            concave_points_worst,
            symmetry_worst,
            fractal_dimension_worst
            ]).reshape(1,-1)
    return {"Predict": predict(data)}


@app.get("/")
def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
