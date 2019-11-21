from flask import Flask,request,render_template



app=Flask(__name__)

@app.route("/")
def my_form():
    return render_template("music.html")


@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."

    return render_template("music.html", forward_message=forward_message);
if __name__=="__main__":
    app.run(debug=True)


