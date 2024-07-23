# nemli-nemlerei-bot

Esse projeto contém um bot de discord capaz de fazer resumos de
conversas de canais em tópicos para fácil compreensão de pessoas que
não estavam presentes em tais conversas.

Como base do projeto, será usado este [template].

[template]: https://github.com/aadibhoyar/python-discord-bot-template

# dev

## Requisitos

Para rodar esse projeto você precisa pelo menos ter a versão 3.10 de
Python instalada e o gerenciador de pacotes [PDM].

[PDM]: https://pdm-project.org/en/latest/

## Gerenciamento do projeto

Instalar o projeto:

```
pdm install
```

Rodar testes:

```
pdm tests
```

Rodar linters:

```
pdm lint
```

Rodar linters + tests:

```
pdm check
```

Rodar formatador em todo código:

```
pdm format
```

## Executar projeto

Para rodar o projeto, após executado `pdm install`, você pode chamar:

```
pdm run nemli
```

Tenha certeza de ter exportado as variáveis de ambiente necessárias.

## Comandos extras

Para instalar novas dependências, digite:

```
pdm add <dependency>
```

Ou, caso seja uma dependencia de desenvolvimento, como
pytest/mypy/flake8, você pode usar usar:

```
pdm add --dev <dependency>
```
