# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 17:12:33 2017

@author: ndoannguyen
"""

DATA_DIR = "../Data/"
import Constants

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

mongo_client = MongoClient('localhost', 27017)

HistoryQCM = mongo_client[Constants.HISTORY_QCM_DATABASE]
QuestionCollection = HistoryQCM[Constants.QUESTION_COLLECTION]

all_questions = []

reader = open(DATA_DIR + Constants.QUESTIONS_FILE).read()
lines = reader.split("\r")
for line in lines:
    question = line.split("\t")
    all_questions.append(question)

index = 1

for question in all_questions:
    rhyme_mongo_document = {
                        "_id": Constants.QUESTION_PREFIX + question[2].zfill(6),
                        "zone" : question[0],
                        "period" : int(question[1]),
                        "question": question[3],
                        "A" : question[4],
                        "B" : question[5],
                        "C" : question[6],
                        "D" : question[7],
                        "answer": question[8]
                    }
    try:
        QuestionCollection.insert_one(rhyme_mongo_document)
        index += 1
    except DuplicateKeyError:
        print "[Error] Question with id %s already exists." % (Constants.QUESTION_PREFIX + str(index).zfill(6))
        index += 1