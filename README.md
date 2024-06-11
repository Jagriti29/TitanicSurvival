
# Titanic Survival Analysis

This repository contains a Jupyter notebook for analyzing the Titanic dataset to predict the survival of passengers based on various features.



## Contents

- `titanic.ipynb`: Jupyter notebook containing the analysis and predictive modeling.
- `Titanic-Dataset.csv`: CSV file containing the Titanic passenger data
- `titanic_model.pkl` : The pre-trained machine learning model saved as a pickle file 
- `app.py` : The main Streamlit application file for deploying the model





## Getting Started
### Prerequisites
To run this application, you need to have the following installed:

- Python 3.6 or higher
- Streamlit
- Pandas
- Matplotlib
- Scikit-learn



## Installation
1. Clone the repository

```bash
git clone https://github.com/Jagriti29/TitanicSurvival.git
cd TitanicSurvival
```
2. Install the required packages


## Running the Application
To run the Streamlit app, execute the following command in your terminal:

```bash
streamlit run app.py
```
This will start a local server and provide you with a URL to access the application in your web browser.
## Usage
 
1. Open the application in your web browser using the provided URL.
2. Enter the required passenger details in the sidebar.
3. Click on the "Predict" button to get the prediction on whether the passenger would have survived.


## Model

The model used in this application is a Random Forest classifier trained on the Titanic dataset. The training process, including data preprocessing and feature engineering, is documented in the `titanic.ipynb` notebook.
## Dataset

The dataset used in this project is the well-known Titanic dataset. It includes features such as passenger class, sex, age, fare, and more. The dataset file is named `Titanic-Dataset.csv`.
## Contributing
Contributions are welcome! Please open an issue to discuss what you would like to change or add.
## Acknowledgments
- The dataset is provided by Kaggle.
- Streamlit for providing an easy way to build and share web apps for machine learning models.
## Contact
For any questions or feedback, please feel free to contact me at jagritilahuriya@gmail.com.

Thank you for checking out the TitanicSurvival project! Your contributions and feedback are highly appreciated.
