
# Flask Application for Green energy Cloud

## Introduction
This Flask application serves as a Runs Greem Energy cloud models to feed data to service layer . It utilizes several Python libraries for web serving, data processing, and machine learning model interaction.

## Prerequisites
Before you start, ensure you have Python installed on your system (preferably Python 3.6 or above).

## Setting Up the Virtual Environment
To avoid conflicts with other Python projects or system-wide packages, it's recommended to use a virtual environment. Follow these steps to set it up:

1. Navigate to your project directory:
```bash
cd path/to/your/project
```

2. Create a virtual environment:
```bash
python3 -m venv venv
```
This command creates a virtual environment named `venv` within your project directory.

3. Activate the virtual environment:
- On Windows:
```bash
.\venv\Scripts\activate
```
- On Unix or MacOS:
```bash
source venv/bin/activate
```

## Installing Dependencies
With your virtual environment activated, install the required libraries by running:

```bash
pip install Flask sklearn pandas flask-cors
```

This command installs Flask for web serving, scikit-learn for preprocessing, pandas for data manipulation, and flask-cors for handling Cross-Origin Resource Sharing (CORS).

## Preparing `.pkl` Files
The application uses `.pkl` (Pickle) files to load pre-trained machine learning models or data. Ensure you place these `.pkl` files in a directory accessible by your Flask application, typically in the root or a subdirectory like `models/` or `data/`.

In your application code, when loading `.pkl` files, specify the correct path, for example:
```python
import pickle

# Example of loading a model
with open('models/your_model_filename.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
```

## Running the Application
To start your Flask application, run:

```bash
export FLASK_APP=your_application_script.py
export FLASK_ENV=development
flask run
```

Replace `your_application_script.py` with the name of your main Python script.

- `FLASK_APP` specifies the entry point of your application.
- `FLASK_ENV=development` enables development mode for more detailed error messages and automatic reloading.

Your application will be accessible at `http://127.0.0.1:5000/` by default.
