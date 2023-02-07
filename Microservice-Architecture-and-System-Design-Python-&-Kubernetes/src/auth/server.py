import datetime
import os
import sys

import jwt
from flask import Flask, request

from ddbb import connection

server = Flask(__name__)


# server configuratio

@server.route("/login", methods=["POST"])
def login():

    auth = request.authorization

    if not auth:
        return "missing credentials", 401

    cur = connection.connection.cursor()

    res = cur.execute(
        f"select email,password from user where email={auth.username}")

    if res:
        user_row = cur.fetchone()

        email = user_row[0]
        password = user_row[1]

        if auth.username != email or auth.password != password:
            return 'invalid credentials', 401
        else:
            return createJWT(auth.username, os.environ.get('JWT_SECRET'), True)
    else:
        return 'invalid credentials', 401
