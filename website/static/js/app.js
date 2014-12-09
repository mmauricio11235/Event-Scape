$(document).ready(function(){
	$('.attend').click(function(){
    var obj;
    obj = $(this).attr("data-event");
     $.get("/event/attend", {eid: obj}, function(data){
               if (data==='true' && $(".titleOfEvent").children().size() < 2){
               		$(".titleOfEvent").append("<h2 style = 'text-align: center;color: blue;'> Attending! </h2>")
               }

           });
});

$('.follow').click(function(){
    var obj;
    obj = $(this).attr("user-id");
     $.get("/user/follow", {uid: obj}, function(data){
               if (data==='true'){
               		window.alert("Working");
               }
               else{
               	window.alert(data);	
               }

           });
});

});