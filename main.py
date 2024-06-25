import json
from pymysql import connect
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
con = connect(host='localhost',
              user='root',
              password="Admin@34", database='world_x')
cur = con.cursor()


class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool


@app.get("/countries")
def get_data():
    cur.execute("select * from country")
    output = [dict(zip([field[0] for field in cur.description], row)) for row in cur]
    print(output)
    return output


@app.post("/countrieslist")
async def read_item(request: Request):
    print(await request.body())
    print(await request.json())
    return {"item id": "1", "q": "5"}


@app.put("/test")
def save_item():
    arr = []
    cur.execute("select doc from countryinfo")
    output = cur.fetchall()
    for i in output:
        arr.append(json.loads(i[0]))
    print(len(arr))
    return JSONResponse({"countries": arr})
