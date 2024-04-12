$(function(){

     let no = [1,2,3,4,5,6,7,8,9,10];
     let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
     let kor = [62,90,64,76,51,89,77,55,73,53];
     let eng = [70,62,73,54,55,60,67,77,51,100];
     let math = [81,79,50,83,72,79,82,86,50,94];
     let total = [213,231,187,213,178,228,226,218,174,247];
     let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];

     //tbody 부분 10개 행 생성
     

     //학생입력확인 버튼
     $("#confirmBtn").click(function(){
         //글자 - text() innerText input - val() value ,htaml() innerHtml
         // console.log("국어 : "+$("#kor").val());
         // console.log("영어 : "+$("#eng").val());
         // console.log("수학 : "+$("#math").val());
         //console.log(Math.max.apply(null,no)+1); //배열에서 최대값 구하기
         //no.push(Math.max.apply(null,no)+1); //배열추가
          console.log("이름 : "+$("#name").val());
          let i_no = Math.max.apply(null,no)+1;
          let i_name = $("#name").val();
          let i_kor = $("#kor").val();
          let i_eng = $("#eng").val();
          let i_math = $("#math").val();
          let i_total = i_kor + i_eng + i_math;
          let i_avg = (total/3).toFixed(2); //소수점 2자리 반올림
          let i_rank = 0;
          // table tr 추가
          let htmlData ="";
               htmlData += "<tr id='"+i_no+"'>";
               htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value="+i_no+"></td>";
               htmlData += "<td>"+i_no+"</td>";
               htmlData += "<td>"+i_name+"</td>";
               htmlData += "<td>"+i_kor+"</td>";
               htmlData += "<td>"+i_eng+"</td>";
               htmlData += " <td>"+i_math+"</td>";
               htmlData += "<td>"+i_total+"</td>";
               htmlData += "<td>"+i_avg+"</td>";
               htmlData += "<td>0</td>";
               htmlData += "<td><button class='delBtn'>삭제</button></td>";
               htmlData += "</tr>";
          
     });//학생입력확인 버튼
     
     
     
     //html 소스를 tbody에 추가
     $("#body").html(htmlData);

     
     //전체선택
     $("#allChk").click(function(){
          if($(this).is(":checked") == true){
               //모든 체크박스 체크
               $(".stuChk").each(function(){
                    $(this).prop("checked",true);
               });

          }else{
               //모든 체크박스 해제
               $(".stuChk").each(function(){
                    $(this).prop("checked",false);
               });

          }
     });//전체 선택
     
     
     //table에 있는 삭제버튼 클릭
     $(".delBtn").click(function(){
          console.log("현재 선택된 class id : "+ $(this).parent().parent().attr("id"));
          if(confirm("정말 삭제하시겠습니까?")){
               $("#"+$(this).parent().parent().attr("id")).remove();
          }
     }); //table삭제
    
     //하단 학생삭제버튼 클릭
     $("#deleteBtn").click(function(){
          // //alert("test");
          console.log("체크박스 개수 : "+$(".stuChk").length);
          console.log("체크박스에서 체크된 개수 : "+$(".stuChk:checked").length);
          console.log("체크박스에서 체크된 개수 : "+$("input:checkbox[name='stu']:checked").length);

          //체크되어 있는 것이 없을 경우
          if($(".stuChk:checked").length<1){
               alert("삭제할 데이터를 체크해주셔야 가능합니다.");
               return false;
          }//체크if
          
          //현재 체크박스가 체크가 되어 있는지 확인
          if(!confirm("정말 삭제하시겠습니까?")){
               return false; // no버튼 클릭시 다시 돌아감. yes를 누르면 건너뜀.
          }//삭제if
          
          //모든 체크박스 가져오기
          $(".stuChk").each(function(){
    
               if($(this).is(":checked") == true){
                    console.log("현재 선택된 class 값 : "+ $(this).val());
                    console.log("현재 선택된 id 값 : "+ $(this).parent().parent().attr("id"));
                    $("#"+$(this).parent().parent().attr("id")).remove();
               }
          });//each
     
     
     });//하단 삭제 버튼





});//제이쿼리