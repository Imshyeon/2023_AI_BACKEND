// 만일, 나이가 19보다 크면 p태그 안에 "성인이다" 라고 출력
// 그렇지 않으면 "청소년이다" 출력 
var age = 1;

if(age>=19){
    //html 태그의 엘리먼트를 id로 찾아서 textContent에다가 출력하자.
    document.getElementById("message").textContent = "I'm an adult";
    
}
else{
    document.getElementsByTagName("p").textContent = "I'm a teenager";
    //실행안되는 오류 해결하기
}
