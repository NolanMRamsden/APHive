$("[class^='use']").click(function () {
    console.log('clicked');
    $(this).siblings().removeClass('review-underline');
    $(this).toggleClass('review-underline');
 });

$("[class^='docs']").click(function () {
    console.log('clicked');
    $(this).siblings().removeClass('review-underline');
    $(this).toggleClass('review-underline');
 });

$("[class^='rel']").click(function () {
    console.log('clicked');
    $(this).siblings().removeClass('review-underline');
    $(this).toggleClass('review-underline');
 });
