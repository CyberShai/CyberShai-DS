from fastapi import Depends, FastAPI


app = FastAPI(title="CyberShai API",
    description="REST API which returns statistics for CyberShai project.",
    version="0.1",)


# @app.get("/", tags=["API Root"])
# def root():
#     return {"message": "Hello World"}
# app.include_router(
#     sentiment.router,
#     prefix="/api/v1",
#     tags=["CyberShai Endpoints"],
#     responses={404: {"description": "Not found"}},
# )


@app.get("/", tags=["API Root"])
def welcome():
    return {"message": "Welcome to CyberShai API"}

@app.get("/colocations-by-cohort", tags=["API statistics"])
def colocations_by_cohort():
    return {"cohort_1": "Pocos",
            "cohort_2": "Más",
            "cohort_3": "Bastantes",
            "cohort_4": "Muchos",
            "cohort_5": "Muchísimos"}

@app.get("/students-can-pay", tags=["API statistics"])
def colocations_by_cohort():
    return {"cohort_1": "1000",
            "cohort_2": "10000",
            "cohort_3": "100000",
            "cohort_4": "1000000",
            "cohort_5": "10000000"}

@app.get("/students-report", tags=["API statistics"])
def colocations_by_cohort():
    return {"job_title": "trabajo soñado",
            "company": "FANG",
            "starting_date": "01/02/2021",
            "salary_increment_porcent": "100%",
            }

@app.get("/global-colocations", tags=["API statistics"])
def colocations_by_cohort():
    return {"cohort_1": "4",
            "cohort_2": "5",
            "cohort_3": "6",
            "cohort_4": "7",
            "cohort_5": "8",
            "global": "47"}