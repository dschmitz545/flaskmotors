# Flask Motors

![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue?style=flat-square)

- A RestFul API, created just for training Python and Flask skills.

- The architecture of this project was based, using concepts from Factories and Blueprints

- As an ORM, it uses SQLAlchemy.

- Is configured to work with PostgreSQL Database

- The database is running on Docker.

- The management of packages and project dependencies was done by Poetry

## Essa API foi desenvolvida pensando no seguinte caso de uso

- Possibilitar a abertura de uma Orçamento/Ordem de Serviço, voltado para o segmento de Pós-vendas para uma concessionária de veículos.

- Nessa ordem de serviço, será possível informar, o cliente, dados do seu veículo, peças e serviços utilizandos para execução desta ordem de serviço.

### Como rodar

```Bash
Poetry Shell
```

```Bash
Poetry install
```

```Bash
export FLASK_APP=flaskmotors/app.py
```

```Bash
flask create-db
```

```Bash
flask migrate
```

```Bash
flask run
```
