# Pokemon-TCG-Collect

## Funcionalidades

- � Visualize informações detalhadas das cartas com dados do conjunto
- 📁 Crie seu inventário de cartas
- 🔍 Pesquise cartas por nome de conjunto e ID
- 📂 Cartas organizadas por sets
- ⚙️ Persistência automática do inventário (armazenamento em JSON)

## Tecnologias Utilizadas

- Python 3
- Flask (Framework Web)
- API Pokémon TCG
- HTML5/CSS3
- Biblioteca Requests

## Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/<seu-usuario>/pokemon-tcg-collection.git
   cd pokemon-tcg-collection
   
2. **Instale as dependências**
   ```bash
   pip install flask requests

3. Crie o diretório de recursos
   ```bash
   mkdir resources

4. Execute a aplicação
   ```bash
   python3 main.py

## Uso
1. Inicie a aplicação
   ```bash
   python3 main.py

2. Acesse a interface web Abra http://localhost:5000 no seu navegador.

      Guia da Interface:
    
     - Página Inicial: Selecione um conjunto e insira o ID da carta
     - Visualização de Carta: Veja os detalhes da carta e adicione à coleção
     - Inventário: Visualize as cartas organizadas por conjuntos
     - Visualização de Conjunto: Navegue por todas as cartas de um conjunto específico

## Estrutura do Projeto
   ```bash
   .
├── main.py                 # Lógica principal da aplicação
├── cardInfo.py             # Manipulação de dados das cartas e interações com a API
├── resources/              # Armazenamento do inventário (criado automaticamente)
│   └── cards_inventory.json
├── templates/              # Templates HTML
│   ├── card.html
│   ├── home.html
│   ├── profile.html
│   └── set_cards.html
```

## API Reference

Este projeto utiliza a API Pokémon TCG:

  - Endpoints de dados das cartas
  - Endpoints de informações dos conjuntos
  - Recursos de imagens

## Créditos

 - API Pokémon TCG: https://pokemontcg.io/
 - Pokémon e Pokémon TCG são marcas registradas da Nintendo/Creatures Inc./GAME FREAK inc.
