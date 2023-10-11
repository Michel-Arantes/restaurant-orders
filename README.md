# Projeto Python Restaurant Orders! :plate_with_cutlery:
Projeto desenvolvido por mim durante o curso de Desenvolvimento Web na Trybe. Divulgado aqui como portfólio de aprendizado

# Sobre o projeto

O Restaurant Orders é uma aplicação back-end web desenvolvida em Python, que permite de maneira simples, gerar seus cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque

## Funcionalidades

- Importar dados de um arquivo CSV e realizar o mapeamento do prato do cardápio com sua respectiva receita, isto é, ingrediente e quantidade
- Gerar um cardápio de acordo com uma restrição alimentar
- Realizar o controle de estoque de ingredientes
- Gerar cardápios dinâmicos considerando restrições alimentares e disponibilidade em estoque

## Tecnologias e habilidades utilizadas
- Python
- Pytest
- -Manipulação de dados de arquivos CSV
- Praticar o conceito de Hashmaps através das estruturas de dados Dict e Set do Python.
- Praticar os conhecimentos de orientação a objetos
  
## Rodando o projeto localmente

Para rodar o projeto em sua máquina, abra seu terminal, crie um diretório no local de sua preferência com o comando `mkdir` e acesse o diretório criado com o comando `cd`:

```bash
mkdir meu-diretorio &&
cd meu-diretorio
```

Clone o projeto com o comando `git clone`:

```bash
git clone git@github.com:michelmix/restaurant-orders.git
```

Acesse o diretório do projeto com o comando `cd`:

```bash
cd tb-restaurant-orders
```

crie o ambiente virtual:
```bash
python3 -m venv .venv
```

Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

Instale as dependências no ambiente virtual:
```bash
python3 -m pip install -r dev-requirements.txt
```
