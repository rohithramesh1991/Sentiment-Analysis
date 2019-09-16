# Sentiment-Analysis
Sentiment analysis is a type of data mining that measures the inclination of people’s opinions through natural language processing (NLP), computational linguistics and text analysis, which are used to extract and analyse subjective information from the Web - mostly social media and similar sources. The analysed data quantifies the general public's sentiments or reactions toward certain products, people or ideas and reveal the contextual polarity of the information. Sentiment analysis is also known as opinion mining.
Types of Sentiment Analysis:
There are many types and flavours of sentiment analysis and sentiment analysis tools range from systems that focus on polarity (positive, negative, neutral) to systems that detect feelings and emotions (angry, happy, sad, etc) or identify intentions (e.g. interested v. not interested). 

![emotion-flashcards-preview jpg__w0](https://user-images.githubusercontent.com/49020018/64973210-3a9df500-d8c8-11e9-90a3-58373b104c39.jpg)
 
Here in this project, we will be looking at target variable with binary classification. The project is about interpreting a hotel review as good or bad, based on the customer experience.
Please go through the comments section of the code file for better understanding.

This Project has been modelled on 4 different types algorithms and their corresponding accuracy are also checked.
1.	Logistic Regression
2.	Random Forest
3.	Naïve Bayes
4.	SVM (Support Vector Machine)

The Best model is selected based on the accuracy , precision , recall , F1 score which are obtained form classification report and also AUC(Area under the curve)
Out of these models, Logistic Regression and SVM with Linear Kernel and regularization parameter (gamma) of 0.001produced an accuracy of about 89%.
