let numbers = [1, 2, 3, "4", 5];    //Object - Array -> 요소를 인덱스로 관리 *관리=CRUD
let length = numbers.length;
for (let i = 0; i < length; i++) {
    console.dir(numbers[i]);
}
console.dir(typeof numbers);

console.dir('-----------------');

let fruitsArray=['사과', '딸기', '바나나', '키위', '포도'];
//1. 딸기의 인덱스를 찾아 출력해보자
console.dir("1. 결과 : "+fruitsArray.indexOf('딸기'));

// //2. 맨 뒤에 자몽을 추가.
console.dir("2-1. 추가 : "+fruitsArray.push('자몽'));
console.dir("2-1. 결과 : "+fruitsArray);

// //3. 자몽 추가한 것을 삭제해보자
console.dir("3-1. 제거 : "+fruitsArray.pop('자몽'));   //꺼낸 값을 리턴. => 삭제이지만 꺼내서 보여줌.
console.dir("3-1. 결과 : "+fruitsArray);

// //4. 맨앞에 포도를 추가해보자
console.dir("4-1. 추가 : "+fruitsArray.unshift('포도'));
console.dir("4-1. 결과 : "+fruitsArray);

// //5. 맨 앞의 요소를 제거해보자.
console.dir("5-1. 제거 : "+fruitsArray.shift());
console.dir("5-2. 결과 : "+fruitsArray);

// //6. 데이터를 배열로 만들어 결합을 해보자 (concat(결합할 오브젝트) 이용)
let myFruit = ['블루베리', '방울토마토', '체리', '파프리카'];
let newfruit = fruitsArray.concat(myFruit);
console.log("6. [ "+newfruit +" ]의 length:\t"+newfruit.length);
console.log("\t"+fruitsArray);

// //7.정렬해보자
let ch = '블루베리';    //'', " ",''' ''' -> string -> [char,,,,,] -> 인덱스로 찾아올 수 있다.
                        // ['참','외'] [0] [1]
console.log("\t"+"블루베리 코드값: "+ch.charCodeAt(1));   //블루베리의 '루'의 코드값
console.dir("7. "+fruitsArray.sort());


function compareNumbers(a, b) {
    return a - b;
  }

  var my_numbers = [4, 2, 5, 1, 3];
//   my_numbers.sort(function(a, b) {   //함수식 = 핸들링
//     console.log(a +" : "+ b + "===>" + my_numbers);
//     return a - b;
//   });
  
my_numbers.sort(compareNumbers);    
//클로저 : 객체가 가진 갯수만큼 일을 계속 함..   (*함수 안에 또다른 함수 호출.)                               
//       : 외부(둘러싸고 있는)에서 실행이 완료되면 둘러싸고있는 범위에서 엑세스 할 수 있는 기능
//          -> 내부함수가 외부함수 내에서 정의가 되고, 내부함수가 외부함수 범위의 변수를 참조할 때 생성되는 것을 말한다.
//          -> '내부함수는 참조하는 변수와 함께 클로저를 형성했다.' 라고 말한다.

// tip : 클로저에 의해 참조되는 변수는 클로저 자체에 더이상 도달할 수 없을 때 까지 가비지 수집되지 않으므로
//       클로저와 메모리 사용에 영향을 미치는 잠재적인 부분을 고려해야 한다.

console.log("7-1.핸들링과 클로저 : "+my_numbers);

//8. fruitsArray의 요소들을 글자 수 기준으로 오름차순(작~큰)으로 정렬해보자.
//   만약에 글자수가 같다면, 가나다순으로 내림차순으로 정렬을 해보자.

// *******************다양한 조건들을 만들어서 공부해보자.************************
function my_compare(a, b){
    if(a.length != b.length) return a.length - b.length;
    // else if(a.length==b.length) return a-b;
    
};

// 1) 예시1
// function my_compare(a,b){
//     //if(a.length  !=  b.length) return a.length - b.length;       
//   if (a.length === b.length) {  
//        return b < a ? -1 : 1; //길이가 같으면 내림차순
//     }
//   return a.length - b.length;
// }

// fruitsArr.sort(my_compare);   
// console.dir(fruitsArr);


// 2) 예시2
//아니면 중첩 구문으로  작성
// fruitsArr.sort(function(a, b) {
//     if (a.length === b.length) {  
//       if (a > b) {
//         return -1;
//       } else if (a < b) {
//         return 1;
//       } else {
//         return 0;
//       }
//     }
//     return a.length - b.length;
//   });


fruitsArray.sort(my_compare);
console.log(fruitsArray);

//9. 매개인자를 통해서 추가,수정,삭제,복사를 한번에 하는 splice()를 사용해보자.
//    array.splice(start[, deleteCount[, item1[, item2[, ...]]]])
//9-1. 2번 인덱스를 삭제해보자.
console.dir("9-1.");
console.dir(fruitsArray.splice(2,1));
console.dir(fruitsArray);

//9-2. 1번 인덱스 과일 2개를 추가해보자.
console.dir("9-2.");
console.dir(fruitsArray.splice(1,0,'메론','참외'));
console.dir(fruitsArray);

//9-3. 3번 인덱스에  수정
console.dir("9-3.");
console.dir(fruitsArray.splice(3,2,'블루베리'));
console.dir(fruitsArray);

//10. 원하는 위치의 배열을 복사해보자.
console.dir("10.");
console.dir(fruitsArray.slice(2,4));
console.dir(fruitsArray);



