$(document).ready(function(){
    var count=0;
    $('#fbArea').on('input',function(){
        count=$(this).val().length;
        $('.count').html(count);
        if(count>0 && count<=100)
        {
            $('.fbsb').css({'visibility':'visible',
            'transform':'translateY(5px)'});
            $('.count').css('color','#268f06');
        }
        else{
            $('.fbsb').css({'transform':'translateY(-5px)',
            'visibility':'hidden'});
            $('.count').css('color','red');
        }
    });
});