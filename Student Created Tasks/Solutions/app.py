from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        subject = request.form.get("subject")
        if subject:
            conn = sqlite3.connect("results.db")
            cursor = conn.cursor()

            # filters students that meet requirements
            cursor.execute("""
                SELECT Name, CG
                FROM Results
                GROUP BY Name, CG
                HAVING 
                    SUM(1 * (Subject != 'GP' AND Grade IN ('A', 'B', 'C', 'D', 'E'))) >= 2
                    AND 
                    SUM(1 * (Subject = 'GP' AND Grade IN ('S', 'A', 'B', 'C', 'D', 'E'))) >= 1
                    AND 
                    SUM(1 * (Subject != 'GP' AND Grade IN ('S', 'A', 'B', 'C', 'D', 'E'))) >= 3
                    AND
                    SUM(1 * (Subject = 'Math' AND Grade = 'A')) > 0
                ORDER BY Name, CG;
            """)
            students = cursor.fetchall()

            conn.close()
            
            return render_template("index.html",students=students, subject=subject)
        else:
            conn = sqlite3.connect("results.db")
            cursor = conn.cursor()

            # filters students that meet requirements
            cursor.execute("""
                SELECT Name, CG
                FROM Results
                GROUP BY Name, CG
                HAVING 
                    SUM(1 * (Subject != 'GP' AND Grade IN ('A', 'B', 'C', 'D', 'E'))) >= 2
                    AND 
                    SUM(1 * (Subject = 'GP' AND Grade IN ('S', 'A', 'B', 'C', 'D', 'E'))) >= 1
                    AND 
                    SUM(1 * (Subject != 'GP' AND Grade IN ('S', 'A', 'B', 'C', 'D', 'E'))) >= 3
                ORDER BY Name, CG;
            """)
            students = cursor.fetchall()

            conn.close()
            
            return render_template("index.html",students=students)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
