class Sung {
  constructor(my_name, kor, eng, mat) {
    this.my_name = my_name;
    this.kor = kor;
    this.eng = eng;
    this.mat = mat;
  }

  calculateTotal() {
    return this.kor + this.eng + this.mat;
  }

  calculateAverage() {
    return this.calculateTotal() / 3;
  }

  printScore() {
    const total = this.calculateTotal();
    const average = this.calculateAverage();

    const scoreContainer = document.getElementById("scoreContainer"); //div id가져와서 거기다가 출력을 하고싶다.
    
      const scoreText = `${this.my_name}'s Total: ${total}, Average: ${average}`;
      const scoreParagraph = document.createElement("p");
      scoreParagraph.textContent = scoreText;

    scoreContainer.appendChild(scoreParagraph);
  }
}

///////////////////////////////////////////
//1. 폼의 id를 찾아서 scoreForm으로 대입
const scoreForm = document.getElementById("scoreForm");
//2. 폼의 이벤트를 추가한다. "summit"이라는 글자를 받아오면 function(event) 실행
//3. 함수 핸들링을 한다.
//ex. scoreForm.addEventListener("submit", function (event) {});
scoreForm.addEventListener("submit", function (event) { //form id = scoreForm
  event.preventDefault(); //준비

  //////////////////폼의 입력상자에서 받은 값들을 각각의 변수에 대입한다.///////////////////
  const nameInput = document.getElementById("name");  //문자열(폼의 input 상자)
  const korInput = document.getElementById("kor");    //문자열(폼의 input 상자)
  const engInput = document.getElementById("eng");    //문자열(폼의 input 상자)
  const matInput = document.getElementById("mat");    //문자열(폼의 input 상자)
 
  ///////////각각의 변수에 대입//////////////
  const name = nameInput.value;
  const kor = Number(korInput.value);   //Number를 통해 수치로 변환
  const eng = Number(engInput.value);   
  const mat = Number(matInput.value);

  const student = new Sung(name, kor, eng, mat);
  student.printScore();

  // Reset form inputs
  scoreForm.reset();
});