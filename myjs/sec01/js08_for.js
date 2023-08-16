//1~10까지 for로 출력.
// for(var i = 1; i <=10; i++){
//     console.log(i);
// }

//10~ 1까지 for로 출력.
// for(var j = 10; j >= 1; j--){
//     console.log(j);
// }

//숫자에 2를 나눈 나머지가 0이면 짝수, 그렇지 않으면 홀수
//1~100 홀수만 출력
// for(var k = 1; k <= 100; k++){
//     if((k%2) != 0){
//         console.log(k);
//     }  
// }

//1~100 짝수만 출력
// for(var k = 1; k <= 100; k++){
//     if((k%2) == 0){
//         console.log(k);
//     }  
// }

//1~100까지 출력을 하되, 2의 배수이면서 3의 배수..
// for(var k = 1; k <= 100; k++){
//     if((k%2 == 0) && (k%3 == 0)){
//         console.log(k);
//     }  
// }



var tableData = [
    {my_name : "홍길동0" , addr : "서울0", tel : "02-000-0000"} ,
    {my_name : "홍길동1" , addr : "서울1", tel : "02-000-1111"} ,
    {my_name : "홍길동2" , addr : "서울2", tel : "02-000-2222"} ,
];

for(var i = 0; i < tableData.length; i++){
    console.log(tableData[i]);
}

console.log(Object.keys(tableData[0]));
