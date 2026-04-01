from flask import Flask, request, jsonify
app = Flask(__name__)
tareas = [
    {'id': 1, 'tarea': 'aprender flask', 'completado': False},
    {'id': 2, 'tarea': 'aprender flask', 'completado': False}
]

#get / obtener todas las tareas
@app.route('/api/tareas', methods=['GET'])
def listar_tareas():
    return jsonify(tareas)

#GET / obtener una tarea especifica
def obtener_tarea(tarea_id):
    for t in tareas:
        if t['id'] == tarea_id:
            tarea = t
            break
    if tarea:
        return jsonify(tarea)
    return jsonify({'error': 'tarea no encontrada'}), 404

