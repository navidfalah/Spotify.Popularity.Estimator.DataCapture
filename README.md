# Spotify Data Collector

## Overview
Spotify Data Collector is a robust project designed to fetch, process, and store data from Spotify. This project primarily focuses on retrieving data about top artists and songs as per Spotify's ratings, specifically targeting the top 100 artists of February 2023. It transforms the JSON data from Spotify into Python ORM to be stored efficiently in an SQLite database, utilizing Django and Django REST framework for its backend.

## Features
- **Data Collection:** Utilizes Spotify API to gather data about artists and songs, including the top 100 artists as chosen by Spotify in February 2023.
- **Data Transformation:** Converts JSON data into Python ORM objects for streamlined database interaction.
- **Database Storage:** Employs SQLite for its lightweight and efficient data storage capabilities, ideal for the scope of this project.
- **Extended API Integration:** Supports additional APIs to fetch more detailed data like song features and analytics.
- **Large Dataset:** Successfully cloned data for over 1000 songs, including their analysis and features as suggested by Spotify.
- **Django and Django REST Framework:** Uses Django for backend development and Django REST Framework for API interaction.
- **Custom Django Admin:** Enhanced Django admin interface for advanced search capabilities and exporting data to CSV.

## Getting Started

### Prerequisites
- Python 3.x
- SQLite
- A Spotify Developer account and an application created on it for API access.
- Django and Django REST Framework

### Installation and Setup
1. **Clone the repository:**
   ```
   git clone [repository link]
   ```
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
   Dependencies include:
   ```
   asgiref==3.7.2
   certifi==2023.7.22
   charset-normalizer==3.3.0
   Django==4.2.6
   djangorestframework==3.14.0
   idna==3.4
   pytz==2023.3.post1
   requests==2.31.0
   sqlparse==0.4.4
   typing_extensions==4.8.0
   tzdata==2023.3
   urllib3==2.0.6
   ```
3. **Setting up Spotify API:**
   - Create an application in your Spotify Developer account.
   - Retrieve the Client ID and Client Secret.
   - Update the configuration file with these credentials.

### Running the Application
To run the application, execute the following commands:
```
python manage.py
python makemigrations
python migrations
```

## Usage
The application will automatically connect to Spotify's API, fetch data as per the implemented models (Artists and Songs), and store this data in the SQLite database. Each artist and song has a specific Spotify ID, for example:
```json
artists = [
    {
        "name": "The Weeknd",
        "id": "1Xyo4u8uXC1ZmMpatF05PJ",
        "rank": 1
    },
    {
        "name": "Ed Sheeran",
        "id": "6eUKZXaKkcviH0Ku9w2n3V",
        "rank": 2
    }
]
```

## Contributing
Contributions to enhance Spotify Data Collector are welcome. Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the [MIT License](LICENSE.md).
