from fastapi import FastAPI, File
import Pyro4

app = FastAPI(
    title="Find Object on Image"
)

@app.post("/")
def get_image(file: bytes = File(...)):
    edit_image = Pyro4.Proxy("PYRONAME:edit.image")
    response = edit_image.get_image(file)
    return {"status": 200, "data": response}
