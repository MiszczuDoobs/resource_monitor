from flask import Flask, render_template
import psutil
import json
import time
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
socket = SocketIO(app)
connected=True

@app.route('/')
def index():
    return render_template('index.html')

@socket.on('connect')
def connection_handler():
    print('Connected')

@socket.on('disconnect')
def disconnect_handler():
  print('Disconnected')
  connected=False

@socket.on('handshake')
def handshake_handler(handshake):
  while(connected):
    socket.emit('performance_stats', 
    {'cpu_usage' :psutil.cpu_percent(), 
    'memory': psutil.virtual_memory()})
    socket.sleep(1)

if __name__ == '__main__':
    socket.run(app, debug=True)
