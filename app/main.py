from fastapi import Depends, FastAPI


app = FastAPI(title="CyberShai API",
    description="REST API which returns statistics for CyberShai project.",
    version="0.1",)


@app.get("/")
async def welcome():
    return {"message": "Welcome to CyberShai API"}

@app.get("/colocations-by-cohort")
async def colocations_by_cohort():
    return {"cohort_1": "Pocos",
            "cohort_2": "Más",
            "cohort_3": "Bastantes",
            "cohort_4": "Muchos",
            "cohort_5": "Muchísimos"}

@app.get("/students-can-pay")
async def students_can_pay():
    return {"cohort_1": "1000",
            "cohort_2": "10000",
            "cohort_3": "100000",
            "cohort_4": "1000000",
            "cohort_5": "10000000"}

@app.get("/students-report")
async def students_report():
    return {"job_title": "trabajo soñado",
            "company": "FANG",
            "starting_date": "01/02/2021",
            "salary_increment_porcent": "100%",
            }

@app.get("/global-colocations")
async def global_colocations():
    return {"cohort_1": "4",
            "cohort_2": "5",
            "cohort_3": "6",
            "cohort_4": "7",
            "cohort_5": "8",
            "global": "47"}