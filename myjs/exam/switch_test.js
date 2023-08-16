function checkFruit() {
    //alert("확인");
    // html에 있는 id=f_input를 찾아서 값을 리턴받자.
    var fruit = document.getElementById("f_select").value;  //f_input으로하면 TEXT바의 VALUE가 들어옴

    var message; // p의 textContent로..

    switch(fruit){ 
        case "apple" : message = "selected fruit is apple"; 
            break;
        case "grape" : message = "selected fruit is grape";
             break;
        case "banana" : message = "selected fruit is banana"; 
            break;
        case "orange" : message = "selected fruit is orange"; 
            break;
        case "pear" : message = "selected fruit is pear"; 
            break;
        default : message="no.."; 
            break;   
    }//end switch
    //document.getElementById("result").textContent=message;
    //2. 
    myp=document.getElementById("result");
    myp.textContent=message;
    myp.style.fontSize="1.5em";
}//end function