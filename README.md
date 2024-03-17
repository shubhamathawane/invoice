# Django Invoice App

This is a Django application for managing invoices and invoice details.

## Installation

1. Clone this repository to your local machine:

```bash
git clone github.com/shubhamathawane/invoice
```

### 1. Navigate to the project directory:
```bash
cd main
```

### 2. Install the required dependencies:
```bash
pip install requirements.txt
```

## Usage
- make migrations
```bash
python manage.py makemigrations
```
- migrate
```bash
python manage.py migrate
```

- Run the Django development server:
```bash
python manage.py runserver
```

### Access the application in your web browser at http://localhost:8000/

#### API Endpoints
- /invoices/: Endpoint to view all invoices and create a new invoice.
- /invoices/<int:pk>/: Endpoint to view, update, or delete a specific invoice.
- /invoice/details/: Endpoint to view all invoice details and create a new invoice detail.
- /invoice/details/<int:pk>/: Endpoint to view, update, or delete a specific invoice detail.

## Directory Structure

```
main/
│
├── invoice/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
│
├── manage.py
└── README.md
```


