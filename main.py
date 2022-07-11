# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_helloworld_service]
# [START run_helloworld_service]
import os

# import scipy as sp
# from joblib import dump, load
import flask
from flask import request, send_file
from flask_socketio import SocketIO, send, emit

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, max_http_buffer_size = 100000000)


@socketio.on('connect')
def handle_connect():
    print('connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('disconnected')

@socketio.on('flutter')
def handle_flutter(data):
    print(data)


if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8082)))
