import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db=client['my_emp']
collection = db['emp']

print(collection.name)
print(collection.find_one())
length_of_collection=collection.estimated_document_count()
print("---------------------")
for i in range(0,length_of_collection):
    empno=collection.find({})[i].get("empno")
    ename = collection.find({})[i].get("ename")
    job = collection.find({})[i].get("job")
    mgr = collection.find({})[i].get("mgr")
    hiredate = collection.find({})[i].get("hiredate")
    sal = collection.find({})[i].get("sal")
    comm = collection.find({})[i].get("comm")
    deptno = collection.find({})[i].get("deptno")
    print(empno, ename, job, mgr, hiredate, sal, comm, deptno)
