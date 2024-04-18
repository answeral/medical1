//1.ajax stu_score 10개 데이터 출력
//4. 하생삭제 -> 선택된 학생이 삭제되게 구성


$(function(){
    
    let s_count =1; 
    //최초데이터 불러오기
    $.ajax({
        url:"file:///C:/workspace/medical1-1/students/stu_score.json",
        data:"",
        type:"get",
        dataType:"json",
        success:function(data){
            console.log(data.length);
            s_count = Number(data.length)
            let h_data = "";
            for(i=0; i<10; i++){
                
                h_data += "<tr>";
                h_data += " <td><input type='checkbox' name='stu' class='stuChk' value=''></td>";
                h_data += "<td>"+data[i].number+"</td>";
                h_data += "<td>"+data[i].name+"</td>";
                h_data += "<td>"+data[i].kor+"</td>";
                h_data += " <td>"+data[i].eng+"</td>";
                h_data += "<td>"+data[i].math+"</td>";
                h_data += "<td>"+data[i].total+"</td>";
                h_data += "<td>"+data[i].avg+"</td>";
                h_data += "<td>"+data[i].rank+"</td>";
                h_data += "<td><button class='delBtn'>삭제</button></td>";
                h_data += "</tr>";
            };//for
            $("#body").html(h_data);
        },//success
        error:function(){
            alert("실패")
        }
        
        
    });//ajax
    
    //2.학생입력 -> 학생추가 프로그램 구성
    
    //학생성적입력 
    //입력버튼
    $("#writeBtn").click(function(){
        $(".p_all").css("display","block");
        $(".p_main h2").text("학생성적입력");
        $("#name").prop("readonly",false);
        
        
    });//입력버튼
    //취소버튼
    
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
    });
    
    
    //성적입력
    //학생 입력 버튼
    $("#confirmBtn").on("click",function(){
        if($("#id").value == ""){
            console.log($("#name").val());
        }
        //공백확인
        if($("#name").val().length<2){
            alert("이름을 입력하셔야 등록이 가능합니다.");
            $("#name").focus(); //바로 입력창으로 커서를 옮기는 함수
            return false;
        }
        s_count = Number(s_count+1)
        //번호, 이름, 국, 영, 수, 총합, 평균, 랭크
        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = (i_kor+ i_eng+i_math);
        let i_avg = (i_total/3).toFixed(2);
        
        let h_data = "";
        h_data += "<tr>";
        h_data += " <td><input type='checkbox' name='stu' class='stuChk' value=''></td>";
        h_data += "<td>"+s_count+"</td>";
        h_data += "<td>"+i_name+"</td>";
        h_data += "<td>"+i_kor+"</td>";
        h_data += " <td>"+i_eng+"</td>";
        h_data += "<td>"+i_math+"</td>";
        h_data += "<td>"+i_total+"</td>";
        h_data += "<td>"+i_avg+"</td>";
        h_data += "<td>0</td>";
        h_data += "<td><button class='delBtn'>삭제</button></td>";
        h_data += "</tr>";
        
        $("#body").append(h_data);
        
    });//학생입력버튼
    
    //3.학생수정 -> 학생성적수정이 가능하게 구성
    // 수정 버튼(수정 버튼 눌렀을 때 1명만) -> 학생 점수 입력 (전 데이터 불러오기, 창에 text로 띄우기)
    $("#modifyBtn").click(function(){
        console.log("체크박스 체크 개수 : "+$(".stuChk:checked"));
        if($(".stuChk:checked")!=1){
            alert("1명만 체크하셔야 수정이 가능합니다.")
            return false;
        }//1명 체크

        //전 데이터 불러오기
        let o_id = $(".stuChk:checked").parent();
        let o_no = o_id.next().text();
        let o_name = o_id.next().next().text();
        let o_kor = o_id.next().next().next().text();
        let o_eng =o_id.next().next().next().next().text();
        let o_math =o_id.next().next().next().next().next().text();


        console.log("학번 : "+o_id.next().text());
    });//수정버튼

    //수정창 열기
    $(".p_all").css("display","block");
    $("#name").prop("readonly",true);

    






    // -> 입력한 점수로 저장시키기(새 데이터로 저장하기)
    
    
    
    
    
    
    


});//jquery