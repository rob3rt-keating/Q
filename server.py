import uvicorn

if __name__ == '__main__':
    print('Running Q')
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
    print('Shutting down Q')