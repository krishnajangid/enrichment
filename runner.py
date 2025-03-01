import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", port=5003, reload=True)
