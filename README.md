# Lista-Fone

Sistema de Lista Telefônica visando abranger as principais funcionalidades do CRUD (Create, Read, Update, Delete) de contatos telefônicos.

## Funcionalidades: Análise de Requisitos

### Requisitos Funcionais:

- **RF01**: Criar contatos;
- **RF02**: Deletar contatos;
- **RF03**: Alterar contatos;
- **RF04**: Listar contatos de forma total;
- **RF05**: Filtro de contatos;
- **RF06**: Validação de telefones;

### Requisitos Não Funcionais:

- **RNF01**: Backup de contatos;
- **RNF02**: Categorias/grupos de contatos;
- **RNF03**: Campo de e-mail para enviar e-mails ao usuário;
- **RNF04**: Compartilhamento de contato (arquivo .vcard);
- **RNF05**: Foto de Perfil dos Contatos;
- **RNF06**: Contador de contatos;
- **RNF07**: Contatos mais acessados;
- **RNF08**: Contatos de emergência;
- **RNF09**: Perfil de usuário;
- **RNF10**: Contatos favoritos;

## Modelagem de Dados

```mermaid
classDiagram
    class Contato {
        +int id 
        +str nome
        +str telefone
        +str email
        +image foto_de_perfil
        +datetime data_criacao
        +datetime data_atualizacao
        +boolean favorito
        +boolean emergencia
        +str categoria
        +adicionar()
        +editar()
        +deletar()
        +listar()
    }
    
    note for Contato "Modelo principal do Projeto
    Validações:
    - Nome: 2-100 caracteres
    - Telefone: formato brasileiro
    - Email: formato válido"

    class Categoria {
        +int id
        +str nome
        +str cor
        +adicionar()
        +deletar()
        +editar()
        +listar()
    }

    note for Categoria "Cores em Hexadecimal
    "

    Contato <|-- Categoria
```

## Wireframes

Tela principal:

<img src="./docs/images/Tela Principal.png" alt = "Tela Principal da Aplicação"> 