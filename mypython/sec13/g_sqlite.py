import sqlite3
import json

con = sqlite3.connect(":memory:")
cur=con.cursor()

def create():
    cur.execute("DROP TABLE IF EXISTS students")
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data JSON NOT NULL
        )
    ''')

def insert():
    #2. 입력할 데이터를 {} 선언하고 insert
    data = {
        "STUDENT" :[
          {"NAME" :"Dominica","SCORE" : {"KOR":10,"ENG":20,"MATH":30}},
          {"NAME" :"Dominico","SCORE" :{"KOR": 90,"ENG":40, "MATH":100}},
          {"NAME" :"RuRe", "SCORE" :{"KOR": 90,"ENG":90, "MATH":90}}
        ]
    }

    cur.execute("INSERT INTO students(data) VALUES (?)",(json.dumps(data),))
    con.commit()

def select():
    #4. 전체 출력 및 json type의 json.loads(row[0])로 결과를 추출
    cur.execute("SELECT data FROM students")
    rows=cur.fetchall()
    print(rows)
    for row in rows:
        json_data = json.loads(row[0])  #이름만 출력
        print(type(json_data),json_data)
        students = json_data.get("STUDENT",[])
        for student in students:
            name = student.get("NAME")
            score = student.get("SCORE")
            print(f'Name : {name}, Scores: {score}')

def select_avg():
    #5. mysql query로 name을 추출하고싶다.
    query = "SELECT data FROM students"
    cur.execute(query)
    rows=cur.fetchall()
    print(rows)
    for row in rows:
        print(row)
        s=row[0]
        students_json = json.loads(s)
        students= students_json.get("STUDENT")
        for each_student in students:
            # print(each_student)
            name=each_student.get("NAME")
            score = each_student.get("SCORE")
            print(name,"==>avg: ",round(sum(score.values())/len(score),1))

def hapScore():
    #6. 점수의 합을 구하고싶다.
    query = "SELECT data -> '$.STUDENT[*].SCORE' FROM students"
    cur.execute(query)
    rows=cur.fetchall()
    print(rows)
    for row in rows:
        score_json=row[0]
        score_list=json.loads(score_json)   #[]로 리턴
        print(score_list[0],'<===',score_list)
        for score_dict in score_list:
            sum_score = sum(score_dict.values())
            print(f"sum of scores : {sum_score}")


if __name__ == '__main__':
    create()
    insert()
    print("\n전체출력")
    select_avg()
    cur.close()
    con.close()