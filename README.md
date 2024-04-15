# Api para consulta de bancos

Api para consulta de bancos utilizando django e mysql

## Installation


```bash
git clone https://github.com/viniciusdvieira/rvgasapi.git
```
```bash
pip install -r requirements.txt
```
## Usage

```bash
python manage.py runserver
```
http://127.0.0.1:8000/ cole no navegador para abrir o HTML responsável pela utilização da api
## Endpoints
GET: http://127.0.0.1:8000/bancos mostra todos os bancos listados  
GET: http://127.0.0.1:8000/bancos/ (codigo de compensação) apresenta o banco em especifico com base no código de compensação
