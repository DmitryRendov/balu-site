$(function () {
    $('.tree li:has(ul)').addClass('parent_li').find(' > .leaf').attr('title', 'Свернуть эту ветвь');
    $('.tree li.parent_li > span').on('click', function (e) {
        var children = $(this).parent('li.parent_li').find(' > ul > li');
        if (children.is(":visible")) {
            children.hide('fast');
            $(this).attr('title', 'Развернуть эту ветвь').find(' > i').addClass('fa-plus').removeClass('fa-minus');
        } else {
            children.show('fast');
            $(this).attr('title', 'Свернуть эту ветвь').find(' > i').addClass('fa-minus').removeClass('fa-plus');
        }
        //FixMe: Add folder-open-close behaviour

        //var isFolder = $(this).find(' > i').hasClass("fa-folder-open") ;

        e.stopPropagation();
    });
});