from fastapi import FastAPI

app = FastAPI(title="Currency Converter API")


@app.get("/")
def root():
    return {"message": "API funcionando"}
