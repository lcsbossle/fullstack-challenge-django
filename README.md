# Teste para vaga de fullstack

## Instruções para rodar

### 1. Configuração do ambiente

Para rodar este projeto, recomendo ter instalado o virtualenvwrapper.
[Guia de Instalação](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

Também será necessário ter o MySQL (aqui está na versão 8.0.21).

Dentro do diretório do projeto:
```bash
$ mkvirtualenv -p /usr/python3 django3
$ workon django3
$ pip install -r requirements.txt
```

### 2. Configuração do MySQL
No shell do MySQL (root):
```sql
mysql> CREATE DATABASE memberarea CHARACTER SET utf8;
mysql> CREATE USER 'tradeclient'@'localhost' IDENTIFIED BY 'Y&U*y7u8';
mysql> GRANT ALL PRIVILEGES ON memberarea.* TO 'tradeclient'@'localhost';
mysql> FLUSH PRIVILEGES;

```

### 3. Configurando o Django

No diretório do projeto (no nível do arquivo manage.py).

Opcional: criar superuser
```bash
$ python manage.py create superuser
```
Migrar modelos para a base de dados:
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
Script para criar usuários, grupos de usuários e setar permissões (só irá funcionar da primeira vez - alterações seguintes deverão ser feitas pela página de admin):
```bash
$ python manage.py <scripts/set_users.py
```

### 4. Rodando o projeto
```bash
$ python manage.py runserver
```
O sistema estará disponível no [localhost](http://127.0.0.1:8000/).

O script set_users.py criou dois usuários com permissões diferentes:

  - Aluno
    - username: Aluno
    - password: alunosenha
  - Professor
    - username: Professor
    - password: profesenha

1. Fazer login como Professor;
2. Acessar "Criar aula" no menu lateral;
3. Preencher todos os campos (o campo "Conteúdo" será interpretado como Markdown e convertido para html na exibição da aula);
4. Criar mais de uma aula como teste;
5. Criar um curso e selecionar as aulas que deseja incluir no curso.
    - As aulas serão adicionadas na sequência em que forem selecionadas na caixa de seleção. A edição da ordem das aulas do curso é uma Feature para ser feita :)
6. Testar os CRUDs
7. Fazer login como "Aluno" e verificar se este só pode visualizar as aulas.

### 5. Fim

Este projeto foi desenvolvido com a finalidade de teste não deve ser considerado um produto final.

Dúvidas: lucas.lb2@gmail.com
