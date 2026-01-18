# Movie Reccomender
A nepali movie reccomender based on cosine similarity, between the casts,actor,directors,genre and description of the movie

This project offers two ways to interact with the application: as a **Streamlit Dashboard** or via a **FastAPI File Response** service.

## Getting Started

You can try out the API without setting anything up locally:

- **API Documentation & Endpoint**:https://nepali-movie-reccommender.onrender.com/docs
- **Interactive Live Preview**:https://nepali-movie-reccommender.onrender.com/

- Only ~900 movies are inside the table so will only work on some nepali  movies, available movies can be viewed from temp/movies_final.csv

## 🛠 Setup & Installation

Before running either version, install the necessary dependencies for your preferred entry point.

**To run via FastAPI:**
```bash
pip install -r api_server/requirements.txt
```
**To run via Streamlit;**
```Bash
pip install -r requirements.txt
```
## 🚀 How to Run

You can choose one of the two methods below. **Important:** Always stay at the project root level to execute these commands.

### Option 1: Run via FastAPI
Use this method if you want to access the app via a File Response hosted by the API.
```bash
# Must be run from the root directory
fastapi dev api_server/main.py
```


### Option 2: Run via Streamlit
```bash
# Must be run from the project directory
streamlit run app.py
```
📂 Project Structure

    api_server/: Contains the FastAPI backend logic and its specific requirements.txt.

    app.py: The main entry point for the Streamlit frontend.

    requirements.txt: Dependencies required specifically for the Streamlit application.

⚠️ Key Reminders

    Directory Level: Do not cd into the api_server folder to run the API. The fastapi dev command expects to be run from the root to correctly map the file paths.

    Dependencies: Ensure you have installed the correct requirements.txt corresponding to the method you choose to run.
