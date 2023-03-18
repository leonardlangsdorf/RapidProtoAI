from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graphene import ObjectType, String, Schema
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_graphql import GraphQLApp

#uvicorn main:app --reload 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/hello/{name}")
async def read_item(name: str):
    return {"message": f"Hello, {name}"}

@app.post("/json")
async def create_json(data: dict):
    return JSONResponse(content=data)

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return f"Hello, {name}!"

schema = Schema(query=Query)

@app.get("/graphql")
async def graphql(request: Request):
    response = GraphQLApp(schema=schema)(request)
    response.set_cookie(key='name', value='value')
    return response
