$('#search_box').focus(function()
{
    $(this).attr('data-default', $(this).width());
    $(this).animate({ width: 150 }, 'fast');
}).blur(function()
{
    var w = $(this).attr('data-default');
    $(this).animate({ width: w }, 'fast');
});
