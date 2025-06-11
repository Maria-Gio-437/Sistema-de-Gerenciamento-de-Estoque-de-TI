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

# ========================= AUTENTICACAO =========================

@app.route('/auth/signup', methods=['POST'])
def signup_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email e senha são obrigatórios'}), 400

    try:
        response = supabase.client.auth.sign_up({"email": email, "password": password})

        if hasattr(response, 'user') and response.user:
            return jsonify({
                'message': 'Usuário cadastrado com sucesso. Verifique seu email para confirmar.',
                'user': response.user.dict(),
                'session': response.session.dict() if response.session else None
            }), 201
        elif hasattr(response, 'error') and response.error: # Erro do Supabase
            return jsonify({'error': response.error.message}), 400
        else:
            return jsonify({'error': 'Erro desconhecido ou resposta inesperada da autenticação'}), 500

    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor ao cadastrar usuário', 'details': f"Trace: {str(e)} Type: {type(e).__name__}"}), 500

@app.route('/auth/signin', methods=['POST'])
def signin_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email e senha são obrigatórios'}), 400

    try:
        response = supabase.client.auth.sign_in_with_password({"email": email, "password": password})

        if hasattr(response, 'user') and response.user:
            return jsonify({
                'message': 'Login realizado com sucesso.',
                'user': response.user.dict(),
                'session': response.session.dict()
            }), 200
        elif hasattr(response, 'error') and response.error: # Erro do Supabase (credenciais inválidas)
            return jsonify({'error': response.error.message}), 401
        else:
            return jsonify({'error': 'Erro desconhecido ou resposta inesperada da autenticação'}), 500

    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor ao fazer login', 'details': f"Trace: {str(e)} Type: {type(e).__name__}"}), 500

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
    try:
        resp = supabase.client.from_('empresa').insert([data]).execute()
        if resp.data is not None and len(resp.data) > 0:
            return jsonify(resp.data), 201
        else:
            return jsonify({'message': 'Empresa criada com sucesso, mas sem dados de retorno'}), 201
    except Exception as e:
        return jsonify({'error': 'Erro ao criar empresa', 'details': str(e)}), 500

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
    try:
        dados_para_insercao = {
            'nome': data.get('nome'),
            'email': data.get('email'),
            'senha': data.get('senha'),
            'cpf': data.get('cpf'),
            'telefone': data.get('telefone'),
            'empresa_id': data.get('empresa_id') 
        }

        dados_finais = {k: v for k, v in dados_para_insercao.items() if v is not None}

        resp = supabase.client.from_('gestor').insert([dados_finais]).execute()

        if resp.data is not None and len(resp.data) > 0:
            return jsonify(resp.data), 201
        else:
            return jsonify({'message': 'Gestor criado com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': 'Erro ao criar gestor', 'details': str(e)}), 500

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

# ======================== FUNCIONARIO ========================
# Listar funcionario
@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    resp = supabase.client.from_('funcionario').select('*').execute()
    if resp.data is not None:
        return jsonify(resp.data), 200
    else:
        return jsonify({'error': 'Erro ao buscar funcionario', 'details': resp}), 500

# Criar funcionario
@app.route('/funcionarios', methods=['POST'])
def criar_funcionario():
    try:
        data = request.json
        nome_departamento = data.get('departamento')

        if not nome_departamento:
            return jsonify({'error': 'O campo "departamento" (com o nome) é obrigatório'}), 400

        resp_depto = supabase.client.from_('departamento').select('id').eq('nome', nome_departamento).execute()

        if not resp_depto.data:
            return jsonify({'error': f'Departamento com o nome "{nome_departamento}" não foi encontrado.'}), 404
        
        departamento_id = resp_depto.data[0]['id']

        dados_para_inserir = {
            'nome': data.get('nome'),
            'email': data.get('email'),
            'senha': data.get('senha'), # Lembre-se de criptografar senhas em produção!
            'cpf': data.get('cpf'),
            'funcao': data.get('funcao'),
            'departamento_id': departamento_id # Aqui usamos o ID que encontramos!
        }

        resp_funcionario = supabase.client.from_('funcionario').insert([dados_para_inserir]).execute()

        if resp_funcionario.data:
            return jsonify(resp_funcionario.data[0]), 201
        else:
            error_details = str(resp_funcionario.error) if resp_funcionario.error else "Detalhes não disponíveis"
            return jsonify({'error': 'Erro ao inserir funcionário no banco de dados.', 'details': error_details}), 500

    except Exception as e:
        return jsonify({'error': 'Ocorreu um erro interno no servidor.', 'details': str(e)}), 500
   
# Editar funcionario
@app.route('/funcionarios/<id>', methods=['PUT'])
def editar_funcionario(id):
    data = request.json
    resp = supabase.client.from_('funcionario').update(data).eq('id', id).execute()
    if resp.data is not None and len(resp.data) > 0:
        return jsonify(resp.data), 200
    elif resp.count > 0:
        return jsonify({'message': 'Funcionario atualizado com sucesso'}), 200
    else:
        return jsonify({'error': 'Erro ao editar funcionario', 'details': resp}), 500

# Excluir funcionario
@app.route('/funcionarios/<id>', methods=['DELETE'])
def excluir_funcionario(id):
    try:
        resp = supabase.client.from_('funcionario').delete().eq('id', id).execute()
        return jsonify({'message': 'Funcionario excluído com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': 'Erro ao excluir funcionario', 'details': str(e)}), 500

# Health check da conexão com o Supabase
@app.route('/health', methods=['GET'])
def health_check():
    try:
        resp = supabase.client.from_('empresa').select('id').limit(1).execute()
        if resp.data is not None:
            return jsonify({'status': 'Conectado ao Supabase!'}), 200
        else:
            return jsonify({'status': 'Erro ao conectar ao Supabase', 'error': resp.error}), 500
    except Exception as e:
        return jsonify({'status': 'Erro inesperado ao conectar ao Supabase', 'error': str(e)}), 500

@app.route("/")
def home():
    return "API de Gerenciamento de Estoque de TI está no ar!", 200

if __name__ == '__main__':
    app.run(debug=True)