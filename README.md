Análise Detalhada do Sistema de Doações para ONG
Este documento explica o funcionamento completo do sistema de gerenciamento de doações desenvolvido em Python puro, sem dependência de bibliotecas externas. O sistema foi projetado para atender às necessidades básicas de uma ONG, com foco na proteção de dados e geração de relatórios úteis.

1. Estrutura Geral do Sistema
O sistema possui quatro componentes principais:

Módulo de Armazenamento: Gerencia a persistência dos dados em arquivo JSON

Módulo de Backup: Cria cópias de segurança automáticas

Módulo de Cadastro: Implementa o fluxo de registro de doações

Módulo de Relatórios: Calcula e exibe estatísticas sobre as doações

2. Funcionamento Detalhado
2.1. Inicialização do Sistema
   
![carbon](https://github.com/user-attachments/assets/d7feada2-7bc5-42ea-bef3-1658817c5dfe)

Verifica e cria a pasta de backups se não existir

Define o arquivo principal de dados (doacoes.json)

2.2. Sistema de Backup

![carbon (1)](https://github.com/user-attachments/assets/f509dd32-7112-40bd-9f1e-993ee391935f)

Gera um nome único para cada backup usando timestamp

Copia o conteúdo integral do arquivo principal

Mantém histórico completo de alterações

2.3. Manipulação de Dados

![carbon (2)](https://github.com/user-attachments/assets/8ab7568b-495e-42f7-bc9c-8b077dfa4980)

carregar_dados() lê o arquivo JSON e trata casos de arquivo vazio/corrompido

salvar_dados() escreve os dados formatados e aciona o backup automaticamente

2.4. Ofuscação de Dados

![carbon (3)](https://github.com/user-attachments/assets/09274091-703a-49a5-bdce-2123e30e9e58)

Técnica básica de substituição de caracteres (não é criptografia segura)

Cada caractere é substituído pelo próximo na tabela ASCII

Objetivo: dificultar leitura casual dos dados sem bibliotecas externas

2.5. Cadastro de Doações

![carbon (4)](https://github.com/user-attachments/assets/9798b958-6d21-4991-9583-d7edf9d2f5ec)

Validações robustas para cada campo:

Nome não pode ser vazio

Idade deve ser número inteiro positivo

Valor deve ser número decimal positivo

Armazena data/hora exata do registro

Ofusca o nome antes do armazenamento

2.6. Sistema de Relatórios

![carbon (5)](https://github.com/user-attachments/assets/e0e42d3b-23ed-4b07-bbd5-d6fd29a7c211)

Calcula 8 métricas diferentes sobre os dados

Trata caso de lista vazia

Usa compreensão de listas para operações eficientes

3. Fluxo de Execução
Inicialização:

Verifica/Cria estrutura de diretórios

Carrega dados existentes (se houver)

Cadastro:

![deepseek_mermaid_20250514_ed746e](https://github.com/user-attachments/assets/59cd6dd5-029d-4375-b746-691738001f80)

![carbon (6)](https://github.com/user-attachments/assets/c3df167d-9b8f-4bf0-8967-43c545b1b894)

Relatórios:

Carrega todos os dados

Calcula estatísticas

Exibe resultados formatados

4. Considerações sobre Segurança e LGPD
Proteção de Dados:

Ofuscação básica de informações pessoais

Armazenamento local com controle de acesso via sistema operacional

Conformidade:

Coleta apenas dados necessários

Registro de data/hora para auditoria

Sistema de backups para recuperação

Limitações:

Ofuscação não substitui criptografia real

Não há controle de acesso ao sistema

Dados sensíveis permanecem no dispositivo local

5. Melhorias Possíveis
Segurança:

Adicionar senha de acesso

Implementar criptografia real com hashing

Funcionalidades:

Exportar relatórios para CSV

Filtrar doações por período

Cadastro de projetos específicos

Interface:

Desenvolver interface gráfica simples

Adicionar menus contextuais

Este sistema oferece uma base sólida para gestão de doações em ONGs pequenas, com cuidado básico com a proteção de dados e funcionalidades essenciais para acompanhamento das arrecadações.





