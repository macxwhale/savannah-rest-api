
# Savannah REST API

This is a Django service using Django REST Framework for creating a RESTful API. It uses **django-oauth-toolkit** for OpenID authentication and integrates features for handling customers and orders. The project is designed to allow seamless API interaction while providing authentication and notification services.

## Features:

- RESTful API with **Django REST Framework**
- **OpenID Connect** authentication using **django-oauth-toolkit**
- **Africa's Talking** SMS Gateway integration
- PostgreSQL for production database
- Unit tests with coverage
- CI/CD setup with GitHub Actions

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [API Documentation](#api-documentation)
4. [Environment Variables](#environment-variables)
5. [Features](#features)
6. [Contributing](#contributing)
7. [License](#license)

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL for production environments
- Virtual environment setup using `virtualenv`

### Clone the repository

```bash
git clone https://github.com/macxwhale/savannah-rest-api.git
cd savannah-rest-api
```

### Virtual Environment Setup

#### Linux/MacOS

1. Install virtualenv if you don’t have it:
   ```bash
   pip install virtualenv
   ```

2. Create a virtual environment:
   ```bash
   virtualenv env
   ```

3. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```

#### Windows

1. Install virtualenv if you don’t have it:
   ```bash
   pip install virtualenv
   ```

2. Create a virtual environment:
   ```bash
   virtualenv env
   ```

3. Activate the virtual environment:
   ```bash
   .\env\Scripts\activate
   ```

### Install dependencies

After activating your virtual environment, install the necessary packages:
```bash
pip install -r requirements.txt
```

### Apply database migrations

```bash
python manage.py migrate
```

### Run the application

```bash
python manage.py runserver
```

### Running Tests

To run the tests and check coverage:

```bash
python manage.py test
```

## API Documentation

For full API documentation, please refer to [API Docs](https://documenter.getpostman.com/view/8710618/2sAXqqcNSa).

## Environment Variables

The following environment variables need to be set in the `.env` file or directly in your environment:

- `PROD_DB_NAME`
- `PROD_DB_USER`
- `PROD_DB_PASSWORD`
- `PROD_DB_HOST`
- `PROD_DB_PORT`
- `AT_API_KEY`
- `AT_SENDER_ID`
- `AT_USERNAME`

### Example `.env` file:

```env
PROD_DB_NAME=your_db_name
PROD_DB_USER=your_db_user
PROD_DB_PASSWORD=your_db_password
PROD_DB_HOST=your_db_host
PROD_DB_PORT=5432
AT_API_KEY=your_africa_talking_api_key
AT_SENDER_ID=your_africa_talking_sender_id
AT_USERNAME=your_africa_talking_username
```

## Features

- **Authentication**: OAuth2-based OpenID Connect support via django-oauth-toolkit.
- **Django REST Framework**: A robust framework for building APIs.
- **SMS Integration**: Sends notifications to customers via Africa's Talking SMS Gateway.
- **Database**: Uses PostgreSQL in production environments.
- **Testing**: Unit tests with coverage for all functionalities.
- **CI/CD**: Integrated with GitHub Actions for continuous integration and deployment.

## Contributing

Contributions are welcome! Please follow the guidelines below:

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
