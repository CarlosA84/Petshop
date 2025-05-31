

PetShop Virtual

Definição do Problema

Em muitos pequenos negócios de pet shops, o gerenciamento de clientes, animais e serviços oferecidos ainda é feito manualmente, seja em papel ou em sistemas pouco eficientes. Isso pode gerar perda de informações, confusão no agendamento de serviços, e dificuldade em manter um histórico dos atendimentos realizados.

Este projeto busca resolver esses problemas criando uma aplicação simples e intuitiva para:

- Cadastrar clientes e seus respectivos animais de estimação.
- Registrar agendamentos de serviços como banho e tosa.
- Visualizar o histórico dos agendamentos e atendimentos realizados.
- Gerenciar os dados com segurança, salvando e carregando as informações localmente.

Funcionalidades / Casos de Uso

1. Cadastro de Clientes

   - Permite inserir novos clientes no sistema.
   - Validação do CPF (11 dígitos numéricos) e prevenção de duplicidade.
   - Resultado: cliente cadastrado e disponível para associação aos animais.

2. Cadastro de Animais

   - Registra animais associados aos clientes.
   - Informações: tipo (cachorro, gato, hamster), espécie, idade e dono.
   - Resultado: animais vinculados corretamente aos donos para agendamento.

3. Agendamento de Serviços

   - Cria agendamentos para os animais.
   - Seleção de cliente, animal, serviço(s) e data.
   - Resultado: agendamento confirmado e listado.

4. Histórico de Atendimentos

   - Exibe o histórico completo dos agendamentos.
   - Mostra cliente, animal, serviços realizados e data.
   - Resultado: histórico acessível para consulta.

5. Gerenciamento dos Dados

   - Salva e carrega dados localmente usando arquivos (pickle).
   - Permite limpar todos os dados salvos com confirmação.
   - Resultado: dados persistidos entre sessões, com opção de limpeza.

6. Interface Gráfica Amigável

   - Interface simples e clara usando Tkinter.
   - Navegação fácil entre cadastro, agendamento e histórico.

Tecnologias Utilizadas

- Python 3.x
- Tkinter para interface gráfica
- Pillow (PIL) para manipulação de imagens
- Módulo pickle para persistência local dos dados

Como Executar

1. Certifique-se de ter Python 3 instalado.

2. Instale a biblioteca Pillow (caso ainda não tenha):

   `pip install pillow`

3. abra a pasta Petshop e execute o programa:

   `python main.py`

