
//ex01. 변수 a에 10을 대입하고 만일 a가 0보다 크면 양수라고 출력하자.

    let a=10;   //let는 지역변수
    if(a>0){
        console.log("ex01. 양수");
    }

//ex02. 변수 b에 -10을 대입하고 만일 b가 0보다 크면 양수라고 출력하자. 
//그렇지 않으면 음수라고 출력하자.

    let b=-10;
    if(b>0){
        console.log("ex02. 양수");
    }
    else{
        console.log("ex02. 음수");
    }

//ex03. 변수 c에 0을 대입하고 만일 c가 0보다 크면 양수라고 출력하자. 
// 0보다 작으면 음수라고 출력. 나머지는 '이도저도 아니야'라고 출력.
// 하나의 if문은 여러개의 else if를 가질 수 있고 마지막은 else로 마무리한다.    
// if는 조건문의 결과가 true일 때 명령을 수행한다.

    let c=0;
    if(c>0){
        console.log("ex03. 양수");
    }
    else if(c<0){
        console.log("ex03. 음수");
    }
    else{
        console.log("ex03. 이도저도 아니다.")
    }