
- `features/`: Contains the feature files and step definitions for Behave.
  - `qa.feature`: A sample feature file.
- `pages/`: Page object models for the web application.
  - `qa_page.py`: Page object for the testing website
- `tests/`: Contains `pytest` test file.
  - `test_qa_challenge.py`: config file and needed for `pytest` run.
- `requirements.txt`: Requirements needed for this proj
- `README.md`: Project documentation.

## Setup

### Prerequisites
- Python 3.6+
- `pip` (Python package installer)
- Chrome browser (or any other browser you want to use with Selenium)
- Other Drivers if desired

### Install Dependencies
1. Download Pycharm:
    ```sh
    https://www.jetbrains.com/es-es/pycharm/download/
2. Clone the repository:
   ```sh
   git clone https://github.com/santonerodrigo/QA_behave_demo_rs.git
   cd your_project
3. Install requirements:
   ```sh
   pip install -r requirements.txt
4. Execute tests using behave command
    ```sh
    behave --junit 
