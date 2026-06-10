# Projeto com CI 

Projeto EM Python para demonstrar como criar funções, testá-las localmente e usar o GitHub Actions para automação.

## Como executar

1. Certifique-se de ter o **Python 3.12** instalado no seu computador.
2. Abra o terminal (ou prompt de comando) na pasta do projeto.
3. Instale as dependências necessárias executando:
   ```bash
   pip install -r requirements.txt

## Como rodar os testes
Para verificar se as funções estão funcionando na sua máquina, mude para a pasta do projeto no terminal e digite:

   ```bash
   pytest --verbose
   ```
Você verá uma mensagem verde mostrando que os testes passaram (PASSED).

## Como funciona o pipeline criado
Toda vez que você faz um git push (envia código para o GitHub) ou abre um Pull Request:

1. O GitHub Actions ativa um computador virtual com Linux (Ubuntu).

2. Ele baixa o código do seu projeto atualizado.

3. Instala a versão correta do Python (3.12).

4. Instala o pacote pytest indicado no requirements.txt.

5. Executa o comando pytest --verbose.

Se todos os testes passarem, o GitHub mostra um sinal verde ✓. Se algo quebrar, ele avisa com um ✗ vermelho!

# Importante
O comando:
   ```bash
   pytest --verbose
   ```
Só funciona em linux, mac ou wsl.
Para o windows:
 ```bash
   python -m pytest
   ```