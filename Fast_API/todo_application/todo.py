#Importing necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List 

#Creating a FastAPI instance
app = FastAPI()

#Create Data Model 
class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
    
#Temporary database to store todos
todos = []

#Create Todo (POST)
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo added", "data": todo}
    
#Reading All Todos (GET)
@app.get("/todos")
def get_todos():
    return todos
    
#Reading Single Todo (GET)
@app.get("/todos/{todo_id}")    
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")
    
#Updating a Todo (PUT)
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo updated", "data": updated_todo}
    raise HTTPException(status_code=404, detail="Todo not found")
    
#Deleting a Todo (DELETE)
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted = todos.pop(index)
            return {"message": "Deleted Successfully", "data": deleted}
    raise HTTPException(status_code=404, detail="Todo not found")
    