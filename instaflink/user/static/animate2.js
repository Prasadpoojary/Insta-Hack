$(window).on('load',function(){
    $('.loading').css('display','none');
});
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

    $(window).scroll(function(){ 
        var scrollVal=$(document).scrollTop();
        if(scrollVal>=45)
        {
            $('.downAnimation').css('display','none');
        }
    });

    function Preview(inp)
    {
        if(inp.files && inp.files[0])
        {
            var reader=new FileReader();
            reader.onload=function(e)
            {
                $('.profile').attr('src',e.target.result);
            };
            reader.readAsDataURL(inp.files[0]);
        }
    }
    $('.profileAdd').click(function(){
        $('#Prof').click();
    });
    $('#Prof').on('change',function(){
        Preview(this);
    });

   


});