# Contact Book
A simple command-line Contact Book application in Python using SQLite for persistent storage.
## Features
- Add new contacts (name, phone, email, address)
- View all contacts
- Search contacts by name or phone number
- Update contact details
- Delete contacts
- All data is saved in a local `contacts.db` file
## Requirements
- Python 3.10 (with built-in `sqlite3` module)
## Setup & Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/hyprpranav/Codsoft_Task4.git
   cd Codsoft_Task4
   ```
2. Run the application:
   ```sh
   python Contactbook.py
   ```
3. Follow the menu prompts to manage your contacts.
## How It Works
- Contacts are stored in a SQLite database (`contacts.db`).
- The app creates the database and table automatically if they do not exist.
- All operations (add, view, search, update, delete) interact with the database for persistent storage.
## License
This project is open source and available under the MIT License.
