from flask import Flask, request
import json
from mock_data import catalog
from config import db
from flask_cors import CORS


app = Flask("server")
CORS(app) #disable CORS to allow request from any origin

@app.get("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "this is another endpoint"

@app.get("/about")
def about():
    return "Jim Barnett"

################################################################
################################Catalog API#####################
################################################################

@app.get("/api/version")
def version():
    version = {
        "V":"V.1.1",
        "name":"Candy_Firewall",
        "yourzip":"your"
    }
    return json.dumps(version)

@app.get("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for prod in cursor: #travel cursor
        prod["_id"] = str(prod["_id"]) #fix _id issue
        results.append(prod)
    return json.dumps(results)

#get product by category
@app.get("/api/catalog/<category>")
def get_by_category(category):
    cursor = db.products.find({"category": category})
    #create a list, travel the cursor, fix the id, add it to the list, return list
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        results.append(prod)
    return json.dumps(results)

#create endpoint to save products
@app.post("/api/catalog")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

    product["_id"] = str(product["_id"]) #clean the obj id into json syntax

    return json.dumps(product)

#get product by title search
@app.get("/api/catalog/search/<title>")
def search_by_title(title):
    #return all products whose title CONTAINS the title variable
    cursor = db.products.find({"title": {"$regex": title, "$options": "i"}}) #this will allow searching by title to return results near to what the user searched for
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        results.append(prod)
    return json.dumps(results)
            

#return product with price less than 10 or 23

@app.get("/api/catalog/price/<price>")
def search_by_price(price):
    #get all the products, travel cursor instead of catalog
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        if prod["price"] < float(price):
            prod["_id"] = str(prod["_id"])
            results.append(prod)
    return json.dumps(results)

    #create a get endpoint that returns the number of products in the catalog
@app.get("/api/product/count")
def count_products():
    count = db.products.count_documents({})
    return json.dumps(count)
    #or json.dumps(len(catalog))

#return the cheapest product
@app.get("/api/catalog/cheapest")
def cheapest_product():
    cursor = db.products.find({})
    answer = cursor[0]
    for prod in cursor:
        if prod["price"] < answer["price"]:
            answer = prod           
    prod["_id"] = str(prod["_id"])           
    return json.dumps(prod)


@app.get('/test/numbers')
def get_numbers():

    result = []
    for n in range(1, 21):
        if n != 12 and n != 18:
            result.append(n)

    return json.dumps(result)

app.run(debug=True)