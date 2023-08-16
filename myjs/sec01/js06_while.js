//1. 반복 while을 이용해서 1~5까지 출력해보자.
var count=1;                            //count = 1,

while(count <= 5){                      //(1<=5)t, (2<=5)t , (3<=5)t, (4<=5)t, (5<=5)t, (6<=5)f
    console.log("count: "+ count);      //"count:1", "count:2", "count:3", "count:4", "count:5",
    count= count+1;     //count++;      //count=2, count=3, count=4, count=5, count=6
}//죽이는 법 : ctrl+<alt>+M
console.log("=======>count: "+ count);          //"count:6"



//2. 반복 while 이용 10~1까지 출력.

var count2=10;                          
while(count2 >= 1 ){                     
    console.log("count2: "+ count2);      
    count2--;     //count--;      
}//죽이는 법 : ctrl+<alt>+M
console.log("=======>count2: "+ count2);