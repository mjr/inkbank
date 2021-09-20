# Inkbank

Sistema bancário.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.9+.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute o projeto.

```console
git clone https://github.com/mjr/inkbank.git wikb
cd wikb
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py runserver
```
