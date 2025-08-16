# PyThrone

PyThrone is a headless, modular content management system designed for creators who want full control over their digital kingdom. It empowers users to publish, manage, and structure content through a flexible API — no bloated dashboards, just clean endpoints and creative freedom.

## 🚀 Installation

```bash
git clone https://github.com/yourusername/PyThrone.git
cd PyThrone
pip install -r requirements.txt
```

## 🌟 Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The application will be available at `http://localhost:8000`

## 📚 API Endpoints

### Items API

#### Create a new item
```bash
curl -X POST "http://localhost:8000/items" \
     -H "Content-Type: application/json" \
     -d '{"name": "Sample Item", "description": "This is a sample item"}'
```

#### Get all items
```bash
curl -X GET "http://localhost:8000/items"
```

#### Get a specific item by ID
```bash
curl -X GET "http://localhost:8000/items/1"
```

### Other Endpoints

#### Root endpoint
```bash
curl -X GET "http://localhost:8000/"
```

#### Quiz endpoint (existing)
```bash
curl -X GET "http://localhost:8000/quiz"
```

## 🗄️ Database

The application uses SQLite as the database with SQLAlchemy ORM for managing items. The database file (`pythrone.db`) will be created automatically when you start the application.

### Item Model
- `id`: Integer (Primary Key)
- `name`: String (Required)
- `description`: Text (Optional)

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
