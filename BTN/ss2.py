from flask import Flask, render_template
app = Flask(__name__)
@app.route ('/usesr/<username>')
def index(username):
  Usesr ={
      'Huy':
    {
    'name' : 'Nguyen Quang Huy',
    'age' : 29
    },
    'Anh':{
    'name' : 'Huynh Tuan Anh',
    'age' : 22
    }
  }
  return  render_template('index2.html', data = Usesr)

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)

