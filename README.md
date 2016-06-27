# Salvo o Angico - Mais Angico, Menos Concreto [salveoangico.com.br](salveoangico.com.br)

Não podemos permitir que mais um crime ambiental seja cometido em
nossa cidade! Várias árvores já foram derrubadas e outras centenas
estão sob ameaça de corte em nossas praças, tudo em nome da uma mobilidade
urbana. A luta pelo Angico não é só pela árvore em si, mas por toda
a história e memórias que ela, assim como todas as árvores carregam.
Este Angico, com quase 100 anos de idade, está repleto de memória...

Teresina já foi conhecida como "cidade verde", porém o que
temos percebido é o verde sendo substituída pelo cinza dos edifícios.
Estão despindo nossa cidade.

Não permita que isso aconteça! Não permita mais essa injustiça.

# Ferramentas utilizadas

## Back-end

* Python 2.7
* Flask
* SQLAlchemy

## Front-end

* Gulp
* Bower
* Foundation

# Como executar

## virtualenv

Recomenda-se utilizar virtualenv para rodar a aplicação. Para instala-la use:

```bash
$ sudo pip install virtualenv
```

Então inicie a virtualenv:

```bash
$ virtualenv env
$ source env/bin/activate
```

## Instalando dependencias

Para executar primeiramente é necessário instalar as dependencias relativas
ao back-end:

```bash
$ pip install -r requirements.txt
```

Com as dependencias do back-end instaladas, caso queira trabalhar nos arquivos
do front-end (JS e CSS) é necessário instalar o [NodeJS](https://nodejs.org)
além das ferramentas [Gulp](gulpjs.com) e [Bower](https://bower.io).

### Instalando Gulp e Bower

```bash
$ sudo npm install -g gulp-cli bower
```

### Instalando as dependencias do front-end

```bash
$ cd app/static
$ npm install && bower install
```

## Arquivo de configuração

Utilizamos `python-decouple` para acessar as configurações da aplicação,
portanto pode-se utilizar variáveis de ambiente, um arquivo `settings.ini`
ou `.env`.

Por padrão, há um arquivo `.env.template` na raiz da aplicação que pode
ser utilizado como base para configurar a aplicação. Utilizamos PostegresSQL
como SGBD, mas pode-se utilizar qualquer outro SGBD que o SQLAlchemy tenha
suporte apenas adicionando a URL para o banco no formato
`<driver>://<username>:<password>@<host>:<port>/<database>`.

## Executando a aplicação

Finalmente para executar a aplicação basta iniciar o script `run.py` na
raiz da aplicação:

```bash
$ python run.py
```

# Como contribuir

Você pode contribuir de várias maneiras, abrindo uma [issue](https://github.com/teresinahc/savetheangico/issues),
com correções de erros ortográficos, sugestões. Corrigindo bugs
ou novas features. Toda contribuição é bem-vinda :heart:.

Pull Requests são bem-vindos, porém utilize a PEP8 no código Python da
aplicação, utilize boas práticas e sempre mantenha o código limpo e
legível.

Um PR pode ser negado em caso de:

* Contribuição inútil
* Código mal organizado
* Identação errada
* Contribuição prejudicial

Em todo caso, estamos abertos a refatoração da contribuição em caso
de negação da mesma.

# Licença

* [MIT](./LICENSE.md)
