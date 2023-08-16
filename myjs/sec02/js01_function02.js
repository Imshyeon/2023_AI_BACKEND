//ex) 세 과목의 총점, 평균을 연산하는 함수를 만들자.
//  조건
//   1. 각 과목의 점수를 리턴하는 함수를 만든다.
//   2. 총점, 평균을 연산하는 함수를 만든다.
//   3. 결과를 콘솔로 출력한다.


//1. 람다 변환
//   1. 각 과목의 점수를 리턴하는 함수를 만든다. _ 국,영,수
 
const getKor=()=>80;
const getEng=()=>90;
const getMat=()=>100;


//   2. 총점, 평균을 연산하는 함수를 만든다.

// const calcAvg = (kor, eng, mat) => {
//     const tot = kor + eng + mat;
//     const arg = tot/3;
//     return arg;
// }

const calcAvg = (kor,eng,mat) => (kor+eng+mat)/3;

//   3. 결과를 콘솔로 출력한다.
const res = calcAvg(getKor(), getEng(), getMat());
console.log("arg = "+ res);
