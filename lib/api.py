from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def returnascii():
    d = {}
    inputchr = str(request.args['query'])
    answer = inputchr
   #d['output'] = answer
    #MySQL
    mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="kl32K4893*",
    database="flutter",
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO Persons (roll, name) VALUES (%s, %d)"
    val = (1, answer)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


    return d



if __name__ =="__main__":
    app.run()
