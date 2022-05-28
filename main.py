from pyexpat import model
from fastapi import FastAPI, Body, Depends
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()    



app = FastAPI()
 
fakeDatabase = {
    1:{'task':'sadad'},
}

@app.get("/")
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item

@app.post("/")
def addItem(item:schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(name = item.name)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

# @app.post("/")
# def addItem(body = Body()):
#    newId = len(fakeDatabase.keys()) + 1
#    fakeDatabase[newId] = {"task":body['task']}
#    return fakeDatabase  

@app.put("/{id}")
def updateItem(id:int, item:schemas.Item, session: Session = Depends(get_session)):
    itemObj = session.query(models.Item).get(id)
    itemObj.name = item.name
    session.commit()
    return itemObj

@app.delete("/{id}")
def updateItem(id:int, session: Session = Depends(get_session)):
    itemObj = session.query(models.Item).get(id)
    session.delete(itemObj)
    session.commit()
    session.close()
    return 'Name was delete'   

