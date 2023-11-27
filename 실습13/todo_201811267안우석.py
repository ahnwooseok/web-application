from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class TodoItem(BaseModel):
    id: int
    item: str
class SingleTodoItem(BaseModel):
    todo: TodoItem
class TodoItems(BaseModel):
    todos: List[TodoItem]

todo_list = []

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "할 일 리스트 서비스"}

@app.get("/todo", response_model=TodoItems, tags=["Todo"])
async def read_all_todos():
    return {"todos": todo_list}

@app.get("/todo/{todo_id}", response_model=SingleTodoItem, tags=["Todo"])
async def read_single_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="할 일 못찾음")

@app.post("/todo", status_code=status.HTTP_201_CREATED, tags=["Todo"])
async def create_todo(todo: TodoItem):
    todo_list.append(todo)
    return {"message": "할 일 추가 완료"}

@app.put("/todo/{todo_id}", tags=["Todo"])
async def update_todo(todo_id: int, item: str):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index].item = item
            return {"message": "할 일 업데이트 완료"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="할 일 없음")

@app.delete("/todo/{todo_id}", tags=["Todo"])
async def delete_todo(todo_id: int):
    global todo_list
    todo_list = [todo for todo in todo_list if todo.id != todo_id]
    return {"message": "할 일 제거 완료"}

@app.delete("/todo", tags=["Todo"])
async def delete_all_todos():
    global todo_list
    todo_list = []
    return {"message": "모든 할 일 제거 완료"}