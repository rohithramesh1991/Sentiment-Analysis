#amex_Card_add_click

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

train=pd.read_csv('drive/My Drive/DATA files/Website Add Clicks/train.csv')
test=pd.read_csv('drive/My Drive/DATA files/Website Add Clicks/test.csv')
hist=pd.read_csv('drive/My Drive/DATA files/Website Add Clicks/historical_user_logs.csv')

train_merged=pd.merge(train,hist[['user_id','product','action']],how='inner',on=['user_id','product'])

train_merged.info()

train_merged['DateTime']=pd.to_datetime(train_merged['DateTime'])
train_merged.info()

train_merged.isnull().sum(axis=0)

#drop few variables
train_merged.drop(['product_category_2','city_development_index'],axis=1,inplace=True)

train_merged.isnull().sum(axis=0)

train_merged.shape
train_merged.info()

train_merged.isnull().sum(axis=0)

train_merged.describe()

train_merged=train_merged[np.isfinite(train_merged["user_group_id"])]

train_merged.isnull().sum(axis=0)

train_merged.head()

# Commented out IPython magic to ensure Python compatibility.
#Exploratory Analysis
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline
sns.set_style('whitegrid')

# Creating a histogram of the Age column
#Let's use seaborn to explore the data
train_merged['age_level'].plot.hist(30)
plt.xlabel('Age_level')

test.info()

test['DateTime']=pd.to_datetime(test['DateTime'])
test.info()

#test merging with hist data
test_merged=pd.merge(test,hist[['user_id','product','action']],how='inner',on=['user_id','product'])
test_merged.info()

test_merged.isnull().sum(axis=0)

#remove missing vale
test_merged=test_merged[np.isfinite(test_merged['user_group_id'])]
test_merged.isnull().sum(axis=0)

#discretizing relevant columns
from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()
label_encoder.fit(train_merged['gender'].append(test_merged['gender'],ignore_index=True))
train_merged['gender']=label_encoder.transform(train_merged['gender'])
test_merged['gender']=label_encoder.transform(test_merged['gender'])

train_merged.describe()

#creating dummies for tain set on product variable
train_merged1 = pd.get_dummies(train_merged, columns=['product'])

train_merged1.head(2)

train_merged1.isnull().sum(axis=0)

#creating dummies for test set on product variable
test_merged1 = pd.get_dummies(test_merged, columns=['product'])

test_merged1.head(2)

#retaining only the columns that are required for both test and train data
train_merged1_columns=list(train_merged1.columns.values)
train_merged1_columns.remove('is_click')
train1=train_merged1[train_merged1_columns]
train1.head(2)

#only retain same columns as train_na data
test1=test_merged1[train_merged1_columns]
test1.head(2)

#discretizing relevant columns
from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()
label_encoder.fit(train1['action'].append(test1['action'],ignore_index=True))
train1['action']=label_encoder.transform(train1['action'])
test1['action']=label_encoder.transform(test1['action'])

train_merged1.info()

train1=train1.drop(['DateTime', 'user_depth', 'user_group_id','campaign_id'], axis=1)
test1=test1.drop(['DateTime', 'user_depth', 'user_group_id','campaign_id'], axis=1)

train1=train1.drop(['product_category_1'], axis=1)
test1=test1.drop(['product_category_1'], axis=1)

train1.info()

test1.info()

#train the model
from sklearn.model_selection import train_test_split, GridSearchCV

X_train,X_test,y_train,y_test=train_test_split(train1,train_merged1['is_click'],random_state=33)

#Feature Selection
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
FS = SelectKBest(score_func=chi2, k=10)
FS_fit = FS.fit(X_train,y_train)
# summarize scores
np.set_printoptions(precision=3)
print(FS_fit.scores_)

from sklearn.linear_model import LogisticRegression
lg_reg=LogisticRegression()
lg_reg.fit(X_train,y_train)
print('amex card data')
print('Accuracy of GBR classifier on the training set:{:.2f}'.format(lg_reg.score(X_train,y_train)))
print('Accuracy of GBR classifier on the test set:{:.2f}'.format(lg_reg.score(X_test,y_test)))
# The predict method just takes X_test as a parameter, which means it just takes the features to draw predictions
predict_click = lg_reg.predict(X_test)

y_test1=pd.DataFrame(y_test)
y_test1.head()

y_test1['pred_click']=predict_click
y_test1.head(100)

#Evaluation
# Importing classification_report from sklearn.metrics family
from sklearn.metrics import classification_report
# Printing classification_report to see the results
print(classification_report(y_test, predict_click))

# Importing a pure confusion matrix from sklearn.metrics family
from sklearn.metrics import confusion_matrix
# Printing the confusion_matrix
print(confusion_matrix(y_test, predict_click))

#Using Nueral Network

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()
# Adding the input layer and the first hidden layer
classifier.add(Dense(units =15 , kernel_initializer = 'uniform', activation = 'relu', input_dim = 17))
# Adding the second hidden layer
classifier.add(Dense(units = 15, kernel_initializer = 'uniform', activation = 'relu'))
# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10000, epochs = 3)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = list(map(lambda x: 1 if x>0.5 else 0,y_pred))
score = classifier.evaluate(X_test, y_test)
score

print(y_pred[:10])

# Importing a pure confusion matrix from sklearn.metrics family
from sklearn.metrics import confusion_matrix
# Printing the confusion_matrix
print(confusion_matrix(y_test, y_pred))
