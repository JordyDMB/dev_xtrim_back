# app/routes.py
from flask import Blueprint, jsonify, request
from .database import mysql

api_bp = Blueprint('api', __name__)

@api_bp.route('/consumption/<int:user_id>', methods=['GET'])
def get_consumption(user_id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT id, user_id, consumption_type, amount, consumption_date, consumption_time, created_at
            FROM consumption
            WHERE user_id = %s
            ORDER BY consumption_date DESC
        """, (user_id,))
        rows = cursor.fetchall()
        cursor.close()

        data = []
        for row in rows:
            data.append({
                "id": row[0],
                "user_id": row[1],
                "consumption_type": row[2],
                "amount": row[3],
                "consumption_date": row[4].isoformat(),
                "consumption_time": str(row[5]) if row[5] else None,
                "created_at": row[6].isoformat()
            })
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/consumption', methods=['POST'])
def add_consumption():
    data = request.json
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO consumption (user_id, consumption_type, amount, consumption_date, consumption_time)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data.get('user_id'),
            data.get('consumption_type'),
            data.get('amount'),
            data.get('consumption_date'),
            data.get('consumption_time')
        ))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Consumption added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
