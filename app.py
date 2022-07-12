from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests


app = Flask(__name__)

client = MongoClient('mongodb+srv://test:spart@cluster0.ribo7dl.mongodb.net/?retryWrites=true&w=majority')
db = client.teamproject



@app.route('/')
def main():
    # 리스트 갖고오기
    projects = list(db.project.find({}, {"_id": False}))
    return render_template("index.html", projects=projects)

@app.route('/api/save_board', methods=['POST'])
def save_board():
    # 보드게임 저장하기
    return jsonify({'result': 'success', 'msg': '단어 저장'})

@app.route('/signup')
def detail():
    # 로그아웃 버튼 누를시 회원가입 페이지
    return render_template("signup.html")

@app.route('/detai')
def detail():
    # 보드게임 등록 누를시 등록 페이지
    return render_template("signup.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)