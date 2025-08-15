from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hallo Welt, wie geht es dir?"}

# python
# git
# fastapi
# openai api
# streamlit
# postgresql