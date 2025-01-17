from datetime import date, time
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
import scheduler as sch

schedulerApp = FastAPI()

class Item(BaseModel):
    id: str
    date: date
    startTime: time
    endTime: time

class Items(BaseModel):
    data: List[Item]
    length: int

@schedulerApp.get("/schedule/duration={duration}_break={brk}_start-date={startDate}_start-time={startTime}_end-time={endTime}", response_model=Items)
async def getSchedule(duration: int, brk: int, startDate: date, startTime: time, endTime: time):
    return sch.callScheduler(duration, brk, startDate, startTime, endTime)

# example - http://127.0.0.1:8000/schedule/duration=17_break=5_start-date=2022-01-25_start-time=17:00_end-time=18:00