# Dashboard Brasil API - Flask

Este projeto é uma aplicação web que permite buscar informações detalhadas sobre um CEP, incluindo dados do IBGE e DDD, utilizando a [BrasilAPI](https://brasilapi.com.br/). Ele é composto por um **backend em Flask** e um **frontend em HTML, CSS e JavaScript**.

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Flask**
- **Flask-CORS** (para permitir requisições entre diferentes origens)
- **Requests** (para consumir a BrasilAPI)
- **HTML, CSS e JavaScript** (frontend para exibição dos dados)

## 📌 Funcionalidades
- Consulta informações de um CEP digitado.
- Retorna detalhes do endereço (rua, bairro, cidade, estado e IBGE).
- Obtém o código IBGE e exibe o nome do município.
- Busca o DDD e exibe a lista de cidades associadas.

## 📂 Estrutura do Projeto
```
/
│-- app.py               # Backend Flask
│-- templates/
│   ├── index.html       # Interface HTML do projeto
│-- static/
│   ├── style.css        # Estilos CSS (caso necessário)
│-- requirements.txt     # Dependências do projeto
│-- README.md            # Documentação do projeto
```

## 🔧 Instalação e Execução
### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2️⃣ Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3️⃣ Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o Backend (Flask)
```bash
python app.py
```
A API será iniciada em `http://127.0.0.1:5500/`.

### 5️⃣ Acessar o Frontend
Abra o arquivo `index.html` no navegador ou configure um servidor local para rodar a aplicação corretamente.

## 📡 Endpoints Disponíveis
### `GET /dashboard/<cep>`
Retorna informações sobre um CEP específico.

📌 **Exemplo de Requisição:**
```bash
curl http://127.0.0.1:5500/dashboard/01001000
```

📌 **Resposta Exemplo:**
```json
{
  "cep": {
    "cep": "01001-000",
    "state": "SP",
    "city": "São Paulo",
    "neighborhood": "Sé",
    "street": "Praça da Sé",
    "ibge": "3550308",
    "ddd": "11"
  },
  "ibge": {
    "nome": "São Paulo",
    "codigo_ibge": "3550308",
    "estado": "SP"
  },
  "ddd": {
    "state": "SP",
    "cities": ["São Paulo", "Guarulhos", "Santo André"]
  }
}
```
![image](https://github.com/user-attachments/assets/dd26813a-2b94-48f7-b856-12fd74ba6a82)


## 📜 Licença
Este projeto está sob a licença MIT.

## 🎨 Interface do Usuário
A interface permite digitar um CEP e exibir os detalhes diretamente na página, organizados em cartões informativos.

- [Meu GitHub](https://github.com/Erick-Lim-Souza)
- [Meu Linkedin](https://www.linkedin.com/in/erick-souza-70404686/ "Meu LinKedin")
- [Meu perfil DIO.me](https://www.dio.me/users/erickdelimasouza "Meu perfil DIO.me")
- [Meu perfil Alura](https://cursos.alura.com.br/user/erickdelimasouza)
- [Meu perfil Rocketseat](https://app.rocketseat.com.br/me/ericksouza)

- E-mail: erick.devzone@gmail.com

## 🤝 Agradecimentos
Agradecimentos especiais à [BrasilAPI](https://brasilapi.com.br/) por fornecer os dados utilizados nesta API.

---
**Desenvolvido com dedicação e foco no aprendizado de tecnologias web.**
