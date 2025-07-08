from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    completed: bool

@app.get("/tasks/daily", response_model=List[Task], tags=["Tasks"])
def get_daily_tasks():
    """
    Retrieve the list of daily tasks.
    """
    tasks = [
        Task(id=1, title="Check emails", completed=False),
        Task(id=2, title="Team stand-up meeting", completed=True),
        Task(id=3, title="Write project report", completed=False)
    ]
    return tasks
