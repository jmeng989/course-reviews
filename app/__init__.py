from flask import Flask, Request
from config import Config

class R(Request):
    trusted_hosts = {
        "jm2598.user.srcf.net",
    }

app = Flask(__name__)
app.request_class = R
app.config.from_object(Config)


from app import routes