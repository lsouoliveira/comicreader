from flask import request
from flask_restx import Resource
from flask_restx import Namespace
from typing import Dict, Tuple

api = Namespace('test')  

@api.route('/')
class Test(Resource):
    def get(self):
        raise Exception('error')
        return 'test'
