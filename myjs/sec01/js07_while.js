//배열과 반복문 : 하나의 변수에 나열형으로 []를 이용해서 값을 관리
//배열은 값을 인덱스로 관리한다. 대부분 0번부터 시작
//배열은 각각의 데이터를 요소라고 부르고 엘리먼트라고 칭한다.
//배열은 선언과 동시에 개수를 length로 속성을 제공한다.
//배열의 length, 인덱스는 1 차이가 난다.
var myArray = [1,2,3,4,5];  


//0~4번지 인덱스까지 일일히 출력
// console.log(myArray);
// console.log(myArray[0]);
// console.log(myArray[1]);
// console.log(myArray[2]);
// console.log(myArray[3]);
// console.log(myArray[4]);


//for문 이용
// for(var i=0; i<myArray.length; i++){ //myArray의 내용 출력
//     console.log(myArray[i]);    
// }


//myArray[0]~myArray[4] ++하면서 반복문으로 출력
// var countArray=0;
//===========1. 인덱스 숫자로 접근===============

// while(countArray <= 4){
//     console.log(myArray[countArray]);
//     countArray++;   
// }

//===========2. length로 접근===================

// while(countArray < myArray.length){
//     console.log(myArray[countArray]);
//     countArray++;   
// }


//myArray의 개수 출력
// console.log("개수 : " + myArray.length); 


//myArray[4] 출력
// console.log(myArray[myArray.length-1]); 

var i =0;

var tableData = [
    {my_name : "홍길동0" , addr : "서울0", tel : "02-000-0000"} ,
    {my_name : "홍길동1" , addr : "서울1", tel : "02-000-1111"} ,
    {my_name : "홍길동2" , addr : "서울2", tel : "02-000-2222"} ,
];

// while(i <= tableData.length-1){
//     console.log(tableData[i]);
//     i++;
// }

 // 홍길동2 서울0 출력
// console.log(tableData[2].my_name + "\t"+ tableData[0].addr);

//tableData에 있는 이름만 추출


// while(i <= tableData.length -1){
//     console.log(tableData[i].my_name);
//     i++;
// }

///이름:전화번호 로 출력
while(i <= tableData.length -1){
    console.log(tableData[i].my_name + ": " + tableData[i].tel);
    i++;
}

//반복 변수 = for, while => i, j, k, l, m ,n -> 포트란에서 유래됨..
// count, sum : 누적데이터 변수, tot : 총점데이터, ex.점수