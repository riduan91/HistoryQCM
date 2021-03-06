# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 17:38:56 2017

@author: ndoannguyen
"""

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append("../Configuration")
import configuration

import random

from pymongo import MongoClient
mongo_client = MongoClient('localhost', 27017)
QUESTION_PREFIX = configuration.QUESTION_PREFIX


def chooseRandom(mylist, nb):
    random.shuffle(mylist)
    return mylist[:nb]

def chooseRandomQuestions(nb_questions):
    HistoryQCM = mongo_client[configuration.HISTORY_QCM_DATABASE]
    QuestionCollection = HistoryQCM[configuration.QUESTION_COLLECTION]
    
    total_nb_questions = QuestionCollection.count()
    if nb_questions > total_nb_questions:
        nb_questions = total_nb_questions
        
    raw_question_list = range(1, total_nb_questions + 1)
    # Shuffle question list, independent of indices
    random.shuffle(raw_question_list)
    question_id_list = raw_question_list[:nb_questions]
    
    questions = []
    
    for question_id in question_id_list:
        try:
            my_question = QuestionCollection.find_one({ "_id": configuration.QUESTION_PREFIX + str(question_id).zfill(6) })
            questions.append(   {   "_id":      my_question["_id"], 
                                    "zone":     my_question["zone"], 
                                    "period":   my_question["period"], 
                                    "question": my_question["question"], 
                                    "A":        my_question["A"], 
                                    "B":        my_question["B"], 
                                    "C":        my_question["C"], 
                                    "D":        my_question["D"],
                                    "level":    my_question["level"],
                                    "tags":      my_question["tags"],
                                    "explanation": my_question["explanation"]} )
        except TypeError:
            print "[Error] Question \"%s\" not found in dictionary." % question_id

    return questions

def getResult(question_id):
    HistoryQCM = mongo_client['HistoryQCM']
    QuestionCollection = HistoryQCM['Questions']
    
    my_question = QuestionCollection.find_one({ "_id": question_id })
    res = {   "_id":      my_question["_id"], 
                                    "zone":     my_question["zone"], 
                                    "period":   my_question["period"], 
                                    "question": my_question["question"], 
                                    "A":        my_question["A"], 
                                    "B":        my_question["B"], 
                                    "C":        my_question["C"], 
                                    "D":        my_question["D"],
                                    "answer":   my_question["answer"],
                                    "level":    my_question["level"],
                                    "tags":      my_question["tags"],
                                    "explanation": my_question["explanation"]}
    return res