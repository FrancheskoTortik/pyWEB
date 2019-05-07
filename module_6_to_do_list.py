## server.py
from bottle import route, run, view, get, static_file
from datetime import datetime as dt
from random import random
import os


class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_completed = False
    def __str__(self):
        pass


@route("/static/<filename:path>")
def send_static(filename):
   return static_file(filename, root="static")

cwd = os.getcwd() + os.sep + 'views' + os.sep + 'index1.tpl'
print(cwd)
@route("/")
@view(cwd)
def index1():
    tasks = [
        TodoItem("прочитать книгу"),
        TodoItem("учиться жонглировать 30 минут"),
        TodoItem("помыть посуду"),
        TodoItem("поесть"),
    ]
    return {"tasks": tasks}


###
run(
  host="localhost",
  port=8080,
  autoreload=True
)