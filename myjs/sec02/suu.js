class suu{
    constructor(myid,mypw,myname,mytel,myjob,mysex,myh){
        this.myid=myid;
        this.mypw=mypw;
        this.myname=myname;
        this.mytel=mytel;
        this.myjob=myjob;
        this.mysex=mysex;
        this.myh=myh;
    }

    printsu(){
        const myText = `id : ${this.myid}, pw : ${this.mypw}, name : ${this.myname}, tel : ${this.mytel}, job : ${this.myjob}, sex : ${this.mysex}, hobby : ${this.myh}`;
        document.getElementById('intro').value=myText;
    }
}

const form = document.querySelector('form');

form.addEventListener("submit", function (event) {
    event.preventDefault();     

    const idinput = document.getElementById('id');
    const pwinput = document.getElementById('pw');
    const mnameinput = document.getElementById('name');
    const telinput1 = document.getElementById('tel');
    const telinput2 = document.getElementById('tel2');
    const telinput3 = document.getElementById('tel3');
    const jobinput = document.getElementById('job');
    const myMale = document.getElementById('male');
    const myFemale = document.getElementById('female');
    const myHobby = document.getElementsByName('hobby');
    console.dir(myHobby[0].checked);

    const id = idinput.value;
    const pw = pwinput.value;
    const mname = mnameinput.value;
    const Tel = `${telinput1.value}-${telinput2.value}-${telinput3.value}`;
    const Job = jobinput.value;
    if(myMale.checked == true){
        var myS = myMale.value; 
    }
    else{
        var myS = myFemale.value;
    }

    var myH=[];
    
    if(myHobby[0].checked == 1) var myH= myHobby[0].value;
    if(myHobby[1].checked == 1) var myH= myHobby[1].value;
    if(myHobby[2].checked == 1) var myH= myHobby[2].value;
    if(myHobby[3].checked == 1) var myH= myHobby[3].value;


    const mee= new suu(id, pw, mname, Tel, Job, myS, myH);
    mee.printsu();
});