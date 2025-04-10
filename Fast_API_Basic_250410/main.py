from fastapi import FastAPI
from controller import items, users  
# 하위 폴더 controller에 있는 items, users를 임포트
# 별도의 폴더에 라우터를 추가하여 유지 보수가 편리하도록 처리하는 방법

app = FastAPI()

# 별도의 폴더에 저장되어 있는 라우터를 아래와 같이 추가
app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}