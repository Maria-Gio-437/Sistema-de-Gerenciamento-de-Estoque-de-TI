import pytest
from apirest import app
from unittest.mock import patch, MagicMock
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_criar_equipamento_sucesso(client):
    """Testa a criação de um equipamento com sucesso."""
    novo_equipamento = {
        'nome': 'Teclado Microsoft',
        'numero_serie': 'SN789',
        'tipo': 'Teclado',
        'data_aquisicao': '2024-01-20',
        'status': 'ativo',
        'funcionario_id': None,
        'departamento_id': None
    }

    mock_response = MagicMock()
    mock_response.data = [{**novo_equipamento, 'id': 'uuid-eq-001'}]

    with patch('apirest.supabase.client') as mock_client:
        mock_client.from_.return_value.insert.return_value.execute.return_value = mock_response

        response = client.post('/equipamentos', data=json.dumps(novo_equipamento), content_type='application/json')
        
        assert response.status_code == 201
        json_data = json.loads(response.data)
        assert json_data[0]['nome'] == 'Teclado Microsoft'
        assert json_data[0]['id'] == 'uuid-eq-001'
        mock_client.from_.assert_called_with('equipamento')
