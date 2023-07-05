# Titanic Machine Learning Project
This project is a part of my machine learning portfolio and aims to predict the survival of passengers on the Titanic using the famous Titanic dataset.

## Dataset
The Titanic dataset is a well-known dataset that provides information about the passengers aboard the Titanic, including whether they survived or not. It consists of the following columns:

- Survived: Indicates if the passenger survived (1) or not (0).
- Pclass: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd).
- Sex: Gender of the passenger.
- Age: Age of the passenger.
- SibSp: Number of siblings/spouses aboard.
- Parch: Number of parents/children aboard.
- Fare: Fare paid for the ticket.
- Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).
The dataset is provided in the file titanic.csv.

## Project Structure
The project follows the following directory structure:
```
.
├── data/
│   └── titanic.csv
├── notebooks/
│   ├── data_exploration.ipynb
│   ├── data_preprocessing.ipynb
│   ├── feature_engineering.ipynb
│   └── model_training.ipynb
├── models/
│   └── titanic_model.pkl
├── README.md
└── requirements.txt
```
- data/: Contains the dataset file.
- notebooks/: Contains Jupyter notebooks for different stages of the project.
- models/: Stores the trained machine learning model.
- README.md: The file you're currently reading, providing an overview of the project.
- requirements.txt: Specifies the project dependencies.

## Setup and Dependencies
To run this project, you need to have the following dependencies installed:

- Python (3.11.4)
- pandas
- numpy
- scikit-learn
- seaborn
You can install the dependencies by running the following command:

`pip install -r requirements.txt`

## Usage
To reproduce the results of this project, follow these steps:

Clone this repository:

`git clone https://github.com/your-username/titanic-machine-learning.git`

Navigate to the project directory:

`cd titanic-machine-learning`

Install the project dependencies:

`pip install -r requirements.txt`

Open the Jupyter notebooks in the notebooks/ directory and execute them in the following order:

data_exploration.ipynb: Perform exploratory data analysis on the Titanic dataset.
data_preprocessing.ipynb: Preprocess the dataset by handling missing values and scaling features.
feature_engineering.ipynb: Create new features from existing ones.
model_training.ipynb: Train and evaluate machine learning models on the preprocessed dataset.
After running the model_training.ipynb notebook, the trained model will be saved in the models/ directory as titanic_model.pkl.

Feel free to explore the notebooks, modify the code, and experiment with different algorithms and feature engineering techniques.

Results
The final trained model achieves an accuracy of XX% on the test set. You can find the detailed analysis and evaluation in the model_training.ipynb notebook.