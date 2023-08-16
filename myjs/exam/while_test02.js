//테이블을 동적으로 만들고 싶다.
//<table><tr><td></td></tr></table>        <th> <thead> <tbody> <tfoot>

var tableData = [
    {my_name : "홍길동0" , addr : "서울0", tel : "02-000-0000"} ,
    {my_name : "홍길동1" , addr : "서울1", tel : "02-000-1111"} ,
    {my_name : "홍길동2" , addr : "서울2", tel : "02-000-2222"} ,
];

///////table, thead, tbody
var table = document.createElement("table");
var thead = document.createElement("thead");
var tbody = document.createElement("tbody");

//////tabel header
var headerRow = document.createElement("tr");
var header = Object.keys(tableData[0]);

//////th
for(var i=0; i<header.length; i++){
    var th = document.createElement("th");
    th.textContent=header[i];
    headerRow.appendChild(th);
}
thead.appendChild(headerRow);
table.appendChild(thead);

///////create table rows
var rowIndex=0; //-> while
while(rowIndex < tableData.length){ // 줄 반복적으로
    //줄
    var row = document.createElement("tr");
    //칸 = 데이터가 가진 값의 인덱스 만큼
        for(var j=0; j<header.length; j++){ //칸 반복적으로
            var td=document.createElement("td");
            td.textContent=tableData[rowIndex][header[j]];
            row.appendChild(td);
        }
    tbody.appendChild(row); 
    rowIndex ++;
}
table.appendChild(tbody);   

var my_res = document.getElementById("container");
my_res.appendChild(table);


//////테이블 보더 1 , 솔리드, 파랑, 배경색은 핑크. => 테이블색깔 만들기
//////td의 폰트사이즈 1.5em
