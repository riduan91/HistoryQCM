#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request
app = Flask(__name__)

import sys
sys.path.append("../Configuration")
sys.path.append("../Requests")

import configuration, ChooseQuestions

@app.route("/")
def app1():
   return render_template("app1.html")
   
@app.route('/start', methods = ['POST', 'GET'])
def show_questions():
    if request.method == 'POST':
        questions = ChooseQuestions.chooseRandomQuestions(configuration.NB_QUESTIONS)
        return render_template("random_questions.html", result = (range(configuration.NB_QUESTIONS), questions))
    else:
        return render_template("app1.html")

@app.route('/answer', methods = ['POST', 'GET'])
def show_answers():
    if request.method == 'POST':
        parameters = request.form
        questions = []
        nb_correct_answers = 0
        
        for i in range(configuration.NB_QUESTIONS):
            question_id = parameters["id_" + str(i)]
            result = ChooseQuestions.getResult(question_id)
            questions.append(result)
            if ("option_" + str(i)) in parameters.keys() and parameters["option_" + str(i)] == result["answer"]:
                nb_correct_answers += 1
            
        return render_template("answer.html", result = (range(configuration.NB_QUESTIONS), questions, parameters, nb_correct_answers, configuration.NB_QUESTIONS, configuration.OPTIONS, map(str, range(configuration.NB_QUESTIONS))))
    else:
        return render_template("app1.html")
    
if __name__ == '__main__':
    app.run(host = configuration.HOST, port = configuration.PORT , debug = configuration.DEBUG)