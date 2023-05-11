from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST','DEleTE'])
def index():
    print(request.method)
    if request.method == 'POST':
        print(request)
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)