import os
import cv2
from flask import Flask,render_template,request
import time

app=Flask(__name__)
@app.route("/",methods=['GET'])
def homepage():
    return render_template("index.html")
@app.route('/click',methods=['POST'])
def click():
    no_pics=int(request.form['pics'])
    video=cv2.VideoCapture(0)
    while True:
        time.sleep(3)
        ret,frame=video.read()
        time.sleep(3)
        if ret==True:
            if not os.path.exists("images"):
                os.makedirs("images")
            for i in range(0,no_pics):
                time.sleep(2)
                cv2.imwrite("images/harsh_{}.jpeg".format(i),frame)
            if cv2.waitKey(1):
                break
    video.release()
    cv2.destroyAllWindows()
    return render_template("index.html")




if __name__=="__main__":
    app.run(debug=True)