
$(document).ready(function(){
    var type=new Typed('.typed',{
        strings:['Welcome...','You are not a Hacker','But You are Smart one',
    'You are not Hacking them','You Just Fooling Them','Thank You...'],
    typeSpeed:60,
    backSpeed:60,
    loop:true,
    // smartBackspace:60
    });

    $('ul li').click(function(){
        $('ul li').removeClass('home');
       $(this).addClass('home');
    });
    var msg=$('.msg');
   var ok=$('.ok');
   ok.click(function(){
    msg.empty();
    $('.notify').css('display','none');
    });
   if(msg.html())
   {
       $('.notify').css('display','block');
   }
   else
   {
        $('.notify').css('display','none');
   }
    $('.copy').click(function(){

         var text=$(this).parent().siblings('.link').html();
        var temp=$('<input>').val(text).appendTo('body').select();
        document.execCommand("copy");
        temp.remove();

    
    });  
    $('.delete').click(function(){
        $(this).parent().parent().parent().remove();
   }); 
//   var msg=$('.msg');
//   var ok=$('.ok');
//   ok.click(function(){
//    msg.empty();
//    $('.notify').css('display','none');
//    });
//   if(msg.html())
//   {
//       $('.notify').css('display','block');
//   }
//   else
//   {
//        $('.notify').css('display','none');
//   }

  
});     


