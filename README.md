
# Monitoramento de Sites (Terminal)

Este é um projeto simples de monitoramento de URLs feito em Python. Ele permite que o usuário adicione, liste, monitore e remova sites por meio de uma interface no terminal.

## Funcionalidades Implementadas

- Adição de URLs para monitoramento  
- Listagem de URLs salvas  
- Verificação do status HTTP das URLs (online/offline)  
- Exclusão de URLs da lista  
- Barra de carregamento animada ao iniciar  
- Interface simples e amigável no terminal usando a biblioteca `rich`  
- Envio automático de email caso uma URL falhe 3 vezes consecutivas, com controle de intervalo mínimo entre envios (cooldown)  

As URLs monitoradas são armazenadas em um arquivo JSON chamado `site_urls.json`.

## Estrutura do Projeto

- `main.py` – Ponto de entrada da aplicação.  
- `interface.py` – Responsável por exibir mensagens, menus e a interface no terminal.  
- `monitor.py` – Manipula as funcionalidades de monitoramento, como adicionar e verificar URLs, envio de alertas.  
- `persistence.py` – Gerencia a leitura e escrita no arquivo JSON.  
- `site_urls.json` – Armazena as URLs monitoradas.  
- `email_config.py` (não incluído no repositório) – Configurações de email para envio de alertas.  

## Requisitos

- Python 3.10 ou superior  
- Biblioteca `rich` para os efeitos visuais no terminal  
- Biblioteca `requests` para verificar status HTTP  
- Biblioteca `smtplib` (padrão do Python) para envio de emails  

### Instalação das dependências

```bash
pip install rich requests
```

## Configuração do Email

Para enviar alertas por email, crie um arquivo `email_config.py` na raiz do projeto com o seguinte conteúdo:

```python
EMAIL_FROM = "seu_email@gmail.com"
EMAIL_PASSWORD = "sua_senha_de_app"
```

## Como usar

1. Execute o script principal:

```bash
python main.py
```

2. Use o menu para adicionar URLs, listar sites monitorados, verificar status, remover URLs, adicionar emails para receberem alertas ou encerrar a aplicação.  
3. Quando uma URL ficar offline por 3 verificações consecutivas, será enviado um email de alerta (se configurado).  


---

Desenvolvido por Arthur Palma 
