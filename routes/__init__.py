from flask import Blueprint

# Blueprint tanımlama
routes = Blueprint('routes', __name__)

from . import routes  # routes.py dosyasını içeri aktar

