
# Monitoramento de Sites (Terminal)

Este é um projeto simples de monitoramento de URLs feito em Python. Ele permite que o usuário adicione, liste, monitore e remova sites por meio de uma interface no terminal.

## Funcionalidades implementadas

- Adição de URLs para monitoramento
- Listagem de URLs salvas
- Verificação do status HTTP das URLs (online/offline)
- Exclusão de URLs da lista
- Barra de carregamento animada ao iniciar
- Interface simples e amigável no terminal com `rich`

As URLs são armazenadas em um arquivo JSON chamado `site_urls.json`.

## Estrutura do Projeto

- `main.py` – Ponto de entrada da aplicação.
- `interface.py` – Responsável por exibir mensagens, menus e a interface no terminal.
- `monitor.py` – Manipula as funcionalidades de monitoramento, como adicionar e verificar URLs.
- `site_urls.json` – Arquivo onde são salvas as URLs monitoradas.
- `persistence.py` – Gerencia a leitura e escrita no arquivo JSON.

## Requisitos

- Python 3.10+
- Biblioteca `rich` para os efeitos visuais no terminal

Instale com:

```bash
pip install rich
```

## Melhorias planejadas

- Envio de email automático caso uma URL falhe 3 vezes consecutivas.
- Parametrização do tempo entre as verificações.
- Interface mais elaborada com filtros e relatórios.

---

Desenvolvido por Arthur Palma – Projeto em andamento 🚧
