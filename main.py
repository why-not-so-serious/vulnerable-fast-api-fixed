
from fastapi import FastAPI, Request, Depends, HTTPException, WebSocket
from fastapi.responses import HTMLResponse
import sqlite3
import os
import subprocess
import pickle
import yaml
import jwt

app = FastAPI()

DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"
JWT_SECRET = "my-secret-key"

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return {"user": result}
