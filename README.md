# Flask-Motors

- Uma API, criada apenas para treinar habilidades com Python e Flask.

- Arquitetura desse projeto, foi baseada, usando conceitos de Factories e Blueprints

- Usa o ORM SQLAlchemy.

- Está configurado para trabalhar com o SGBD PostgreSQL.

- O Banco da dados está rodando em Docker.

- O gerenciamento de pacotes e dependencias do projeto, ficou por conta do Poetry.

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

### Testando

```Bash
pytest tests/ -v --fixtures
