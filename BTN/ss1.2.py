from flask import Flask, render_template
app = Flask(__name__)
@app.route('/BMI/<int:weight>/<int:height>')
def index(weight, height):
  bmi = { 
   'height' : float(height)/100,
   ' BMI' : float(weight) / float(height*height)
  }
  return  render_template('index1.html', data = bmi) 

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
