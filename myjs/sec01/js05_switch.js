//fruit 변수에 과일을 대입해서 문구를 출력해보자.

var fruit="apple";

switch(fruit){
    case "apple" : console.log("apple"); 
    case "과일" : console.log("과일선택"); break;
    
    case "pear" : console.log("pear"); break;
    case "과일" : console.log("과일선택 "); break;
    
    case "grape" : console.log("grape"); 
    case "과일" : console.log("과일선택"); break;

    case "strawberry" : console.log("strawberry"); 
    case "과일" : console.log("과일선택"); break;

    default: console.log("there's no what I want"); break;
}