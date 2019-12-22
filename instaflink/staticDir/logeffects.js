$(window).on('load',function(){
    $('.loading').css('display','none');
});
$(document).ready(function(){
    $('#password').on('blur',function(){
        $('.submitButton').addClass('animation');
    })

    $('.logo').click(function(){
        $(this).siblings('input').attr('type','text');
        $(this).css('display','none');
        $(this).siblings('.offLogo').css('display','block');
    });
    $('.offLogo').click(function(){
        $(this).siblings('input').attr('type','password');
        $(this).css('display','none');
        $(this).siblings('.logo').css('display','block');
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
 
    
});