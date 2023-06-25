(function ($) {
    'use strict';
    $(function () {
        $('[data-toggle="offcanvas"]').on("click", function () {
            $('.sidebar-offcanvas').toggleClass('active')
        });
    });
})(jQuery);

function rotateIcon() {
    var icon = document.getElementById('icn');

    // Create a clone of the icon element
    var clonedIcon = icon.cloneNode(true);

    // Replace the icon element with its clone
    icon.parentNode.replaceChild(clonedIcon, icon);

    // Toggle the rotation class on the cloned icon
    clonedIcon.classList.toggle('rotate');
}