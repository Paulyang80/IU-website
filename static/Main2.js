
function Search(){
    $(document).ready(function(){
        $.ajax({
        method :"GET",
        url:"/shopping/"+$("#ShopGo").val(),
        data: {"Shop":$("#ShopGo").val()},
        success:function(data){
        $("#ShopFinal").val(data);
        },
        error:function(){
            alert("HEHE")
        }
    });})
     }
    