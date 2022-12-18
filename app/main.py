import uvicorn
import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"data": datetime.datetime.now()}

@app.get("/items")
def read_item():
    return {
        "id": 1,
        "Name": "Denis",
        "Fam": "Korchagin",
        "Group": "035"
            }

#http://127.0.0.1:8080 и http://127.0.0.1:8080/items
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080, log_level='info')