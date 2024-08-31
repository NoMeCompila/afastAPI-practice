from fastapi import FastAPI, Body
#from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'Ejercicios'
app.version = '1.0'

@app.get('/ej1', tags=['ejercicio 1'])
def message():
    return 'hello'