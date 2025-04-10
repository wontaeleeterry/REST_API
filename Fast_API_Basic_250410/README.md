/
│
├── controller/
│   ├── items
│   └── users.py
├── __init__.py
├── main.py
└── README.md


# 포트 사용 중일 경우
lsof -i :8000
kill -9 16758

# 실행 방법
uvicorn app.main:app --reload
uvicorn main:app --reload

# 중지할 때
Ctrl + C로 할 것 (맥북)