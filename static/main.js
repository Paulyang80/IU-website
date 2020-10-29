
function SearchGo(){
    $(document).ready(function(){
        $.ajax({
        method :"GET",
        url:"/"+$("#sendData").val(),
        data: {"Search":$("#sendData").val()},
        success:function(data){
        $("#sendData").val(data);
        },
        error:function(){
            alert("HEHE")
        }       
    });})
     }
    