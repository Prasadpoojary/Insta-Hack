$(document).ready(function(){
    $('.editbtn').click(function(){
      $('#email').css({'pointer-events':'visible',
     'border-bottom':'2px solid #03157e',
     'height':'40px'}).focus();
     $('#save').css('visibility','visible');
    });

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
    $('.cpbtn').click(function(){
        if($(this).html()=='Change Password')
        {
        $(this).css('transition','.3s ease-out');
        $(this).html('X');
        $('.form').css({'display':'block','transition':'.3s ease-out'});
        $('.changeP').css({'transition':'.3s ease-out','box-shadow':'0px 0px 10px 0px #01043a','transform':'translateY(-20px)'});
        $(this).addClass('cpsextrabtn');
        }
       else
        {
        $(this).css('transition','none');
        $(this).html('Change Password');
        $('.form').css({'display':'none','transition':'none'});
        $('.changeP').css({'transition':'none','box-shadow':'unset','transform':'translateY(10px)'});
        $(this).removeClass('cpsextrabtn');
        }
    });

});