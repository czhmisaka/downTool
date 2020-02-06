# -*- coding: UTF-8 -*-
from flask import Flask
from flask_socketio import SocketIO, emit
from flask import request
from flask import render_template
from flask import session
from datetime import timedelta
import json
import random
import time
# app = Flask(__name__)
# app.config["SECRET_KEY"] = "xcbo221"
# tasks = ''
# newTask = ''
# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html',title='hi~~~')
# @app.route('/getTask',methods=['GET', 'POST'])
# def getTask():
#     global tasks
#     return tasks



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
tasks = ''
newTask = ''
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/createTask',methods=['POST'])
def createTask():
    global newTask
    data = request.json        # 获取 JOSN 数据
    task = data["task"]
    newTask = task
    print(task)
    socketio.emit("onupdate",{'code':3,'data': task},namespace="/client")
    return "1001"
@app.route('/refresh',methods=['POST'])
def refresh():
    global newTask
    global tasks
    tasks = request.form["tasks"]
    socketio.emit('response', {'data': tasks},namespace='/test')
    #_tasks = json.loads(tasks,encoding='utf-8')
    if newTask:
        _newTask = newTask
        newTask = ''
        return _newTask
    else:
        return "ok"
@socketio.on('update', namespace='/test')
def test_message(message):
    global tasks
    time.sleep(1)
@socketio.on('connect', namespace='/test')
def test_connect():
    emit('connect', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')
@socketio.on('checkStatus',namespace="/client")
def onmessage(message):
    time.sleep(1)
    print(message)
    socketio.emit("onstart",{'data': 'hello world'},namespace="/client")
@socketio.on('onupdate',namespace="/client")
def onupdate(message):
    time.sleep(1)
    print(message)
    tasks = message.get("tasks")
    socketio.emit('response', {'data': tasks},namespace='/test')
    socketio.emit("onupdate",{'code':1,'data': 'hello world'},namespace="/client")

if __name__ == '__main__':
    socketio.run(app)