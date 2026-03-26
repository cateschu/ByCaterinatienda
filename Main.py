from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API funcionando 🚀"}

@app.get("/trends")
def get_trends():
    productos = [
        {
            "name": "Mini proyector portátil",
            "viral_score": random.randint(70, 95),
            "precio_estimado": 25000,
            "ganador": True
        },
        {
            "name": "Mini impresora térmica",
            "viral_score": random.randint(60, 90),
            "precio_estimado": 18000,
            "ganador": True
        },
        {
            "name": "Luz LED RGB",
            "viral_score": random.randint(40, 70),
            "precio_estimado": 12000,
            "ganador": False
        }
    ]

    return productos
