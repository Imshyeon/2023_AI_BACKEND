class present {
    constructor(userid, userpw, name, tel) {
        this.userid = userid;
        this.userpw = userpw;
        this.name = name;
        this.tel = tel;
    }
    
    printpr() {
        const prtext=`user id: ${this.userid}, user pw: ${this.userpw}, user name: ${this.name}, 
        user telephone: ${this.tel}`;

        document.getElementById('intro').value = prtext;
    }
}

const form = document.querySelector('form');

form.addEventListener("submit", function (event) {
    event.preventDefault();


    const idinput = document.getElementById('id');
    const pwinput = document.getElementById('pw');
    const unameinput = document.getElementById('name');
    const telinput1 = document.getElementById('tel');
    const telinput2 = document.getElementById('tel2');
    const telinput3 = document.getElementById('tel3');

const id = idinput.value;
const pw = pwinput.value;
const uname = unameinput.value;
const tel = `${telinput1.value}-${telinput2.value}-${telinput3.value}`;

const userpr = new present(id, pw, uname, tel);
userpr.printpr();
});
