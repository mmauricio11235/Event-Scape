$(document).ready(function(){
	$('.attend').click(function(){
    var obj;
    obj = $(this).attr("data-event");
     $.get("/event/attend", {eid: obj}, function(data){
               if (data==='true'){
               		$(".jumbotron").append("<h1> ATTENDING </h1>")
               }

           });
});

});