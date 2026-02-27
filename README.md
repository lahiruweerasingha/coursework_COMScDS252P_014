# Coursework – COMScDS252P_014
**Student:** Lahiru Weerasingha  
**Module:** Data Science Fundamentals  
**Python Version:** 3.14.0  
**Environment:** `env_ecommerce_analysis` (virtualenv)

---

## Submission Structure

```
coursework_[StudentID]/
├── question1_university_management_system/
│   ├── main.py
│   ├── person.py
│   ├── student.py
│   ├── faculty.py
│   ├── staff.py
│   ├── course.py
│   ├── department.py
│   └── README.md
│
├── question2_data_analysis/
│   ├── 1_scraper.py
│   ├── 2_data_cleaning.py
│   ├── 3_analysis.py
│   ├── 4_visualization.py
│   ├── 5_prediction.py
│   ├── data/
│   │   ├── raw_books_data.csv
│   │   └── cleaned_books_data.csv
│   └── visualizations/
│       ├── 1_histogram_price_distribution.png
│       ├── 2_boxplot_price_top5_categories_interactive.html
│       ├── 3_scatter_price_vs_rating_interactive.html
│       └── 4_bar_avg_rating_top8_categories.png
│
├── question3_ethics/
│   └── healthcare_ethics_report.pdf
│
├── technical_report.pdf
├── requirements.txt
└── README.md
```

---

## Question 1 – Object-Oriented Programming: University Management System

### Overview
A fully object-oriented University Management System demonstrating inheritance, encapsulation, polymorphism, and abstraction using Python 3.14.0.

### Class Structure
| File | Class | Description |
|---|---|---|
| `person.py` | `Person` | Base class with shared attributes and methods |
| `student.py` | `Student` | Extends Person; manages courses, grades, GPA |
| `faculty.py` | `Faculty` | Extends Person; represents academic staff |
| `staff.py` | `Staff` | Extends Person; represents administrative staff |
| `course.py` | `Course` | Manages enrollment and capacity |
| `department.py` | `Department` | Manages faculty and course lists |
| `main.py` | — | Demonstration script covering all requirements A–E |

### How to Run
```bash
cd question1_university_management_system
python main.py
```

### Key Features Demonstrated
- **Inheritance:** Student, Faculty, Staff all extend Person via `super().__init__()`
- **Encapsulation:** `_grades` private store, read-only `@property gpa`
- **Polymorphism:** `get_responsibilities()` overridden across all three subclasses
- **Validation:** Grade range (0.0–4.0), max 6 courses per semester enforced via `ValueError`

---

## Question 2 – Data Analysis: E-commerce Book Data

### Overview
A five-stage data pipeline scraping, cleaning, analysing, visualising, and modelling book data from [books.toscrape.com](http://books.toscrape.com).

### Pipeline Execution Order
Run each script in sequence from the `question2_data_analysis/` directory:

```bash
cd question2_data_analysis

# Stage A – Scrape raw data (takes ~10–15 mins due to polite delay)
python 1_scraper.py

# Stage B – Clean and preprocess
python 2_data_cleaning.py

# Stage C – Statistical analysis
python 3_analysis.py

# Stage D – Visualisations
python 4_visualization.py

# Stage E – Predictive modelling
python 5_prediction.py
```

### Script Summary
| Script | Purpose | Output |
|---|---|---|
| `1_scraper.py` | Scrapes 200 books across 10 pages | `data/raw_books_data.csv` |
| `2_data_cleaning.py` | Cleans prices, encodes ratings, creates derived columns | `data/cleaned_books_data.csv` |
| `3_analysis.py` | Descriptive + inferential statistics | Printed stats + summary CSVs |
| `4_visualization.py` | 4 charts (2 static PNG, 2 interactive HTML) | `visualizations/` |
| `5_prediction.py` | Linear Regression to predict price | R² score + MAE printed |

### Key Findings
- **200 books** scraped across 10 catalogue pages with zero missing values
- Mean price: **£34.80** | Std Dev: **£14.12** | Range: **£49.48**
- Pearson r = **0.017** (p = 0.810) — price and rating are uncorrelated
- t-test Fiction vs Non-Fiction: p = 0.077 — no significant price difference
- Regression R² = **−0.1849** — price is not linearly predictable from rating or category
- Category is a stronger pricing influence than rating

---

## Question 3 – Data Ethics: AI Ethics in Healthcare

### Overview
A written ethical analysis examining healthcare data privacy regulations (HIPAA, GDPR), algorithmic bias in medical AI, an ethical decision framework, and stakeholder impact analysis.

### File
```
question3_ethics/healthcare_ethics_report.pdf
```

### Key Topics Covered
- HIPAA vs GDPR comparison and anonymisation limitations
- Documented bias case: Obermeyer et al. (2019) risk-stratification algorithm
- 6-point ethical checklist for healthcare data scientists
- Right to explanation and model interpretability requirements
- Patient, provider, and developer stakeholder impact analysis
- Policy recommendation: mandatory pre-market algorithmic impact assessments

---

## Installation & Dependencies

### Create and activate virtual environment
```bash
python -m venv env_ecommerce_analysis

# Windows
env_ecommerce_analysis\Scripts\activate

# macOS / Linux
source env_ecommerce_analysis/bin/activate
```

### Install all dependencies
```bash
pip install -r requirements.txt
```

### requirements.txt contents
```
requests
beautifulsoup4
pandas
numpy
scipy
matplotlib
plotly
scikit-learn
```

---

## VS Code Configuration

Pylance import warnings for local modules are resolved via `.vscode/settings.json`:
```json
{
    "python.analysis.extraPaths": [
        "./question1_university_management_system",
        "./question2_data_analysis"
    ]
}
```
This does not affect code execution or submission structure.

---

## Notes
- Interactive visualisations (`.html` files) open directly in any web browser
- The scraper includes a **1–2 second randomised delay** between requests and **3-attempt retry logic** to respect server rate limits
- All scripts include `try-except` error handling and produce clear terminal output
- The negative R² in `5_prediction.py` is an honest and expected result — book prices on toscrape.com are randomly assigned regardless of rating or category

