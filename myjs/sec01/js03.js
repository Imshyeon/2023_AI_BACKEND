//1)비교연산자.  
var a = 5;
var b = 10;
var c = "5";    //문자열로 간주

console.log(a == b);    // '==' 값 비교  
console.log(a != b);       
console.log(a === c);   //'==='은 '=='으로 생각    
console.log(a !== c);    
    console.log(a > b);      
    console.log(a < b);      
    console.log(a >= b);     
    console.log(a <= b);     

    //2) 비트연산,
    var a = 2, b = 7, c;
    c = a & b; 
    console.log(" 2 & 7 는 "+c);
    c = a | b;    
    console.log("2| 7 는 "+c); 
    c = a ^ b;
    console.log("2 ^ 7  는 "+c);

    //3)  논리연산
    a=5;
    b=10;
    var result = a > 0 && b < 20 ;  //true && true = true(1)
    console.log(result);

    // 논리합일 경우, 왼쪽에 있는 피연산자의 결과가 true이면 나머지 연산 안하고 true를 리턴
    // 논리곱일 경우, 왼쪽에 있는 피연산자의 결과가 false이면 나머지 연산 안하고 false를 리턴
    // 2 && 7 = 7 => 자세한설명은 notice.txt
    // 7 && 2 = 2 

    q=0;
    w=7;
    var result1 = q && w;
    var result2 = q || w;
    var result3 = q ^ w;
    console.log(result1 && 0 && 9); // 0 && 7 = 0
    console.log(result2 || 10 || 0); // 0 || 7 = 7
    console.log(result3); // 0 ^ 7 = 7
/*

		 0000000000000010  (2)
      |  0000000000000111  (7)
       _________________________
         0000000000000111  (7)

       
       
           0000000000000010  (2)
       &   0000000000000111  (7)
	   _________________________
           0000000000000010  (2)




         0000000000000010  (2)
     ^   0000000000000111  (7)
_______________________________
         0000000000000101  (5)

 */