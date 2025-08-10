# Monitoramento de Sites (Terminal)

Este é um projeto simples de monitoramento de URLs feito em Python. Ele permite que o usuário adicione, liste, monitore e remova sites por meio de uma interface no terminal.

## Funcionalidades implementadas

- Adição de URLs para monitoramento
- Listagem de URLs salvas
- Verificação do status HTTP das URLs (online/offline)
- Exclusão de URLs da lista
- Barra de carregamento animada ao iniciar
- Interface simples e amigável no terminal com rich
- Envio de email automático caso uma URL falhe 3 vezes consecutivas (configuração necessária)
- Armazenamento das URLs em arquivo JSON chamado `site_urls.json`

## Estrutura do Projeto

- `main.py` – Ponto de entrada da aplicação.
- `interface.py` – Responsável por exibir mensagens, menus e a interface no terminal.
- `monitor.py` – Manipula as funcionalidades de monitoramento, como adicionar e verificar URLs.
- `persistence.py` – Gerencia a leitura e escrita no arquivo JSON.
- `site_urls.json` – Arquivo onde são salvas as URLs monitoradas.
- `test_server.py` – Um servidor Flask básico para testes de monitoramento. Permite simular um site online/offline localmente.

## Requisitos

- Python 3.10+
- Biblioteca `rich` para os efeitos visuais no terminal
- Biblioteca `requests` para as requisições HTTP
- Biblioteca `flask` para rodar o servidor de teste (opcional)

Instale as dependências com:

```bash
pip install rich requests flask
```

## Configuração de Email para Alertas

Para usar o envio automático de email quando um site falhar 3 vezes consecutivas, você deve criar um arquivo `email_config.py` na raiz do projeto com o seguinte conteúdo:

```python
EMAIL_FROM = "seu_email@gmail.com"
EMAIL_PASSWORD = "sua_senha"
EMAIL_TO = ["destinatario1@gmail.com", "destinatario2@gmail.com"]
```

> **Atenção:**  
> Nunca compartilhe seu arquivo `email_config.py` publicamente. Para evitar que ele seja enviado ao GitHub, inclua o nome dele no seu `.gitignore`.

## Instruções para Testes

Para facilitar os testes do monitoramento, foi criado o arquivo `test_server.py`, que roda um servidor Flask simples na porta 5000. Você pode iniciar esse servidor para simular um site online:

```bash
python test_server.py
```

- O servidor responderá com a mensagem `Servidor está online!` ao acessar `http://localhost:5000/`.
- Para testar o monitoramento, adicione a URL `http://localhost:5000` no seu aplicativo.
- Você pode parar o servidor para simular um site offline.

---

Desenvolvido por Arthur Palma – Projeto em andamento 🚧
