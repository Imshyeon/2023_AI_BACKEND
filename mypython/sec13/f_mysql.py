''' json 타입의 문자열을 python 모듈로 인코딩, 디코딩 -> mysql '''
import mysql.connector  #테이블 생성, insert, select
import json

config = {
      'user': 'root',
      'password': '^Kimjml5v2!',
      'host': '127.0.0.1',
      'database': 'my_test',
      'raise_on_warnings': True
    }
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

def create():
    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute('''
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

    cursor.execute("INSERT INTO students(data) VALUES (%s)",(json.dumps(data),))
    cnx.commit()

#3. 테이블 생성 및 데이터를 mysql에서 확인
def select():
    #4. 전체 출력 및 json type의 json.loads(row[0])로 결과를 추출
    cursor.execute("SELECT data FROM students")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        print(json.loads(row[0]))   #전체출력
        json_data = json.loads(row[0])  #이름만 출력
        print(type(json_data))
        students = json_data.get("STUDENT",[])
        for student in students:
            name = student.get("NAME")
            print(name)

        print(students[0])  #Dominica와 관련값을 가져오고 싶다.

def select_name():
    #5. mysql query로 name을 추출하고싶다.
    query = "SELECT data -> '$.STUDENT[*].NAME' FROM students"
    cursor.execute(query)
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        names=row[0]
        print(names)
        name_json = json.loads(names)
        for name in name_json:
            print(name)


def select_score():
    query = "SELECT data -> '$.STUDENT[*].SCORE' FROM students"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        print(row)
        scores = row[0]
        print(scores)
        json_data = json.loads(scores)
        print(type(json_data),json_data)
        for score in json_data:
            kor = score.get("KOR")
            eng = score.get("ENG")
            mat = score.get("MATH")
            avg = (kor+eng+mat) / 3
            print(f'kor:{kor}, eng:{eng}, mat:{mat} ==> avg:{round(avg,1)}')

def scoreHap():
    #6. 점수의 합을 구하고싶다.
    query = "SELECT data -> '$.STUDENT[*].SCORE' FROM students"
    cursor.execute(query)
    rows=cursor.fetchall()
    print(rows)
    for row in rows:
        score_json=row[0]
        score_list=json.loads(score_json)   #[]로 리턴
        print(score_list[0],'<===',score_list)
        for score_dict in score_list:
            print(score_dict.values())
            sum_score = sum(score_dict.values())
            print(f"sum of scores : {sum_score}")

def select_all():
    query1 ="SELECT data -> '$.STUDENT[*].NAME' FROM students"
    query2 = "SELECT data -> '$.STUDENT[*].SCORE' FROM students"
    cursor.execute(query1)
    names=cursor.fetchall()
    cursor.execute(query2)
    scores = cursor.fetchall()
    print(names, scores)
    for name, score in zip(names,scores):
        print(name,score)
        print(name[0],score[0])
        json_name = json.loads(name[0])
        json_score = json.loads(score[0])
        print(json_name,json_score)

        for s_name, s_score in zip(json_name,json_score):
            print(s_name,"==> avg: ",round(sum(s_score.values())/len(s_score),1))

def select_all2():
    query1 ="SELECT data -> '$.STUDENT[*].NAME', data -> '$.STUDENT[*].SCORE' FROM students"
    cursor.execute(query1)
    data=cursor.fetchall()
    print(data)
    for name, score in data:
        print(type(name),name,"::",score)   #str type
        json_name = json.loads(name)
        json_score = json.loads(score)
        print(type(json_name),json_name,json_score) #list type
        for s_name, s_score in zip(json_name,json_score):
            print(s_name,"==> avg: ",round(sum(s_score.values())/len(s_score),1))


create()
insert()
select_all2()
cursor.close()
cnx.close()