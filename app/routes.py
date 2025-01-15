from flask import request, jsonify, Blueprint
from . import db
from .models import Equipment
from datetime import datetime

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/equipment', methods=['GET'])
def get_all_equipment():
    equipment_list = Equipment.query.all()
    return jsonify([{
        'id': equipment.id,
        'equipment_name': equipment.equipment_name,
        'last_calibrated': equipment.last_calibrated.strftime('%Y-%m-%d'),
        'next_due': equipment.next_due.strftime('%Y-%m-%d')
    } for equipment in equipment_list])
    
@main_bp.route('/equipment', methods=['POST'])
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

@main_bp.route('/equipment/<int:id>', methods=['GET'])
def get_equipment(id):
    equipment = Equipment.query.get(id)
    return jsonify({
        'id': equipment.id,
        'equipment_name': equipment.equipment_name,
        'last_calibrated': equipment.last_calibrated.strftime('%Y-%m-%d'),
        'next_due': equipment.next_due.strftime('%Y-%m-%d')
    })
    
@main_bp.route('/equipment/<int:id>', methods=['PUT'])
def update_equipment(id):
    equipment = Equipment.query.get_or_404(id)
    data = request.get_json()
    equipment.equipment_name = data['equipment_name']
    equipment.last_calibrated = datetime.strptime(data['last_calibrated'], '%Y-%m-%d')
    equipment.next_due = datetime.strptime(data['next_due'], '%Y-%m-%d')
    db.session.commit()
    return jsonify({'message': 'Calibration updated successfully'})

@main_bp.route('/equipment/<int:id>', methods=['DELETE'])
def delete_equipment(id):
    equipment = Equipment.query.get_or_404(id)
    db.session.delete(equipment)
    db.session.commit()
    return jsonify({'message': 'Calibration deleted successfully'})