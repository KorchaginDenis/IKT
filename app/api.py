from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome to the first FastApi"}


@app.get("/items")
def read_item():
    return {
        "id": 1,
        "Name": "Denis",
        "Fam": "Korchagin",
        "Group": "035"
            }