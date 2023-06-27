from flask import Flask, render_template,request

app = Flask(__name__)  
  
@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/login',methods = ['GET','POST'])  
def login():  
      uname=request.form.get('uname')  
      passwrd=request.form.get('pass')
      print(uname)
      print(passwrd)  
      if uname=="ayush" and passwrd=="google":  
          return render_template('indo.html') 
      else:
          return "none" 
@app.route('/upload',methods=['POST'])
def upload():
    f= request.files['myfile']
    if f:
        csv_data=f.read().decode('utf-8')
        csv_rows=csv_data.split('\n')
        
    return render_template('result.html',data=csv_rows)      
if __name__ == '__main__':  
   app.run(debug = True) 


