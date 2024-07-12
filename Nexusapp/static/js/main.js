'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");
    });

    /*------------------
        main banner Background 
    --------------------*/
    $('.main-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });
    
    //Canvas Menu
    $(".canvas__open").on('click', function () {
        $(".offcanvas-menu-wrapper").addClass("active");
        $(".offcanvas-menu-overlay").addClass("active");
    });

    $(".offcanvas-menu-overlay").on('click', function () {
        $(".offcanvas-menu-wrapper").removeClass("active");
        $(".offcanvas-menu-overlay").removeClass("active");
    });

    //Accordin Active
    $('.collapse').on('shown.bs.collapse', function () {
        $(this).prev().addClass('active');
    });

    $('.collapse').on('hidden.bs.collapse', function () {
        $(this).prev().removeClass('active');
    });

    /*Navigation*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    // 
    var testimonialSlider = $(".testimonial__slider");
    testimonialSlider.owlCarousel({
        loop: true,
        margin: 0,
        items: 3,
        dots: true,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: false,
        responsive: {
            992: {
                items: 3
            },
            768: {
                items: 2
            },
            320: {
                items: 1
            }
        }
    });

    //mobile close navigation
    document.querySelector('.offcanvas__close').addEventListener('click', function() {
        document.querySelector('.offcanvas-menu-wrapper').classList.remove('active');
        document.querySelector('.offcanvas-menu-overlay').classList.remove('active');
    });
    $('.offcanvas__close').on('click', function() {
        $('.offcanvas-menu-wrapper').removeClass('active');
        $('.offcanvas-menu-overlay').removeClass('active');
    });
    
    /*
        Select
    */
    $("select").niceSelect();

    // Swiper

    document.addEventListener('DOMContentLoaded', (event) => {
        var swiper = new Swiper(".mySwiper", {
            spaceBetween: 30,
            effect: "fade",
            autoplay: {
                delay: 2000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
        });
    });
    
    
    /*------------------
        Counter Up
    --------------------*/
    $('.counter-add').each(function () {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 4000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });

})(jQuery);