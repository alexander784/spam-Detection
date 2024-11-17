import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


#data frame
# Read the data
data = pd.read_csv('/home/alexander/machine/spam/spam.csv')
# Remove duplicates
data.drop_duplicates(inplace=True)
data['Category'] = data['Category'].replace(['han','spam'],['Not Spam','Spam'])


# Categorize the data
mess = data ['Message']
cat = data['Category']


# Split thre data
(mess_train,mess_test,cat_train,cat_test) = train_test_split(mess, cat,test_size=0.2)


cv = CountVectorizer(stop_words='english')
features = cv.fit_transform(mess_train)

##Create model
model = MultinomialNB()
model.fit(features, cat_train)

# Test model
features_test = cv.transform(mess_test)

print(model.score(features_test,cat_test))

# Predict the data
def predict(message):
    input_message = cv.transform([message]).toarray()
    result = model.predict(input_message)
    return result

output = predict('Congratulation you won a lottery')
print(output)






