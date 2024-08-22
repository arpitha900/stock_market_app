# Stock Market App
## Description
Stock Market App is a Django-based web application that provides real-time stock market data, allows users to create and manage watchlists, and offers stock market insights. The application integrates TradingView charts for enhanced data visualization and includes user authentication features for a personalized experience.
## Features
- Real-time stock market data fetching
- User authentication (login, registration)
- Watchlist management
- Stock portfolio tracking
- Integration with TradingView charts
- User-friendly UI with responsive design

## Flowchart

 ## Technologies
- Django
- Python
- HTML/CSS
- JavaScript
- TradingView API
- Git & GitHub
## Installation
1. Clone the Repository : First, clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
##Set Up a Virtual Environment
python -m venv venv
venv\Scripts\activate
## Install Depedencies : pip install -r requirements.txt
## Configure Environment Variable
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=your_database_url
TRADINGVIEW_API_KEY=your_tradingview_api_key
Then python manage.py migrate
Run development server :  python manage.py runserver

Usage
•	Register: Create an account using the registration page.
•	Login: Access your account using the login page.
•	Manage Watchlist: Add or remove stocks from your watchlist.
•	Track Portfolio: View and manage your stock portfolio.
•	View Stock Data: Get real-time stock data and charts.
Contributing
1.	Fork the repository.
2.	Create a new branch (git checkout -b feature/your-feature).
3.	Make your changes.
4.	Commit your changes (git commit -am 'Add some feature').
5.	Push to the branch (git push origin feature/your-feature).
6.	Create a new Pull Request.

