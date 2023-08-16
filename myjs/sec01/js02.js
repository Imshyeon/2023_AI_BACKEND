// 자바스크립트 데이터 타입 : typeof (python의 type과 같다.)
// [const, let(지역변수 선언)] => 권장, var=>글로벌 


//Number
const age = 23;    // age 변수에 23을 대입했다. -> 상수화(const) 
console.log(typeof age + "\t\t\t" + age)     // age의 타입을 확인했다. console.log(기록된다. 출력이 아니라)
                                             //number

//String ' ' " "
const m_name = '수현';
const addr = "군포";
console.log(typeof m_name + "\t" + m_name);     //string
console.log(typeof addr + "\n\t     " + addr);       //string

//Boolean
const isStudent = true;
console.log(typeof isStudent + "\t" + isStudent);      //boolean

//Undefined 
let myvar;
console.log(typeof myvar + "\t" + myvar);      //undefined

//Null
const m = null;     //object를 초기화하는 키워드
console.log(typeof m + "\t" + m);      //object

//Object
const person = {
    m_name : '강수현',
    addr : '군포'
}; //person의 m_name
console.log(typeof person + "\t" + person.m_name + "\t" + person.addr)  
// console.log(person[0].m_name, person[1].addr); 

//Array : 하나의 변수에 나열형 인덱스로 값을 저장하는 것.
const numbers = [1,2,3,4,5];
console.log(typeof numbers + "\t" + numbers);    // object로 나옴
console.log(typeof numbers + "\t" + numbers[0]);   
console.log(typeof numbers + "\t" + numbers[1]);   
console.log(typeof numbers + "\t" + numbers[2]);    
console.log(typeof numbers + "\t" + numbers[3]);   
console.log(typeof numbers + "\t" + numbers[4]);    
console.log(numbers[0] + numbers[3]);    

//Function
const add = function(a,b){
    return a+b;
};
console.log(typeof add + "\t" + add)     //funtion
console.log(typeof add + "\t" + add(10,20));
console.log(add(0,4));
console.log(add(10, numbers[4]));


console.log(2+"2");

//Symbol 
const id = Symbol('uniqueId');
console.log(typeof id + "\t" + id);     //symbol


