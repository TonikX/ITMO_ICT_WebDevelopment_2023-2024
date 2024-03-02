# Project "Warrior Management"

The "Warrior Management" project is a web application developed using the Django framework. This application is designed to manage information about warriors, their professions, and skills.

## Installation

1. Clone the repository:


2. Navigate to the project directory:


3. Create and activate a virtual environment:


4. Install dependencies:


5. Apply migrations:


## Usage

1. Run the development server:


2. Go to http://127.0.0.1:8000/ in your browser to access the "Warrior Management" web application.

## API Endpoints

- **GET /api/warriors/**: Get a list of all warriors.
- **POST /api/warriors/**: Create a new warrior.
- **GET /api/profession/create/**: Get a form for creating a new profession.
- **GET /api/warrior-with-profession/**: Get a list of warriors with their professions.
- **GET /api/warrior-with-skill/**: Get a list of warriors with their skills.
- **GET /api/warriors/<int:pk>/**: Get information about a specific warrior by their identifier.

## Author

- Al-Moshki Esmail <esmailalmoshki@gmail.com>


