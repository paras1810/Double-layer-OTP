from flask import Flask, redirect, render_template, request, url_for, session, abort, jsonify
import helpers as h
lastOTP =""
app = Flask(__name__)
app.secret_key = "Hello World!!!!!$%^&*("
name = ""
@app.route('/')
def Home_page():
    return render_template("Home_page.html")

@app.route("/login", methods = ["POST"])
def login():
    d = getUsers()
    if request.form["username"] in d:
        name = request.form["username"]
        dic = {
            'name': request.form["username"],
            'password': request.form["password"],
            'otp': d[request.form["username"]][1],
        }
        f = open("newuser.txt","w")
        f.write(dic['name'])
        f.close()
        return render_template("myPage.html", obj = dic)

def getUsers():
    import pandas as pd
    df = pd.read_csv("Users/All_Users.csv")
    d = {}
    for i in range(df.shape[0]):
        l=[]
        for j in range(1, df.shape[1]):
            l.append(df.iloc[i,j])
        d[df.iloc[i,0]]=l
    return d

@app.route("/Otppage")
def otpProcess():
    var = h.genOTP()
    lastOTP = var
    return render_template("submitOTP.html", otp = var)

@app.route("/otpcheck", methods = ["POST"])
def otpcheck():
    var = str(request.form["otp"])
    value,otp = h.getotpvalue(var,lastOTP)
    f = open("newuser.txt","r")
    name = f.readline()
    value2 = h.getAppid(name)
    print(value)
    print(value2)

    if value == value2 :
        return render_template("valid.html")
    else:
        return render_template("invalid.html")

# @app.route("/register", methods = ["POST"])
# def register():
#     # import csv, io
#     # print("Hello2")
#     # file1 = request.files["file1"].read().decode("utf-8")
#     # f = request.files['file1']
#     # stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
#     # csv_input = csv.reader(stream)
#     # print(csv_input)
#     # print("Hello1")
#     if not request.files["file1"]:
#         abort(400, "missing file")
#     try:
#         file1 = request.files["file1"].read().decode("utf-8")
#         print(file1)
#     except Exception:
#         abort(400, "invalid file")
#     nf = open("db.csv", "a")
#     nf.write(file1)
#     user_id = h.getAppid(file1)
#     tup = (request.form["username"], request.form["password"], user_id)
#     f = open(tup[0] + ".csv", "w")
#     writer2 = csv.writer(tup)
#     obj = h.user()
#     obj.name = tup[0]
#     obj.password = tup[1]
#     obj.id_no = tup[2]
#     session[tup[0]] = obj



