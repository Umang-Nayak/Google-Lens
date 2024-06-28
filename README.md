# Google Lens <img src="https://lh3.googleusercontent.com/H65Hxq0ooUCcwhoRGU-fwoXqrGS58mwa2vtr2ZfhGgJzMU0uYybOrZVBs8jydtR22TRC1k9XwDMD2xHB5BBU4IyXW7oH8PyCsq46uX6A42CmXP5GDZ2d" alt="Google Gemini" width="100"/>

## Introduction
This project demonstrates the usage of the Google Lense.
To use the google lense functionality, you need API of third party app called "serpapi".
You can get API by doing Sign Up at : https://serpapi.com/
Follow the steps below to set up and run the program.


## Steps to Setup and Run the Program

### Step 1: Clone the Repository
Clone the repository using the following command:
```bash
git clone https://github.com/Umang-Nayak/Google-Lense.git
```

### Step 2: Install Requirements
Navigate to the cloned directory and install the required dependencies from the requirements.txt file:
```bash
pip install -r requirements.txt
```

### Step 3: Setup API Key
Enter your SERP_API_KEY key in the ".env" file. 
The ".env" file should contain the following line:
```bash
SERP_API_KEY="Enter API Key Here"
```

### Step 4: Run The Program
Run the program using the Streamlit command in your terminal:
```bash
streamlit run main_ui.py
```
