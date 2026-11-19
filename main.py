from fastapi import FastAPI
from pydantic import BaseModel # for the model
app = FastAPI()

@app.get("/")
def root ():
    return {"Hello World"}

# a model for the producs
"""
class Product(BaseModel):
    product_name: str
    product_price: float

#for when the web/app wants to view products...
@app.get("/products")
def get_products():
    return {"id": 1, "name": "Product 1", "price": ""}

@app.post("/products")
def create_product(product_name: str, product_price: float):
    return{"Successfully saved product": {"name": product_name, "price": product_price}}
"""