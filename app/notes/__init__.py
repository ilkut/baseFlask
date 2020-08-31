from flask import Blueprint

bp = Blueprint('Note', __name__)

from app.notes import routes