# automacao-web-pratica-python

Projeto de prática de automação em Python usando **PyAutoGUI** para preencher automaticamente um formulário web a partir de dados em uma planilha CSV.

## O que o projeto faz

- Lê o arquivo `produtos.csv` com **pandas**.
- Abre o navegador (Chrome) via atalhos de teclado.
- Acessa a página de login da Hashtag Treinamentos.
- Faz login.
- Percorre cada linha da tabela e cadastra os produtos no formulário da página.

## Requisitos

- Python 3 instalado  
- Google Chrome instalado  
- Mesma resolução/posição de tela usada para gravar as coordenadas (para os `clicks` funcionarem)

## Instalação e uso

```bash
git clone https://github.com/dalessandrosantos/automacao-web-pratica-python.git
cd automacao-web-pratica-python

pip install pyautogui pandas
# ou: pip install -r requirements.txt  (se houver)

python main.py
```

Enquanto o script roda, não mexa no mouse nem no teclado.
