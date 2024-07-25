import pytest
from nltk import download as nltk_download


# This fixture insures that nltk is downloaded before running tests, avoiding setup errors
@pytest.fixture()
def setup_nltk_stopwords():
    nltk_download("punkt")
    nltk_download("stopwords")


@pytest.fixture
def bot_summary_example():
    return """\
# Resumo das últimas 100 mensagens
### Assuntos discutidos:

1. **CI/CD e Gitflow**
   - **foo** e **bar** discutem a implementação de CI/CD, com
     **foo** mencionando que o Gitflow parece conveniente e que
     ainda há muito a ser feito nessa área.
   - **bar** sugere que a ideia de ter uma branch de desenvolvimento
     permanente pode facilitar os testes.

2. **Github Actions vs. Gitlab**
   - **foo** expressa preferência pelo Gitlab em relação ao Github,
     especialmente em relação a ações manuais e a configuração de
     pipelines.
   - **bar** menciona que o Github Actions existe, mas **foo** não
     encontrou informações sobre isso.

3. **Uso de Husky e Hooks do Git**
   - **bar** fala sobre o uso de Husky para hooks de pré-commit e
     pré-push, e como isso ajuda a automatizar processos de commit.
   - **foo** questiona o funcionamento do Husky e expressa
     descontentamento com a ferramenta "pre-commit".

4. **Desenvolvimento do Bot**
   - **foo** menciona que o bot está em desenvolvimento e que a
     situação atual é complicada devido à falta de um túnel SSH
     estável.
   - **bar** fala sobre a estrutura do projeto, que é bem elaborada e
     modular.

5. **Publicação e Testes**
   - **foo** compartilha um link para uma nova versão publicada no
     PyPI e discute a remoção de stopwords em um contexto de teste.
   - **linus** faz uma piada sobre a situação e menciona que vai
     testar uma frase relacionada.

6. **Experiências Pessoais com Ferramentas**
   - **foo** compartilha experiências negativas com ferramentas de
     pre-commit e comenta sobre sua abordagem de usar Makefile para
     setup de projetos.
   - **bar** defende o uso do Husky, afirmando que reduz a
     necessidade de hotfixes e melhora a qualidade do código.

### Participantes:
- **foo**
- **bar**
- **linus**
"""
