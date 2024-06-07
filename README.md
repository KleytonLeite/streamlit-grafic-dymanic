# Streamlit Project

Este projeto é um template para um projeto Python utilizando Streamlit para gerar gráficos a partir de arquivos CSV ou Excel enviados.

## Link de uma versão online

```bash
https://streamlit-grafic-dymanic-1.onrender.com/
```

## Executando o Projeto Localmente

### Pré-requisitos

- Python 3.8 ou superior
- Virtualenv

### Passos para Configurar e Executar

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/KleytonLeite/streamlit-grafic-dymanic.git
    cd streamlit_dynamic
    ```

2. **Crie um ambiente virtual**:

    ```bash
    python -m venv venv
    ```

3. **Ative o ambiente virtual**:

    - No Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - No macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Execute a aplicação**:

    ```bash
    streamlit run streamlit_app/app.py
    ```

6. **Acesse a aplicação**:

    Abra o navegador e acesse `http://localhost:8501`.

## Fazendo o Deploy no Render

### Passos para Configurar o Deploy

1. **Crie uma conta no Render**:
    - Acesse [Render](https://render.com) e crie uma conta gratuita.

2. **Crie um Novo Serviço Web**:
    - No painel do Render, clique em "New" e depois em "Web Service".
    - Conecte seu repositório GitHub ou GitLab ao Render.
    - Selecione o repositório onde está sua aplicação Streamlit.

3. **Configure o Serviço**:
    - **Environment**: Docker
    - **Build Command**: (deixe em branco, pois o Dockerfile será usado)
    - **Start Command**: `bash start.sh`

4. **Deploy Automático**:
    - Cada vez que você fizer um push para o branch principal do repositório (geralmente `main`), o Render irá automaticamente fazer o deploy da aplicação.

### Estrutura do Projeto no Render

Certifique-se de que a estrutura do projeto está organizada corretamente:

### Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### Acessar a Aplicação no Render

Após o deploy ser concluído, você receberá um URL do Render onde sua aplicação estará hospedada. Acesse essa URL para verificar se a aplicação está rodando corretamente.

## Resumo

Este projeto permite a criação de gráficos dinâmicos utilizando Streamlit e suporta upload de arquivos CSV ou Excel. Você pode executar a aplicação localmente ou fazer o deploy no Render utilizando Docker. Siga os passos descritos para configurar e executar a aplicação corretamente.






