from typing import Union
from fastapi import APIRouter

router = APIRouter(
    prefix = "/items",
    tags = ["items"],
    responses = {404: {"description": "Not found"}},
)
# id를 입력하지 않은 경우, 에러 메시지 

@router.get("/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 호출 방법: localhost:8000/10
# 응답 결과: {"item_id":10, "q": null}