# IoC Pain Score Tool

A tool that takes various Indicators of Compromise (IoCs)—including hash values, IP addresses, domain names, host artifacts, network artifacts, and TTPs—and assigns each a "pain score" based on its position in the Pyramid of Pain. This score helps prioritize alerts in a SOC environment by highlighting which IoCs represent the highest difficulty for an adversary to change.

## Key Features
- **IoC Categorization:**  
  Ingest IoCs (via user input or threat feeds) and classify them into categories such as:
  - **Trivial:** Hash values  
  - **Easy:** IP addresses  
  - **Simple:** Domain names  
  - **Annoying:** Host artifacts  
  - *(Additional categories as needed)*
- **Pain Scoring Engine:**  
  Assigns a numerical "pain score" to each IoC based on predefined weights (the higher the score, the more painful it is for an adversary to change).
- **Visualization Dashboard:**  
  A simple web interface displays the prioritized list of IoCs alongside visual charts (using Chart.js) to facilitate rapid assessment.
- **Reporting & Alerts (Future Enhancement):**  
  Optionally, generate reports or trigger alerts based on cumulative pain scores.

## Technologies Used
- **Backend:** Python with Flask for data processing and scoring.
- **Frontend:** HTML/CSS with Chart.js for visualization.
- **Data Integration:** Uses sample JSON files (with potential future integration to threat feeds/APIs like VirusTotal).

## Installation & Setup

### Prerequisites
- Python 3.6+ and pip  
- Node.js (v12+ recommended)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Barrosleo/ioc-pain-score-tool.git
   cd ioc-pain-score-tool
   ```
2.  **Setup the Python Backend:**

  ```
  cd backend
  pip install -r requirements.txt
  python app.py
  ```
  This starts the backend Flask server on http://localhost:5000.
  
3.  **Launch the Frontend Dashboard:**
  In a separate terminal (or your favorite static server), serve the files in the frontend directory. For a quick test, you can simply open frontend/index.html in your browser.

##  Usage
- **The backend loads sample IoCs from backend/sample_data/iocs.json and calculates a pain score based on their type.**

- **The API endpoint /api/iocs returns the processed IoC data.**

- **The frontend dashboard (served by index.html) fetches this data and visualizes it as a bar chart.**

## Project Structure
```
ioc-pain-score-tool/
├── README.md
├── .gitignore
├── docs/
│   └── architecture.md
├── backend/
│   ├── app.py
│   ├── ioc_processor.py
│   ├── requirements.txt
│   └── sample_data/
│         └── iocs.json
└── frontend/
    ├── index.html
    ├── script.js
    └── style.css
```
## Future Enhancements

- **Integrate with live threat feeds (e.g., VirusTotal, MISP).**

- **Add user input forms for ad-hoc IoC uploads.**

- **Automate report generation and alerting based on cumulative pain scores.**

## License

This project is licensed under the MIT License.

