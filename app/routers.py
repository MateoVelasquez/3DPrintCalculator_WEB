"""Routers

Modulo con las rutas de la API
"""
from flask import Blueprint, jsonify, request
from .models import CfgParameters


calculator_api = Blueprint('calculator_api', __name__)


@calculator_api.route('/api/cfgparameters', methods=['GET'])
def cfgparams():
    if request.method == 'GET':
        cfgparameters = []
        for row in CfgParameters.query.all():
            cfgparameters.append(row.to_json())
        response = jsonify({'parameters': cfgparameters})
        return response
    elif request.method == 'POST':
        pass
