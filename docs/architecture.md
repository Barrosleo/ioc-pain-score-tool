# Architecture Overview

## System Components

1. **Backend (Python with Flask):**
   - **app.py:**  
     Initializes the Flask server and exposes the `/api/iocs` endpoint.
   - **ioc_processor.py:**  
     Loads sample IoCs from a JSON file, assigns a pain score based on their type, and returns the augmented data.
   - **Sample Data:**  
     The file `sample_data/iocs.json` contains raw IoC entries.

2. **Frontend (HTML/JavaScript with Chart.js):**
   - **index.html:**  
     Provides a basic interface and a canvas for rendering charts.
   - **script.js:**  
     Fetches processed IoC data from the Flask API and renders a bar chart to visualize pain scores.
   - **style.css:**  
     Contains simple styling for a clean dashboard display.

## Data Flow

1. The backend reads IoCs from `iocs.json`.
2. Each IoC is processed using a defined mapping that assigns a pain score.
3. The processed data is exposed via the `/api/iocs` API endpoint.
4. The frontend fetches the data and uses Chart.js to display a visual bar chart of IoCs versus their pain scores.
