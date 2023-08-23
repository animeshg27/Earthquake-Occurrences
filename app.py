from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)
driver = '{ODBC Driver 18 for SQL Server}'
database = 'ADB'
server = 'tcp:adbassignments.database.windows.net'
username = "axg6991"
password = "27Animesh$"

conn=pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor=conn.cursor()

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/Task4")
def task4():
    return render_template('Task4.html') 

@app.route("/fetch_data3")
def task3():
    return render_template('fetch3.html') 




@app.route('/Task1', methods=['POST', 'GET'])
def ShowPieChart():
            sql1 = "SELECT count(*) FROM all_month WHERE mag <=1"
            cursor.execute(sql1)
            output = cursor.fetchall()
            s2 = output[0][0]
            sql2 = "SELECT count(*) FROM all_month WHERE mag between 0 and 1"
            cursor.execute(sql2)
            output = cursor.fetchall()
            s3 =output[0][0]
            sql3 = "SELECT count(*) FROM all_month WHERE mag between 1 and 2"
            cursor.execute(sql3)
            output = cursor.fetchall()
            s4 =output[0][0]
            sql3 = "SELECT count(*) FROM all_month WHERE mag between 2 and 3"
            cursor.execute(sql3)
            output = cursor.fetchall()
            s5 =output[0][0]
            sql4 = "SELECT count(*) FROM all_month WHERE mag between 3 and 4"
            cursor.execute(sql4)
            output = cursor.fetchall()
            s6 =output[0][0]
            sql5 = "SELECT count(*) FROM all_month WHERE mag between 4 and 5"
            cursor.execute(sql5)
            output = cursor.fetchall()
            s7 =output[0][0]
            sql5 = "SELECT count(*) FROM all_month WHERE mag  >= 5"
            cursor.execute(sql5)
            output = cursor.fetchall()
            s1 =output[0][0]
            l=[[5,"more",s1], [4,5,s7],[3,4,s6],[2,3,s5],[1,2,s4],[0,1,s3],["less",1,s2]]
            return render_template('Task1.html', rows=l)
        

@app.route('/Task2', methods=['POST', 'GET'])
def ShowBarChart():
            sql1 = "SELECT count(*) FROM all_month WHERE mag <=1"
            cursor.execute(sql1)
            output = cursor.fetchall()
            s2 = output[0][0]
            sql2 = "SELECT count(*) FROM all_month WHERE mag between 0 and 1"
            cursor.execute(sql2)
            output = cursor.fetchall()
            s3 =output[0][0]
            sql3 = "SELECT count(*) FROM all_month WHERE mag between 1 and 2"
            cursor.execute(sql3)
            output = cursor.fetchall()
            s4 =output[0][0]
            sql3 = "SELECT count(*) FROM all_month WHERE mag between 2 and 3"
            cursor.execute(sql3)
            output = cursor.fetchall()
            s5 =output[0][0]
            sql4 = "SELECT count(*) FROM all_month WHERE mag between 3 and 4"
            cursor.execute(sql4)
            output = cursor.fetchall()
            s6 =output[0][0]
            sql5 = "SELECT count(*) FROM all_month WHERE mag between 4 and 5"
            cursor.execute(sql5)
            output = cursor.fetchall()
            s7 =output[0][0]
            sql5 = "SELECT count(*) FROM all_month WHERE mag  >= 5"
            cursor.execute(sql5)
            output = cursor.fetchall()
            s1 =output[0][0]
            l=[[5,"more",s1], [4,5,s7],[3,4,s6],[2,3,s5],[1,2,s4],[0,1,s3],["less",1,s2]]
        
            return render_template('Task2.html', rows=l)


@app.route('/Task3', methods=['POST','GET'])
def ShowScatterPlot():

        s1 = "select top 100 mag, all_month.depth from all_month order by time desc"
        cursor.execute(s1)
        r = cursor.fetchall()
        return render_template('Task3.html', msg="done",r=r)

# Quiz 4 (q12)
# @app.route('/Task3', methods=['POST','GET'])
# def ShowScatterPlot():
#         # r1 = str(request.form['r1'])
#         # r2 = str(request.form['r2'])
#         s1 = "select top 100 mag, all_month.depth from all_month order by time desc"
#         # s1 = "select S,T from datas where R between '"+r1+"' and '"+r2+"' "
#         cursor.execute(s1)
#         r = cursor.fetchall()
#         return render_template('Task3.html', msg="done",r=r)


# @app.route('/Task4', methods=['POST', 'GET'])
# def line_chart():
#     if request.method == 'POST':
#         magWeek1 = request.form['magWeek1']
#         magWeek2 = request.form['magWeek2']
#         d1 = request.form['d1']
#         d2 = request.form['d2']
#         s1 = "SELECT  count(mag) , substring(time, 1, 10) as date from all_month where mag between {} and {} and substring(time, 1, 10) between '{}' and '{}' group by substring(time, 1, 10) order by substring(time, 1, 10)".format(magWeek1 , magWeek2 , d1 , d2)
#         cursor.execute(s1)
#         r=cursor.fetchall()
#         return render_template('Task4.html', r=r,msg="done")
#     if request.method == 'GET':
#         return render_template('Task4.html', result="")        

if __name__ == '__main__':
    app.run(port=5001)
