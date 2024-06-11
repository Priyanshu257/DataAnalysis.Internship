#!/usr/bin/env python
# coding: utf-8

# ```Project-3
# Credit Card Prediction Analysis
# Made by : Priyanshu Kumar```

# # Credit Card Prediction Analysis!

# <img src="data:image/jpeg;base64,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">
# 
# # Context
# 
# Credit score cards are a common risk control method in the financial industry. It uses personal information and data submitted by credit card applicants to predict the probability of future defaults and credit card borrowings. The bank is able to decide whether to issue a credit card to the applicant. Credit scores can objectively quantify the magnitude of risk.
# 
# Generally speaking, credit score cards are based on historical data. Once encountering large economic fluctuations. Past models may lose their original predictive power. Logistic model is a common method for credit scoring. Because Logistic is suitable for binary classification tasks and can calculate the coefficients of each feature. In order to facilitate understanding and operation, the score card will multiply the logistic regression coefficient by a certain value (such as 100) and round it.
#  
# At present, with the development of machine learning algorithms. More predictive methods such as Boosting, Random Forest, and Support Vector Machines have been introduced into credit card scoring. However, these methods often do not have good transparency. It may be difficult to provide customers and regulators with a reason for rejection or acceptance.
#  
# 
# 
# # Task
# Build a machine learning model to predict if an applicant is 'good' or 'bad' client, different from other tasks, the definition of 'good' or 'bad' is not given. You should use some techique, such as vintage analysis to construct you label. Also, unbalance data problem is a big problem in this task.

# # Importing Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Extracting data using two data sources

# In[2]:


app = pd.read_csv("../input/credit-card-approval-prediction/application_record.csv")
crecord = pd.read_csv("../input/credit-card-approval-prediction/credit_record.csv")


# * Using different methods to understand data
# * data is complex and both dataset need some kind of transformation before analysis
# * datasets are indivudally dealt with and then eventually compiled using joins

# In[3]:


app.info()


# In[4]:


crecord.info()


# In[5]:


app['ID'].nunique() # the total rows are 438,557. This means it has duplicates


# In[6]:


crecord['ID'].nunique() 
# this has around 43,000 unique rows as there are repeating entries for different monthly values and status.


# In[7]:


len(set(crecord['ID']).intersection(set(app['ID']))) # checking to see how many records match in two datasets


# In[8]:


sns.heatmap(app.isnull()) # checking for null values. Seems like occupation_type has many


# In[9]:


sns.heatmap(crecord.isnull()) # checking for null values. All good here!


# In[10]:


app = app.drop_duplicates('ID', keep='last') 
# we identified that there are some duplicates in this dataset
# we will be deleting those duplicates and will keep the last entry of the ID if its repeated.


# In[11]:


app.drop('OCCUPATION_TYPE', axis=1, inplace=True) 
#we identified earlier that occupation_type has many missing values
# we will drop this column


# In[12]:


ot = pd.DataFrame(app.dtypes =='object').reset_index()
object_type = ot[ot[0] == True]['index']
object_type
#we are filtering the columns that have non numeric values to see if they are useful


# In[13]:


num_type = pd.DataFrame(app.dtypes != 'object').reset_index().rename(columns =  {0:'yes/no'})
num_type = num_type[num_type['yes/no'] ==True]['index']
#HAVE CREATED SEPARATE LIST FOR NUMERIC TYPE INCASE IT WILL BE NEEDED IN FURTHER ANALYSIS
# IT IS NEEDED IN FURTHER ANALYSIS


# In[14]:


a = app[object_type]['CODE_GENDER'].value_counts()
b = app[object_type]['FLAG_OWN_CAR'].value_counts()
c = app[object_type]['FLAG_OWN_REALTY'].value_counts()
d = app[object_type]['NAME_INCOME_TYPE'].value_counts()
e = app[object_type]['NAME_EDUCATION_TYPE'].value_counts()
f = app[object_type]['NAME_FAMILY_STATUS'].value_counts()
g = app[object_type]['NAME_HOUSING_TYPE'].value_counts()

print( a,"\n",b,'\n', c, '\n', d, '\n', e, '\n', f, '\n', g)

#this is just to see what each column is. 
#It seems that all of them are important since there is very fine classifcation in each column.
# their effectiveness cannot be judged at this moment so we convert all of them to numeric values.


# In[15]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for x in app:
    if app[x].dtypes=='object':
        app[x] = le.fit_transform(app[x])
# we have transformed all the non numeric data columns into data columns
# this method applies 0,1.. classification to different value types.


# In[16]:


app.head(10)


# In[17]:


app[num_type].head()
# We will look at numeric columns and see if there is anything that needs to be changed. 


# In[18]:


fig, ax= plt.subplots(nrows= 3, ncols = 3, figsize= (14,6))

sns.scatterplot(x='ID', y='CNT_CHILDREN', data=app, ax=ax[0][0], color= 'orange')
sns.scatterplot(x='ID', y='AMT_INCOME_TOTAL', data=app, ax=ax[0][1], color='orange')
sns.scatterplot(x='ID', y='DAYS_BIRTH', data=app, ax=ax[0][2])
sns.scatterplot(x='ID', y='DAYS_EMPLOYED', data=app, ax=ax[1][0])
sns.scatterplot(x='ID', y='FLAG_MOBIL', data=app, ax=ax[1][1])
sns.scatterplot(x='ID', y='FLAG_WORK_PHONE', data=app, ax=ax[1][2])
sns.scatterplot(x='ID', y='FLAG_PHONE', data=app, ax=ax[2][0])
sns.scatterplot(x='ID', y='FLAG_EMAIL', data=app, ax=ax[2][1])
sns.scatterplot(x='ID', y='CNT_FAM_MEMBERS', data=app, ax=ax[2][2], color= 'orange')


# There are outliers in 3 columns.
# 1. CNT_CHILDREN
# 2. AMT_INCOME_TOTAL
# 3. CNT_FAM_MEMBERS

# * We need to remove these outliers to make sure they do not affect our model results. 
# * We will now remove these outliers. 

# In[19]:


# FOR CNT_CHILDREN COLUMN
q_hi = app['CNT_CHILDREN'].quantile(0.999)
q_low = app['CNT_CHILDREN'].quantile(0.001)
app = app[(app['CNT_CHILDREN']>q_low) & (app['CNT_CHILDREN']<q_hi)]


# In[20]:


# FOR AMT_INCOME_TOTAL COLUMN
q_hi = app['AMT_INCOME_TOTAL'].quantile(0.999)
q_low = app['AMT_INCOME_TOTAL'].quantile(0.001)
app= app[(app['AMT_INCOME_TOTAL']>q_low) & (app['AMT_INCOME_TOTAL']<q_hi)]


# In[21]:


#FOR CNT_FAM_MEMBERS COLUMN
q_hi = app['CNT_FAM_MEMBERS'].quantile(0.999)
q_low = app['CNT_FAM_MEMBERS'].quantile(0.001)
app= app[(app['CNT_FAM_MEMBERS']>q_low) & (app['CNT_FAM_MEMBERS']<q_hi)]


# In[22]:


fig, ax= plt.subplots(nrows= 3, ncols = 3, figsize= (14,6))

sns.scatterplot(x='ID', y='CNT_CHILDREN', data=app, ax=ax[0][0], color= 'orange')
sns.scatterplot(x='ID', y='AMT_INCOME_TOTAL', data=app, ax=ax[0][1], color='orange')
sns.scatterplot(x='ID', y='DAYS_BIRTH', data=app, ax=ax[0][2])
sns.scatterplot(x='ID', y='DAYS_EMPLOYED', data=app, ax=ax[1][0])
sns.scatterplot(x='ID', y='FLAG_MOBIL', data=app, ax=ax[1][1])
sns.scatterplot(x='ID', y='FLAG_WORK_PHONE', data=app, ax=ax[1][2])
sns.scatterplot(x='ID', y='FLAG_PHONE', data=app, ax=ax[2][0])
sns.scatterplot(x='ID', y='FLAG_EMAIL', data=app, ax=ax[2][1])
sns.scatterplot(x='ID', y='CNT_FAM_MEMBERS', data=app, ax=ax[2][2], color= 'orange')


# In[23]:


crecord['Months from today'] = crecord['MONTHS_BALANCE']*-1
crecord = crecord.sort_values(['ID','Months from today'], ascending=True)
crecord.head(10)
# we calculated months from today column to see how much old is the month
# we also sort the data according to ID and Months from today columns. 


# In[24]:


crecord['STATUS'].value_counts() 
# performed a value count on status to see how many values exist of each type


# In[25]:


crecord['STATUS'].replace({'C': 0, 'X' : 0}, inplace=True)
crecord['STATUS'] = crecord['STATUS'].astype('int')
crecord['STATUS'] = crecord['STATUS'].apply(lambda x:1 if x >= 2 else 0)
# replace the value C and X with 0 as it is the same type
# 1,2,3,4,5 are classified as 1 because they are the same type
# these will be our labels/prediction results for our model


# In[26]:


crecord['STATUS'].value_counts(normalize=True) 
# there is a problem here
# the data is oversampled for the labels
# 0 are 99%
# 1 are only 1% in the whole dataset
# we will need to address the oversampling issue in order to make sense of our analysis
# this will be done after when we combine both the datasets
# so first we will join the datasets


# In[27]:


crecordgb = crecord.groupby('ID').agg(max).reset_index()
crecordgb.head() 
#we are grouping the data in crecord by ID so that we can join it with app


# In[28]:


df = app.join(crecordgb.set_index('ID'), on='ID', how='inner')
df.drop(['Months from today', 'MONTHS_BALANCE'], axis=1, inplace=True)
df.head()
# no that this is joined, we will solve over sampling issue


# df.info() # checking for number of rows. 
# # there are 9516 rows.

# In[29]:


df.info() # checking for number of rows. 
# there are 9516 rows.


# In[30]:


X = df.iloc[:,1:-1] # X value contains all the variables except labels
y = df.iloc[:,-1] # these are the labels


# In[31]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)
# we create the test train split first


# In[32]:


from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
X_scaled = pd.DataFrame(mms.fit_transform(X_train), columns=X_train.columns)
X_test_scaled = pd.DataFrame(mms.transform(X_test), columns=X_test.columns)
# we have now fit and transform the data into a scaler for accurate reading and results.


# In[33]:


from imblearn.over_sampling import SMOTE
oversample = SMOTE()
X_balanced, y_balanced = oversample.fit_resample(X_scaled, y_train)
X_test_balanced, y_test_balanced = oversample.fit_resample(X_test_scaled, y_test)
# we have addressed the issue of oversampling here


# In[34]:


y_train.value_counts()


# In[35]:


y_balanced.value_counts()


# In[36]:


y_test.value_counts()


# In[37]:


y_test_balanced.value_counts()


# * We notice in the value counts above that label types are now balanced
# * the problem of oversampling is solved now
# * we will now implement different models to see which one performs the best

# In[38]:


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


# In[39]:


classifiers = {
    "LogisticRegression" : LogisticRegression(),
    "KNeighbors" : KNeighborsClassifier(),
    "SVC" : SVC(),
    "DecisionTree" : DecisionTreeClassifier(),
    "RandomForest" : RandomForestClassifier(),
    "XGBoost" : XGBClassifier()
}


# In[40]:


train_scores = []
test_scores = []

for key, classifier in classifiers.items():
    classifier.fit(X_balanced, y_balanced)
    train_score = classifier.score(X_balanced, y_balanced)
    train_scores.append(train_score)
    test_score = classifier.score(X_test_balanced, y_test_balanced)
    test_scores.append(test_score)

print(train_scores)
print(test_scores)


# * We found out that XGBoost model is performing best on the train set as well as test set with 91% accuracy
# * We will be using XGBoost to predict our values.

# In[41]:


xgb = XGBClassifier()
model = xgb.fit(X_balanced, y_balanced)
prediction = xgb.predict(X_test_balanced)


# In[42]:


from sklearn.metrics import classification_report
print(classification_report(y_test_balanced, prediction))

