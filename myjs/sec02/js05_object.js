// Object 클래스의 재정의 메소드를 구현한 Person 확인
class Person{
    constructor(my_name, age){
        this.my_name = my_name;
        this.age = age;
    }
    toString(){ //'재정의'를 한 메소드
        return "내꺼";
    }
}
console.log(new Person("홍길동", 10));
//객체를 p1으로 생성한 후 p1을 출력해보자
const p1 = new Person("1111", 20);  //p1 = Object() -> Person()
console.log(p1.toString()); 

