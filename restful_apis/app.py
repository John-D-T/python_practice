"""
pip install flask
pip install flask_sqlalchemy
pip install flask_marshmallow
pip install flask_restful
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api