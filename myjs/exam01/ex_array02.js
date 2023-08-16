//ES6 추가문법을 활용한 메소드 호출
//Array join, filter, find, map, flatMap
let fruitsArray=['사과', '딸기', '바나나', '키위', '포도'];

//1.
console.dir("1. join test");
console.dir(`[${fruitsArray.join(']*[')}]`);

//2.
//  arr.filter(callback(element[, index[, array]])[, thisArg])
//  
console.dir("2. filter test : 조건 추출");  // 변수 => 조건식 ~ 클로저가 끝나면 true의 결과값(테스트통과한 값)을 받아서 리턴.
console.dir(fruitsArray.filter(function(e){
    return e.length == 2;
}));

console.dir(`2-1. ${fruitsArray.filter(e => e.length == 2)}`);
console.dir(`2-2. ${fruitsArray.filter(r => r.length == 3)}`);


//3.
console.dir("3. find test : 요소를 찾는다");
console.dir(fruitsArray.find(function(e){
    console.log(e.search('도'));    //mdn string.search() 참고
    return e.search('도') > -1;
}));

console.dir(fruitsArray.find(e => e.search('바') > -1));




// 배열에서 소수 찾기
console.log("\n\n====배열에서 소수 찾기=====")
function isPrime(element, index, array) {
    var start = 2;
    while (start <= Math.sqrt(element)) {
      if (element % start++ < 1) {
        return false;
      }
    }
    return element > 1;
  }
  
  console.log([4, 6, 8, 12].find(isPrime)); // undefined, not found
  console.log([4, 5, 8, 12].find(isPrime)); // 5
// 소수%2 > 1
// 6%2(결과 : 0) < 1   
console.log("\n\n")
  


//4. map
console.dir("4. map test : 요소 연산");
// 각 요소의 첫글자만 추출해서 배열로 리턴받자.
console.dir(fruitsArray.map(e => e[0]));


//5.
console.dir("5. flatMap test");
console.dir(fruitsArray);
console.dir(fruitsArray.flatMap(e => e[0]));
console.log("\n\n========map과 flatMap의 비교==========")
//map과 flatMap의 비교
//1.
let arr1 = ["it's Sunny in", "", "California"];
console.dir(arr1.map(x=>x.split(" ")));
console.dir(arr1.flatMap(x => x.split(" ")));
//2.
console.dir([1,2,3,4,5].map(e=>[e,e*2]));   //배열의 배열(=이중배열)
console.dir([1,2,3,4,5].flatMap(e=>[e,e*2]));   //단일배열


