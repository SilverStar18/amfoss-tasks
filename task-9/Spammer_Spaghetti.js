var x = 0 ;
var spam = setInterval(function()
{
    document.getElementsByClassName("composer_rich_textarea")[0].innerHTML = "Hi" ;
    $('.im_submit').trigger('mousedown');
    x++;
    if (x == 666)            
    {
        clearInterval(spam)
    }

}, 1000) ;

