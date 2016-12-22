#!/usr/bin/env python

#################//Virtual Doctor//######################
#Ilakya Selvarajan - ML assignment
#Program to predict disease by using symptoms 
# I have used Bag of words concept and random forest classifer (supervised learning) for this assignment
# The idea was formulated from a kaggle tutorial (Link of the tutorial is present in the assignment manuscript)
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from Word2VecUtility import Word2VecUtility
import pandas as pd
import numpy as np

#import train set

if __name__ == '__main__':
    train = pd.read_csv('trainset.txt', header=0, delimiter="\t", quoting=3)

    print "\n\n The program was written for assignment purpose. Always always consult a doctor and never look up the symptoms on the internet :-) \n\n\n"
    
#Ask the user for symptoms
    test=["input", ""] 
    test[0]=raw_input("Type the symptoms with space and press enter")
    #test= raw_input()	
    
    

    print '\n\nPlease uncomment nltk.download() to download text data sets \n'
    #nltk.download()  # Download text data sets, including stop words

    # Initialize an empty list to hold the clean symptoms and summary
    clean_train_symptom = []
    clean_train_summary ={}

    

    print "Cleaning and parsing the training set symptoms...\n"
    for i in xrange( 0, len(train["symptom"])):
        clean_train_symptom.append(" ".join(Word2VecUtility.symptoms_to_wordlist(train["symptom"][i],True)))
    print "Cleaning and parsing the training set summary...\n"
    for i in xrange( 0, len(train["summary"])):
        
	clean_train_summary[train["disease"][i]] = "".join(Word2VecUtility.summary_to_wordlist(train["summary"][i]))
	
    
    # ****** Create a bag of words from the training set
    #
    print "Creating the bag of words...\n"
    

    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # bag of words tool.
    vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = None)

    # fit_transform() does two functions: First, it fits the model and learns the vocabulary; 
    #second, it transforms the training data into feature vectors. 
    train_data_features = vectorizer.fit_transform(clean_train_symptom)

    # Numpy arrays are easy to work with, so convert the result to an
    # array
    train_data_features = train_data_features.toarray()


    # ******* Train a random forest using the bag of words
    #
    print "Training the random forest (this may take a while)..."


    # Initialize a Random Forest classifier with 200 trees
    forest = RandomForestClassifier(n_estimators = 300,random_state=1500)
    
    # Fit the forest to the training set, using the bag of words as
    # features and the disease, summary  as the response variables
    #
    
    forest = forest.fit( train_data_features, train["disease"] )
    

    # Get a bag of words for the test set, and convert to a numpy array
    test_data_features = vectorizer.transform(test)
    
    test_data_features = test_data_features.toarray()
    

    # Use the random forest to make sentiment label predictions
    print "Predicting test labels...\n"
    result = forest.predict(test_data_features)
    print "the disease is",result[0]
    print clean_train_summary[result[0]]






