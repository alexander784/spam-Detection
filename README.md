## Spam Detection System with Naive Bayes 

<p> This is a Spam Detection System built with Python, Streamlit, and machine learning techniques.It classifies messages as either "Spam" or "Not Spam" using a Naive model trained on preprocessed dataset. </p>

## Features

* Data Preprocessing: CLeans and deduplicates a dataset of messages for training.
* Naive Bayes Model: Utilizes the MUltinomial Naive Nayes algorithm for classification.
* Streamlit interface: Provides a user friendly interface for testing message classifications.
* Real-time Predictions:Classified messages entered by the user as "Spam" or "Not spam"

## Technologies Used

* Python: Main Programming tool.
* Pandas: for data manipulation and preprocessing.
* Scilit -learn: For vectorization(CountVectorizer) and Naive Bayes classification.

* Sreamlit: For building an interactive web-based interface.

## Installation.
1. Clone the Repo: <br/>
  ``git clone https://github.com/alexander784/spam-Detection.git ``<br/>
  ``cd spam-Detection``<br/>

2. Install dependecies:<br/>
  `` pip install -r requirements.txt``

3. Run the app:

   ``streamlit run SpamDetection.py``

## Workflow
1. Load and Clean Data:
   * Reads the dataset from a CSV file.
   * Removes duplicates and standardizes labels.

2. Feature Engineering:
    * Uses COunt Vectorizer to convert text into numerical features.
3. Model Training:
    * Splits the data into training and testing sets.
    * Trains a Multinomial Naive model on the training data.

4. User input:
    * Users can input message through the Streamlit interface to classify it as "SPam" or "NOt spam."


## Usage
  1. OPen the app in your favorite browser after running the Streamlit server.
  2. Enter message in the input field.
  3. CLick the "validate" Button to chack if the message is spam or not spam.

## Accuracy:
The model achieves an accuracy of approximately 98% on the test dataset.

## Future Improvements:
* Enhance the model with additional preprocessing (eg,stemming, lemmatization)

* Explore other algorithms: Logistic Regression or SVM for better performance.

* Add a feature to visualize the dataset and predictions.

## License
This project is licensed under the MIT License.

## Author:
Developed By Alexander.For inquiries or suggestions, feel free to reach out at ga.nyaga7@gmail.com




