# MRC_DJango

## Prerequisites

- Python 3.x
- pip
- Arduino IDE
- MySQL Server

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-repo/MRC_DJango.git
    cd MRC_DJango/mysite
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root of your project and add your database credentials:**

    ```env
    MYSQL_DATABASE=django
    MYSQL_USER=root
    MYSQL_PASSWORD=2023
    MYSQL_HOST=localhost
    MYSQL_PORT=3306
    ```

5. **Configure the database settings in [`mysite/settings.py`]( "/home/august/django_practice/api/mysite/mysite/settings.py"):**

    ```python
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("MYSQL_DATABASE"),
            "USER": os.getenv("MYSQL_USER"),
            "PASSWORD": os.getenv("MYSQL_PASSWORD"),
            "HOST": os.getenv("MYSQL_HOST"),
            "PORT": os.getenv("MYSQL_PORT"),
        }
    }
    ```

6. **Run the migrations:**

    ```sh
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

7. **Create a superuser for the Django admin:**

    ```sh
    python3 manage.py createsuperuser
    ```

8. **Start the Django development server:**

    ```sh
    python3 manage.py runserver
    ```

9. **Access the Django admin interface:**

    Open your browser and go to `http://localhost:8000/admin` and log in with the superuser credentials.

## Arduino Setup

1. **Connect your Arduino to your computer and open the Arduino IDE.**

2. **Open the [`arduino_side/arduino.ino`]( "/home/august/django_practice/api/arduino_side/arduino.ino") file in the Arduino IDE.**

3. **Upload the code to your Arduino.**

## Communication Process

### From Arduino to Django

1. **Arduino collects sensor data and sends it via HTTP POST requests to the Django API.**

2. **Django's API receives the data and stores it in the database.**

### Django API Endpoints

- **BlogPost API:**
  - `GET /api/blogposts/` - List all blog posts
  - `POST /api/blogposts/` - Create a new blog post
  - `GET /api/blogposts/{id}/` - Retrieve a blog post
  - `PUT /api/blogposts/{id}/` - Update a blog post
  - `DELETE /api/blogposts/{id}/` - Delete a blog post

- **Sensors API:**
  - `GET /api/sensors/` - List all sensors
  - `POST /api/sensors/` - Create a new sensor
  - `GET /api/sensors/{id}/` - Retrieve a sensor
  - `PUT /api/sensors/{id}/` - Update a sensor
  - `DELETE /api/sensors/{id}/` - Delete a sensor

- **SensorData API:**
  - `GET /api/sensordata/` - List all sensor data
  - `POST /api/sensordata/` - Create new sensor data
  - `GET /api/sensordata/{id}/` - Retrieve sensor data
  - `PUT /api/sensordata/{id}/` - Update sensor data
  - `DELETE /api/sensordata/{id}/` - Delete sensor data

## Configuration

### Database Settings

The database settings are configured to use MySQL and are defined in [`mysite/settings.py`]("/home/august/django_practice/api/mysite/mysite/settings.py"):

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DATABASE"),
        "USER": os.getenv("MYSQL_USER"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),
        "HOST": os.getenv("MYSQL_HOST"),
        "PORT": os.getenv("MYSQL_PORT"),
    }
}