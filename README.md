# MeteoDesk

MeteoDesk is a Web-Based System for production of weather bulletins and forecasts.

`NOTE:` The purpose of this repo is to provide a guide on how to develop Django/Wagtail applications that can be run as
standalone or integrated into larger projets, like https://github.com/wmo-raf/climweb

## Installation as Standalone System

1. Clone the repository:
   ```bash
   git clone https://github.com/wmo-raf/meteodesk
   cd meteodesk
    ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```

4. Install the required packages:
   ```bash
   pip install -r meteodesk/requirements/standalone.txt
   ```

5. Install the meteodesk package:
   ```bash
    pip install -e meteodesk
    ```
6. Create `.env` file:
   ```bash
   cp .env.sample .env
   ```

7. Edit the `.env` file to set your environment variables. Current for development we only need one variable:
   ```env
   DATABASE_URL=postgis://postgres:postgres@localhost:5432/meteodesk
   ```
   Ensure that the database meteodesk exists in your PostgreSQL server.

8. Run the migrations to set up the database:
   ```bash
   meteodesk migrate
   ```
   `meteodesk` is a command line tool that comes with the package. This is a shortcut for running `python manage.py`
9. Create a superuser account:
   ```bash
   meteodesk createsuperuser
   ```

10. Run the development server:
    ```bash
    meteodesk runserver 8000
    ```

11. Open your web browser and go to `http://localhost:8000` to access the MeteoDesk application.

The application directly opens to the Administration interface, where you can log in with the superuser account you
created.

12. Start developing the application as needed.

