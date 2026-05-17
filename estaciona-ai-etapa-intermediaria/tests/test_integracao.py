from src.main import buscar_endereco

def test_buscar_endereco():
    dados = buscar_endereco("01001000")
    assert dados["localidade"] == "São Paulo"
