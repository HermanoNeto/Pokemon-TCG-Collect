# Pokemon-TCG-Collect

🇧🇷 [Português - Brasil](README.md)

## Features

- � View detailed card information with set details
- 📁 Create your card inventory
- 🔍 Search cards by set name and ID
- 📂 Cards organized by set
- ⚙️ Automatic inventory persistence (JSON storage)

## Technologies Used

- Python 3
- Flask (Web Framework)
- Pokémon TCG API
- HTML5/CSS3
- Requests library

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/pokemon-tcg-collection.git
   cd pokemon-tcg-collection
   
2. **Install dependencies**
   ```bash
   pip install flask requests

3. **Create resources directory**
   ```bash
   mkdir resources

4. **Run the application**
   ```bash
   python3 main.py

## Usage
1. **Start the application**
   ```bash
   python3 main.py

2. **Access the web interface**
   
   Open http://localhost:5000 in your browser

3. Interface Guide:

   - Home Page: Select a set and enter card ID
   - Card View: See card details and add to collection
   - Inventory: View cards organized by sets
  -  Set View: Browse all cards in a specific set

## Project Structure
   ```bash
  .
├── main.py                 # Main application logic
├── cardInfo.py             # Card data handling and API interactions
├── resources/              # Inventory storage (auto-created)
│   └── cards_inventory.json
├── templates/              # HTML templates
│   ├── card.html
│   ├── home.html
│   ├── profile.html
│   └── set_cards.html
```

## API Reference

**This project uses the Pokémon TCG API:**

   - Card data endpoints
   - Set information endpoints
   - Image resources

## Credits

- Pokémon TCG API: https://pokemontcg.io/
- Pokémon and Pokémon TCG are trademarks of Nintendo/Creatures Inc./GAME FREAK inc.
