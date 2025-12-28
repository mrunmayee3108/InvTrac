from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

# session -> actual DB session object (used to query, add, commit data)
# Session -> class/type (used for type hints or creating new sessions)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods = ["*"]
)

database_models.Base.metadata.create_all(bind=engine)  # Create ALL tables present in metadata (if they dont already exist)

@app.get("/")
def greet():
    return "Hello! Welcome to InvTrac"

Products = [
    product(id = 1, name = "Samsung S25 Ultra", description = "Mobile Phone", price = 129999.00, quantity = 10),
    product(id = 2, name = "Lenovo LOQ Ryzen 7", description = "Laptop", price = 80000.00, quantity = 50),
    product(id = 3, name = "Apple Ipad", description = "Ipad", price = 35000.00, quantity = 30)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(database_models.product).count   # this initialisation must be done only once. if we run again, then we'll get duplicate data. SO make sure it runs only once.
    if count == 0:
        for product in Products:
            db.add(database_models.product(**product.model_dump()))  # db.add(database_models.product-->database(product)-->pydantic)
                                                                 # model_dump: Convert to dictionary. ** unpack dictionary values. so we can pass like (name="xyz", id=2)
        db.commit()
init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_prods = db.query(database_models.product).all()
    return db_prods

@app.get("/products/{id}")
def get_prod_by_id(id: int, db: Session = Depends(get_db)):
    db_prod = db.query(database_models.product).filter(database_models.product.id == id).first()
    if db_prod:
        return db_prod
    return "Product not found"

@app.post("/products")
def add_new_prod(product: product, db: Session = Depends(get_db)):
    db.add(database_models.product(**product.model_dump()))
    db.commit()
    return Products

@app.put("/products/{id}")
def update_prod(id: int, product: product, db: Session = Depends(get_db)):
    db_prod = db.query(database_models.product).filter(database_models.product.id == id).first()
    if db_prod:
        db_prod.name = product.name
        db_prod.description = product.description
        db_prod.price = product.price
        db_prod.quantity = product.quantity
        db.commit()
        return "Product added successfully!"
    else:
        return "Product not found"
        
@app.delete("/products/{id}")
def delete_prod(id: int, db: Session = Depends(get_db)):
    db_prod = db.query(database_models.product).filter(database_models.product.id == id).first()
    if db_prod:
        db.delete(db_prod)
        db.commit()
        return "Product deleted successfully!"
    else:
        return "Product not found!"
    
    

