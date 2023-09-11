# Local
from database import server

#External
from fastapi import FastAPI

app = FastAPI()

@app.get("/random")
async def get_random_dinosaur():
  result = server.aggregate()
  return result

@app.get("/dinosaurs/{name}")
async def get_dinosaur(name: str):
  result = server.find(name)
  return result