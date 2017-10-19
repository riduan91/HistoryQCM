#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request
app = Flask(__name__)

SOURCE_DIR = "../"
import sys
sys.path.append(SOURCE_DIR)
import Constants, ChooseQuestions

@app.route("/")
def app1():
   return render_template("app1.html")
   
@app.route('/start', methods = ['POST', 'GET'])
def show_questions():
    if request.method == 'POST':
        questions = ChooseQuestions.chooseRandomQuestions(Constants.NB_QUESTIONS)
        return render_template("random_questions.html", result = (range(Constants.NB_QUESTIONS), questions))
    else:
        return render_template("app1.html")

@app.route('/answer', methods = ['POST', 'GET'])
def show_answers():
    if request.method == 'POST':
        parameters = request.form
        questions = []
        nb_correct_answers = 0
        
        for i in range(Constants.NB_QUESTIONS):
            question_id = parameters["id_" + str(i)]
            result = ChooseQuestions.getResult(question_id)
            questions.append(result)
            if ("option_" + str(i)) in parameters.keys() and parameters["option_" + str(i)] == result["answer"]:
                nb_correct_answers += 1
            
        return render_template("answer.html", result = (range(Constants.NB_QUESTIONS), questions, parameters, nb_correct_answers, Constants.NB_QUESTIONS, Constants.OPTIONS, map(str, range(Constants.NB_QUESTIONS))))
    else:
        return render_template("app1.html")
    
if __name__ == '__main__':
    app.run(host = Constants.HOST, port = Constants.PORT , debug=True)