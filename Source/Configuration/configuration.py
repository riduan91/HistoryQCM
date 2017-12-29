# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 17:52:01 2017

@author: ndoannguyen
"""

DATA_DIR = "../../Data/"

QUESTIONS_FILE = DATA_DIR + "QCM.csv"
QUESTION_PREFIX = "QTN"
DEFAULT_NB_QUESTIONS = 40

LEVELS = ["EASY", "MEDIUM", "HARD"]
NB_QUESTIONS = [10, 20, 40]
ZONES = ["WORLD", "VN"]
PERIODS = [0, 1, 2, 3, 4] 

HOST = "0.0.0.0"
PORT = 8802
DEBUG = True

HISTORY_QCM_DATABASE = "HistoryQCM"
QUESTION_COLLECTION = "Questions"
OPTIONS = ['A', 'B', 'C', 'D']