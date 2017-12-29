# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 17:12:33 2017

@author: ndoannguyen
"""

import sys
sys.path.append("../Configuration")
sys.path.append("../Requests")
import configuration

DATA_DIR = configuration.DATA_DIR

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

mongo_client = MongoClient('localhost', 27017)

HistoryQCM = mongo_client[configuration.HISTORY_QCM_DATABASE]
QuestionCollection = HistoryQCM[configuration.QUESTION_COLLECTION]

def print_help():
    print "Usage: python ImportQuestionDatabase.py [option]"
    print "    - The data file name is specified in the folder 'Configuration'"
    print "    - option can be 'help', 'force' or nothing"
    print "         + 'help': Print this text."
    print "         + 'force': Delete questions in the current database, replace them by the questions in the file."
    print "         + nothing: Insert the questions in the file without overriding questions in the current database."
    
def delete_all_questions():
    print "Dropping the question collection in MongoDB"
    QuestionCollection.drop()
    print "Drop finished"

def insert_all_questions():
    all_questions = []
    
    print "Inserting questions into MongoDB"

    reader = open(configuration.QUESTIONS_FILE).read()
    lines = reader.split("\r")
    for line in lines:
        if len(line) > 0:
            question = line.split("\t")
            all_questions.append(question)

    index = 1

    for question in all_questions:
        rhyme_mongo_document = {
                            "_id": configuration.QUESTION_PREFIX + question[2].zfill(6),
                            "zone" : question[0],
                            "period" : int(question[1]),
                            "question": question[3],
                            "A" : question[4],
                            "B" : question[5],
                            "C" : question[6],
                            "D" : question[7],
                            "answer": question[8],
                            "level": question[9],
                            "tags": question[10],
                            "explanation": question[11]
                            }
        try:
            QuestionCollection.insert_one(rhyme_mongo_document)
            print "[Info] Question with id %s has been successfully inserted." % (configuration.QUESTION_PREFIX + str(index).zfill(6))
            index += 1
        except DuplicateKeyError:
            print "[Error] Question with id %s already exists." % (configuration.QUESTION_PREFIX + str(index).zfill(6))
            index += 1
        
    print "Import successfully finished."
    return

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'help':
            print_help()
    
        elif sys.argv[1] == 'force':
            delete_all_questions()
            insert_all_questions()
    
        else:
            print "Option not recognized."
            print_help()
    
    elif len(sys.argv) == 1:
        insert_all_questions()
    
    else:
        print "Syntax incorrect."
        print_help()
