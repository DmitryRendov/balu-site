;(function( window, undefined ){ 
 'use strict'; 
/*!
 * IE10 viewport hack for Surface/desktop Windows 8 bug
 * Copyright 2014 Twitter, Inc.
 * Licensed under the Creative Commons Attribution 3.0 Unported License. For
 * details, see http://creativecommons.org/licenses/by/3.0/.
 */

// See the Getting Started docs for more information:
// http://getbootstrap.com/getting-started/#support-ie10-width

(function () {
  'use strict';
  if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
    var msViewportStyle = document.createElement('style');
    msViewportStyle.appendChild(
      document.createTextNode(
        '@-ms-viewport{width:auto!important}'
      )
    );
    document.querySelector('head').appendChild(msViewportStyle);
  }
})();
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
}( window ));