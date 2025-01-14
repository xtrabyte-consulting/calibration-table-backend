from flask import request, jsonify
from . import db
from .models import Equipment
from datetime import datetime

@app.route('/equipment', methods=['GET'])
def get_all_equipment():
    equipment_list = Equipment.query.all()
    return jsonify([{
        'id': equipment.id,
        'equipment_name': equipment.equipment_name,
        'last_calibrated': equipment.last_calibrated.strftime('%Y-%m-%d'),
        'next_due': equipment.next_due.strftime('%Y-%m-%d')
    } for equipment in equipment_list])
    
@app.route('/equipment', methods=['POST'])
def add_equipment():
    data = request.get_json()
    new_equipment = Equipment(
        equipment_name=data['equipment_name'],
        last_calibrated=datetime.strptime(data['last_calibrated'], '%Y-%m-%d'),
        next_due=datetime.strptime(data['next_due'], '%Y-%m-%d')
    )
    db.session.add(new_equipment)
    db.session.commit()
    return jsonify({'id': new_equipment.id, 'message': 'Calibration added successfully'}), 201

@app.route('/equipment/<int:id>', methods=['GET'])
def get_equipment(id):
    equipment = Equipment.query.get(id)
    return jsonify({
        'id': equipment.id,
        'equipment_name': equipment.equipment_name,
        'last_calibrated': equipment.last_calibrated.strftime('%Y-%m-%d'),
        'next_due': equipment.next_due.strftime('%Y-%m-%d')
    })
    
@app.route('/equipment/<int:id>', methods=['PUT'])
def update_equipment(id):
    equipment = Equipment.query.get_or_404(id)
    data = request.get_json()
    equipment.equipment_name = data['equipment_name']
    equipment.last_calibrated = datetime.strptime(data['last_calibrated'], '%Y-%m-%d')
    equipment.next_due = datetime.strptime(data['next_due'], '%Y-%m-%d')
    db.session.commit()
    return jsonify({'message': 'Calibration updated successfully'})

@app.route('/equipment/<int:id>', methods=['DELETE'])
def delete_equipment(id):
    equipment = Equipment.query.get_or_404(id)
    db.session.delete(equipment)
    db.session.commit()
    return jsonify({'message': 'Calibration deleted successfully'})