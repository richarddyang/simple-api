"""NOTE
This an over simplified version of an application made with FastAPI.

In production, we would split the accessing of the csv (or database), the different routes, 
and potential functions into thier own designated file/ folders. Please look at the
following: https://fastapi.tiangolo.com/tutorial/bigger-applications/ for more information.
"""
import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# create app
app = FastAPI()

# accepts requests from the following urls
origins = ["*"]

# add CORS compliannce middleware to allow access to api from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


# This endpoint refers to "http://<DOMAIN>:<PORT>/"
@app.get("/")
async def home():
    return "Welcome to the simple API!!"


"""Getting Data
For this example, we are using pandas to read from a csv (as if it was a database table)
and returning the data along with the column headers in a dictionary format. 

FastAPI will then convert this dictionary into json automatically.

** In production, we would be querying an actual database, but a csv file is used here to
keep things simple.
"""


# This endpoint refers to "http://<DOMAIN>:<PORT>/data/"
@app.get("/data")
async def get_data():
    df = pd.read_csv("./cars.csv")
    headers = headers = list(df.columns)
    data = df.to_dict("records")
    return {"headers": headers, "data": data}


"""Run Server
Uvicorn is an ASGI server that we will use to run this application. 

Using uvicorn here isn't necessary, but it makes development nicer since you 
only need to run the command "python main.py" on your terminal.

This is an alternative to running "uvicorn main:app --host 127.0.0.1 --reload" 
on your terminal

** In production, we would rather use the "uvicorn main:app --host 127.0.0.1 --reload"
instead of this alternative. However it's simpler to use this during development as 
"python main.py" is much easier to remember.
"""
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True, port=5000)
