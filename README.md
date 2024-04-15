# Api para consulta de bancos

Api para consulta de bancos utilizando django e mysql

## Installation


```bash
git clone https://github.com/viniciusdvieira/rvgasapi.git
```
```bash
pip install -r requirements.txt
```
**Criação do Banco de Dados**: Crie um novo banco de dados para o seu projeto. Você pode fazer isso usando um cliente MySQL, como o MySQL Workbench, ou executando comandos SQL diretamente no terminal. Use as seguintes configurações para o banco de dados:

   - Nome do Banco de Dados: `api_banco`
   - Usuário: `bancoadm`
   - Senha: `banco123123@`
   - Host: `localhost`
   - Porta: `3306'  

execute o script para importar os dados do exel para o MYSQl:
```bash
python import_exel.py
```
depois é só dar o comando:
```bash
python manage.py migrate
```

## Usage

```bash
python manage.py runserver
```
http://127.0.0.1:8000/ cole no navegador para abrir o HTML responsável pela utilização da api
## Endpoints
GET: http://127.0.0.1:8000/bancos mostra todos os bancos listados  
GET: http://127.0.0.1:8000/bancos/(codigo de compensação) apresenta o banco em especifico com base no código de compensação
