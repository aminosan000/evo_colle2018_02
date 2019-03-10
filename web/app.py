# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'this_is_secret_key'

@app.route('/', methods=['GET', 'POST'])
def top():
    registered = []

    # 登録済み情報があった場合
    if 'registered' in session:
        registered = json.loads(session['registered'])

    # 登録ボタンによって呼び出された場合
    if request.method == 'POST':
        registered.append({'name': request.form['name'],
                          'company': request.form['company'],
                          'tel': request.form['tel'],
                          'mail': request.form['mail']})
        # 入力データを追加したlistをセッションに登録(上書き)
        session['registered'] = json.dumps(registered)

    return render_template('index.html', registered=registered)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
