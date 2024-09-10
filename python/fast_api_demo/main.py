"""This module contains demo code for fast api calculator"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalRequest(BaseModel):
    """__summary__"""
    val_1: int
    val_2: int

class CalResponse(BaseModel):
    """__summary__"""
    val_1: int
    val_2: int
    result: int

@app.get("/{value_1}/{value_2}")
def add(value_1: int, value_2: int):
    """adding"""
    return value_1 + value_2

@app.post("/sub", response_model= CalResponse)
def sub(request: CalRequest):
    """__summary__"""
    response = CalResponse(
        val_1= request.val_1,
        val_2= request.val_2,
        result= request.val_1 - request.val_2
    )
    return response
