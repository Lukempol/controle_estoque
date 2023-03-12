#  TCC do curso Desenvolvimento Web Fullstack pela PUC-Minas

Para rodar o projeto localmente é preciso ter o git e o python instalados. 
Primeiro copiar o projeto via git

> git clone https://github.com/Lukempol/controle_estoque.git

Acesse a pasta do projeto
>cd controle_estoque

Crie o ambiente virtual com python
> python -m venv .venv

Ative o ambiente virtual no
Windows
> .venv/Scripts/Activate.ps1

Ative o ambiente virtual no Linux
>source .venv/bin/activate

Com o ambiente virtual ativado, vamos agora instalar todas as dependências do projeto

> pip install -r requirements.txt

Para rodar o projeto usamos o comando
> python manage.py runserver

Para rodar os testes
> python manage.py test
