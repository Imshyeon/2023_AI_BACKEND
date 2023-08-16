import xml.etree.ElementTree as ET
#json 형식의 데이터를 xml로 저장하자.

data={
"STUDENT" :[
  {"NAME" :"Dominica","SCORE" : {"KOR":10,"ENG":20,"MATH":30}},
  {"NAME" :"Dominico","SCORE" :{"KOR": 90,"ENG":40, "MATH":100}},
  {"NAME" :"RuRe", "SCORE" :{"KOR": 90,"ENG":90, "MATH":90}}
  ]
}
#1. root를 만들자.
root=ET.Element("STUDENT")
print(data["STUDENT"])
#2. xml서식으로 하위 요소를 생성해서 추가하자
for student_data in data["STUDENT"]:
  student= ET.SubElement(root,"student")
  name = ET.SubElement(student,"NAME")
  name.text = student_data["NAME"]
  score= ET.SubElement(student,"SCORE")
  for subject, marks in student_data["SCORE"].items():
    #"SCORE" : {"KOR":10,"ENG":20,"MATH":30}
    sub = ET.SubElement(score,subject)
    sub.text = str(marks) #점수는 int니끼 str로 변환해서 넣어줘야함

#3. xml 만들자
tree = ET.ElementTree(root)

#4. xml생성된 tree를 파일로 저장하자.
tree.write("student.xml",encoding='utf-8',xml_declaration=True)

