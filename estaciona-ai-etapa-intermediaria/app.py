import requests
import streamlit as st

st.set_page_config(page_title="EstacionaAÍ", page_icon="🚗")

st.title("🚗 EstacionaAÍ")
st.write("Sistema com integração à API ViaCEP para buscar endereço por CEP.")

cep = st.text_input("Digite o CEP:", placeholder="Ex: 01001000")

if st.button("Buscar endereço"):
    if not cep:
        st.warning("Digite um CEP.")
    else:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url, timeout=5)
        dados = response.json()

        if "erro" in dados:
            st.error("CEP inválido.")
        else:
            st.success("Endereço encontrado!")
            st.write(f"**Rua:** {dados.get('logradouro')}")
            st.write(f"**Bairro:** {dados.get('bairro')}")
            st.write(f"**Cidade:** {dados.get('localidade')}")
            st.write(f"**Estado:** {dados.get('uf')}")
