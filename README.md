<<<<<<< HEAD
# N8N-Restaurante-Front
# N8N-Restaurante-Front
# N8N-Restaurante-Front
# N8N-Restaurante-Front
# N8N-Restaurante-Front
=======
# FastAPI Restaurant App

This project is a FastAPI application designed to manage and display information about dishes ordered in a restaurant. It allows customers to submit their orders, including details such as quantity, prices, and observations, and presents this data on a user-friendly frontend.

## Project Structure

```
fastapi-restaurant-app
├── app
│   ├── main.py          # Entry point of the FastAPI application
│   ├── models.py        # Data models for the application
│   ├── schemas.py       # Pydantic schemas for request and response validation
│   ├── api
│   │   └── dishes.py    # API endpoints related to dishes
│   └── frontend
│       ├── index.html    # Main HTML file for the frontend
│       └── static
│           └── style.css  # CSS styles for the frontend
├── requirements.txt      # Project dependencies
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-restaurant-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   uvicorn app.main:app --reload
   ```

5. **Access the frontend:**
   Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

- Customers can submit their orders through the frontend interface.
- The application will validate the incoming data and store it appropriately.
- The ordered dishes, along with their details, will be displayed on the frontend.

## License

This project is licensed under the MIT License.
>>>>>>> master
