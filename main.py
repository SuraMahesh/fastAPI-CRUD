from fastapi import FastAPI

app = FastAPI()

fakeDatabase = {
    1:{'task':'sadad'},
}

@app.get("/")
def getItems():
    return ['Item 1', 'Item 2']

@app.get("/{id}")
def getItem(id:int):
    return fakeDatabase[id] 