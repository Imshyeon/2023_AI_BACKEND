// ES6 = 2015 : `$ `(템플릿 문자열), let, lambda식, 클래스, 상속, 다형성
// class = 속성 + 메소드 (기능), 각 속성의 접근제한자, 상속(), 재정의, 다형성 -> 특징 : 클래스, 다형성, 상속
//       각 이름 + 총점, 평균, 출력
// class => 안에 선언된 변수(속성), 메소드.. 이런 것들을 멤버라고 부른다.
//                                 메소드 안에 생성자(키워드) 추가.
class Sung{ //class username{}
    constructor(my_name="noname", kor=50, eng=50, mat=50){    //constructor(){} -> 생성자. new연산자로 호출가능.
                                                              //아예 초기값을 설정.
        this.my_name = my_name; 
        this.kor = kor;         
        this.eng = eng;         
        this.mat = mat;         
    }

    //==========*예시 : Date*=============/
    // class Date{
    //  constructor(year, monthIndex, day, hours, minutes, seconds, milliseconds) {
    //    this.year = year;
    //  } 
    // }
    //new Date(year, monthIndex, day, hours, minutes, seconds, milliseconds)

    // constructor(){    //생성자 목적 : 멤버 변수 초기화
    //     this.my_name = "noname"; 
    //     this.kor = 100;         
    //     this.eng = 100;         
    //     this.mat = 100;         
    // }

    //총점을 계산하는 메소드
    calculateTotal(){
        return this.kor+this.eng+this.mat;
    }
    //평균을 계산하는 메소드
    calculateAverage(){
        return this.calculateTotal()/3;
    }
    //멤버를 호출해서 출력하는 메소드
    printScore(){
        const total = this.calculateTotal();
        const average = this.calculateAverage();
        console.log(`${this.my_name}'s Total : ${total}, Average : ${average}`);
        // console.log(`${this.my_name}'s Total : ${total}, Average : ${average}`);
    }
}
// new Sung("홍길동",90, 80, 70); -> 초기값 전달하면서 동적할당. -> 생성자 호출하며 방 만듦
// new 연산자는 동적할당 후 초기값 전달을 생성자를 통해서 실행된다.
// new = 동적할당 하겠다.(생성자 호출) => 생성자(멤버변수 초기화 -> 방 만듦)
// 클래스는 항상 초기값을 받으면서 방을 만들어야 함. 빈방은 못 만듦
const s1 = new Sung("홍길동",90, 80, 70);   //new : 동적할당 키워드
                                            // Sung클래스가 가진 constructor()를 찾아서 자동호출 -> 값 대입 -> 메모리 할당.

s1.printScore();    // 기능형 메소드
const s2 = new Sung();
s2.printScore();
const s3 = new Sung("이길동", 0, 100, 100);
s3.printScore();
const s4 = new Sung("최길동",100);
s4.printScore();
const s5 = new Sung("강길동");  //이렇게 함로써 자체 overload
s5.printScore();

// let today = new Date()
console.log(new Date().toString()); // 오늘 날짜
console.log(new Sung().toString()); // Sung { my_name: 'noname', kor: 50, eng: 50, mat: 50 } => constructor의 초기값
                                    // Sung().toString() : [object Object]