# from flask import Flask
# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()




from flask import Flask, render_template
# import Flask:
app = Flask(__name__)
# app = flask.Flask(__name__)
print(__name__)

# @app.route('/say/<action>/<name>')
# def index(action,name):
#     return action +' '+name


# @app.route('/say - hi/lan')
# def say_hi_lan():
#     return 'hello lan'

# @app.route('/add/<a>/<b>')
# def add(a,b):
#     return int(a)+int(b)


@app.route('/')
def index():
    # return '<h1>xin chao</h1> hoa'
    # return  render_template('index.html', title = 'tĩnh dạ tứ', body = 'nội dung',author = 'lý bạch')
    poen_data = [{
     'title' : 'tĩnh dạ tứ', 
     'body' : 'nội dung',
     'author' : 'lý bạch'
    },{
      'title' : 'bánh trôi nước', 
     'body' : 'nội dung',
     'author' : 'hồ xuân hương'
    },{
      'title' : 'đồng chí', 
     'body' : 'nội dung',
     'author' : 'tố hữu'
    }]
    return  render_template('index.html')

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)


