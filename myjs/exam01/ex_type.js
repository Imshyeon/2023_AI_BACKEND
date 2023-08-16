var a = 5;
var b = 10;
var result = `The sum of ${a} and ${b} is ${a + b}`; // ~밑의 `로 줘야 함.
console.log(result);

let my_name = "홍길동";
let greeting = `hello, ${my_name}`;
console.log(greeting);

let res1 =` -123의 절대값 : ${Math.abs(-123)}`; // class -> math 내장 객체 = 속성(값) + 메서드(기능) 
                       // math의 모든 속성과 메서드는 정적 = static
                       // static = 클래스.멤버 = 정적 = 공용
                       // non-static = 객체(클래스 변수).멤버 = 동적 = 개별적 작업

let res2 =`난수 : ${Math.random()}`; 
let res3 =`123.456의 반올림 : ${Math.round(123.456)}`; 
let res4 =`123.456의 올림 : ${Math.ceil(123.456)}`; 
let res5 =`123.456의 내림 : ${Math.floor(123.456)}`; 

console.log(res1);
console.log(res2);
console.log(res3);
console.log(res4);
console.log(res5);