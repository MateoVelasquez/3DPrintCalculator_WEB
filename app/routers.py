"""Routers

Modulo con las rutas de la API
"""
from flask import Blueprint, jsonify, render_template, request
from .models import CfgParameters
from app import db, calculator_core


calculator_api = Blueprint('calculator_api', __name__)


@calculator_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@calculator_api.route('/api/cfgparameters', methods=['GET', 'POST'])
def cfgparams():
    if request.method == 'GET':
        cfgparameters = []
        for row in CfgParameters.query.all():
            cfgparameters.append(row.to_json())
        response = jsonify({'parameters': cfgparameters})
        return response
    elif request.method == 'POST':
        try:
            cfg = CfgParameters()
            cfg.amortization_years = request.form['amortization_years']
            cfg.daily_printer_time = request.form['daily_printer_time']
            cfg.electric_cost = request.form['electric_cost']
            cfg.failure_rate_prcent = request.form['failure_rate_prcent']
            cfg.material_cost = request.form['material_cost']
            cfg.material_density = request.form['material_density']
            cfg.measure_unit = bool(request.form['measure_unit'])
            cfg.printer_power = request.form['printer_power']
            cfg.printer_price = request.form['printer_price']
            cfg.profile_name = request.form['profile_name']
            cfg.spool_weigth = request.form['spool_weigth']
            cfg.workforce_cost = request.form['workforce_cost']
            db.session.add(cfg)
            db.session.commit()
            response = jsonify({'message': 'Configuración agregada', 'parameters': cfg.to_json()})
        except Exception as e:
            response = jsonify({'message': 'Error agregando información'})
        return response


@calculator_api.route('/api/calculate', methods=['GET'])
def calculatevalue():
    data = request.args.to_dict()
    if 'profilename' in  data.keys():
        profilename = data['profilename']
    else:
        profilename = 'Default'
    print_h = int(request.args.get('hours'))
    print_m = int(request.args.get('minutes'))
    material = float(request.args.get('material'))
    workhours = float(request.args.get('workhours'))
    cfgdict = CfgParameters.query.filter(CfgParameters.profile_name == profilename).first()
    cfgdict = cfgdict.to_json()
    printcost = calculator_core.calculate_cost(print_h, print_m, workhours, material, cfgdict)
    return jsonify({'print_cost': printcost, 'currency': 'COP', 'profile': cfgdict['profile_name'], 'message': 'Correcto'})