# bolero-app
Sistema de peladas de futebol desenvolvido em python/django.

## Pré requisitos

- Python 3 instalado

## Instruções

Instalar o virtualenv usando:
```
python3 -m venv env
```

Ativar o virtualenv:
```
source env/bin/activate
```

Instalar as dependências do projeto:
```
pip install -r requirements.txt
```

Migrar o banco de dados local:
```
./manage.py migrate
```

Rodar o servidor local:
```
./manage.py runserver
```
