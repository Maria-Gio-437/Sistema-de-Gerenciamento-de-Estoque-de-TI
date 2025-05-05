from flask import Flask, request, jsonify
from flask_supabase import Supabase
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)
CORS(app, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.config['SUPABASE_URL'] = os.getenv('SUPABASE_URL')
app.config['SUPABASE_KEY'] = os.getenv('SUPABASE_KEY')

supabase = Supabase(app)

# ========================= EMPRESA =========================

# Listar empresas
@app.route('/empresas', methods=['GET'])
def listar_empresas():
    resp = supabase.client.from_('empresa').select('*').execute()
    if resp.data is not None:
        return jsonify(resp.data), 200
    else:
        return jsonify({'error': 'Erro ao buscar empresas', 'details': resp}), 500

# Criar empresa
@app.route('/empresas', methods=['POST'])
def criar_empresa():
    data = request.json
    resp = supabase.client.from_('empresa').insert([data]).execute()
    if resp.data is not None and len(resp.data) > 0:
        return jsonify(resp.data), 201
    else:
        return jsonify({'error': 'Erro ao criar empresa', 'details': resp}), 500

# Editar empresa
@app.route('/empresas/<id>', methods=['PUT'])
def editar_empresa(id):
    data = request.json
    resp = supabase.client.from_('empresa').update(data).eq('id', id).execute()
    if resp.data is not None and len(resp.data) > 0:
        return jsonify(resp.data), 200
    elif resp.count > 0:
        return jsonify({'message': 'Empresa atualizada com sucesso'}), 200
    else:
        return jsonify({'error': 'Erro ao editar empresa', 'details': resp}), 500

# Excluir empresa
@app.route('/empresas/<id>', methods=['DELETE'])
def excluir_empresa(id):
    try:
        resp = supabase.client.from_('empresa').delete().eq('id', id).execute()
        return jsonify({'message': 'Empresa excluída com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': 'Erro ao excluir empresa', 'details': str(e)}), 500

# ========================= GESTOR =========================

# Listar gestores
@app.route('/gestores', methods=['GET'])
def listar_gestores():
    resp = supabase.client.from_('gestor').select('*').execute()
    if resp.data is not None:
        return jsonify(resp.data), 200
    else:
        return jsonify({'error': 'Erro ao buscar gestores', 'details': resp}), 500

# Criar gestor
@app.route('/gestores', methods=['POST'])
def criar_gestor():
    data = request.json
    resp = supabase.client.from_('gestor').insert([data]).execute()
    if resp.data is not None and len(resp.data) > 0:
        return jsonify(resp.data), 201
    else:
        return jsonify({'error': 'Erro ao criar gestor', 'details': resp}), 500

# Editar gestor
@app.route('/gestores/<id>', methods=['PUT'])
def editar_gestor(id):
    data = request.json
    resp = supabase.client.from_('gestor').update(data).eq('id', id).execute()
    if resp.data is not None and len(resp.data) > 0:
        return jsonify(resp.data), 200
    elif resp.count > 0:
        return jsonify({'message': 'Gestor atualizado com sucesso'}), 200
    else:
        return jsonify({'error': 'Erro ao editar gestor', 'details': resp}), 500

# Excluir gestor
@app.route('/gestores/<id>', methods=['DELETE'])
def excluir_gestor(id):
    try:
        resp = supabase.client.from_('gestor').delete().eq('id', id).execute()
        return jsonify({'message': 'Gestor excluído com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': 'Erro ao excluir gestor', 'details': str(e)}), 500

# ========================= DEPARTAMENTO =========================

# Listar departamentos
@app.route('/departamentos', methods=['GET'])
def listar_departamentos():
    resp = supabase.client.from_('departamento').select('*').execute()
    if resp.data is not None:
        return jsonify(resp.data), 200
    else:
        return jsonify({'error': 'Erro ao buscar departamentos', 'details': resp}), 500

# Criar departamento
@app.route('/departamentos', methods=['POST'])
def criar_departamento():
    data = request.json
    resp = supabase.client.from_('departamento').insert([data]).execute()
    if resp.data is not None and len(resp.data) > 0:
        return jsonify(resp.data), 201
    else:
        return jsonify({'error': 'Erro ao criar departamento', 'details': resp}), 500

# Editar departamento
@app.route('/departamentos/<id>', methods=['PUT'])
def editar_departamento(id):
    data = request.json
    resp = supabase.client.from_('departamento').update(data).eq('id', id).execute()
    if resp.data is not None and len(resp.data) > 0:
        return jsonify(resp.data), 200
    elif resp.count > 0:
        return jsonify({'message': 'Departamento atualizado com sucesso'}), 200
    else:
        return jsonify({'error': 'Erro ao editar departamento', 'details': resp}), 500

# Excluir departamento
@app.route('/departamentos/<id>', methods=['DELETE'])
def excluir_departamento(id):
    try:
        resp = supabase.client.from_('departamento').delete().eq('id', id).execute()
        return jsonify({'message': 'Departamento excluído com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': 'Erro ao excluir departamento', 'details': str(e)}), 500

# ========================= EQUIPAMENTO =========================

# Listar equipamentos
@app.route('/equipamentos', methods=['GET'])
def listar_equipamentos():
    resp = supabase.client.from_('equipamento').select('*').execute()
    if resp.data is not None:
        return jsonify(resp.data), 200
    else:
        return jsonify({'error': 'Erro ao buscar equipamentos', 'details': resp}), 500

# Criar equipamento
@app.route('/equipamentos', methods=['POST'])
def criar_equipamento():
    data = request.json
    resp = supabase.client.from_('equipamento').insert([data]).execute()
    if resp.data is not None and len(resp.data) > 0:
        return jsonify(resp.data), 201
    else:
        return jsonify({'error': 'Erro ao criar equipamento', 'details': resp}), 500

# Editar equipamento
@app.route('/equipamentos/<id>', methods=['PUT'])
def editar_equipamento(id):
    data = request.json
    resp = supabase.client.from_('equipamento').update(data).eq('id', id).execute()
    if resp.data is not None and len(resp.data) > 0:
        return jsonify(resp.data), 200
    elif resp.count > 0:
        return jsonify({'message': 'Equipamento atualizado com sucesso'}), 200
    else:
        return jsonify({'error': 'Erro ao editar equipamento', 'details': resp}), 500

# Excluir equipamento
@app.route('/equipamentos/<id>', methods=['DELETE'])
def excluir_equipamento(id):
    try:
        resp = supabase.client.from_('equipamento').delete().eq('id', id).execute()
        return jsonify({'message': 'Equipamento excluído com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': 'Erro ao excluir equipamento', 'details': str(e)}), 500

@app.route("/")
def home():
    return "API de Gerenciamento de Estoque de TI está no ar!", 200

if __name__ == '__main__':
    app.run(debug=True)