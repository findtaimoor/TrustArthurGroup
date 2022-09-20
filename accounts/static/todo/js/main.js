(function($) {
    "use strict";
    /*-------------------------------------
        Contact Form initiating
    -------------------------------------*/
    var contactForm = $('#contact-form');
    if (contactForm.length) {
        contactForm.validator().on('submit', function(e) {
            var $this = $(this),
                $target = contactForm.find('.form-response');
            if (e.isDefaultPrevented()) {
                $target.html("<div class='alert alert-danger'><p>Please select all required field.</p></div>");
            } else {
                $.ajax({
                    url: "php/form-process.php",
                    type: "POST",
                    data: contactForm.serialize(),
                    beforeSend: function() {
                        $target.html("<div class='alert alert-info'><p>Loading ...</p></div>");
                    },
                    success: function(response) {
                        var res = JSON.parse(response);
                        console.log(res);
                        if (res.success) {
                            $this[0].reset();
                            $target.html("<div class='alert alert-success'><p>Message has been sent successfully.</p></div>");
                        } else {
                            if (res.message.length) {
                                var messages = null;
                                res.message.forEach(function(message) {
                                    messages += "<p>" + message + "</p>";
                                });
                                $target.html("<div class='alert alert-success'><p>" + messages + "</p></div>");
                            }
                        }
                    },
                    error: function() {
                        $target.html("<div class='alert alert-success'><p>Error !!!</p></div>");
                    }
                });
                return false;
            }
        });
    }
    /*-------------------------------------
    Slick Slider
    -------------------------------------*/
    if ($('.slick-carousel').length) {
        $('.slick-carousel').slick();
    }
    /*-------------------------------------
    Wow Js
    -------------------------------------*/
    new WOW().init();
    /*-------------------------------------
Section background image
-------------------------------------*/
    imageFunction();

    function imageFunction() {

        $('[data-bg-image]').each(function() {
            var img = $(this).data('bg-image');
            $(this).css({
                backgroundImage: 'url(' + img + ')',
            });
        });
    }

    /*-------------------------------------
      Progress Bar Init
      --------------------------------------*/
    if ($.fn.circleProgress !== undefined) {

        $('.circle-progress').circleProgress({
            size: 160,
            thickness: 9,
            emptyFill: "#114d7f",
            fill: {
                color: "#fff"
            },
            startAngle: 0,
        }).on('circle-animation-progress', function(event, progress) {
            var data_value = $(this).data('value');
            var data_value_full = data_value * 100;
            $(this).find('span').html(Math.round(data_value_full * progress) + '<i>%</i>');
        });
    }
    /*-------------------------------------
        Sal Init
    -------------------------------------*/
    if (typeof sal === 'function') {
        sal({
            threshold: 0.05,
            once: true
        });

        if ($(window).outerWidth() < 1025) {
            var scrollAnimations = sal();
            scrollAnimations.disable();
        }
    }

    /*-------------------------------------
    Jquery Serch Box
    -------------------------------------*/
    $('a[href="#header-search"]').on("click", function(event) {
        event.preventDefault();
        var target = $("#header-search");
        target.addClass("open");
        setTimeout(function() {
            target.find('input').focus();
        }, 600);
        return false;
    });

    $("#header-search, #header-search button.close").on("click keyup", function(event) {
        if (
            event.target === this ||
            event.target.className === "close" ||
            event.keyCode === 27
        ) {
            $(this).removeClass("open");
        }
    });
    /*-------------------------------------
    Page Preloader
    -------------------------------------*/
    $("#preloader").fadeOut("slow", function() {
        $(this).remove();
    });

    /*---------------------------------------
    On Click Section Switch
    --------------------------------------- */
    $('[data-type="section-switch"]').on('click', function() {
        if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && location.hostname === this.hostname) {
            var target = $(this.hash);
            if (target.length > 0) {

                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });
    /*-------------------------------------
    On Scroll 
    -------------------------------------*/
    $(window).on('scroll', function() {

        // Back Top Button
        if ($(window).scrollTop() > 500) {
            $('.scrollup').addClass('back-top');
        } else {
            $('.scrollup').removeClass('back-top');
        }
        // Sticky Header
        if ($('body').hasClass('sticky-header')) {
            var stickyPlaceHolder = $("#rt-sticky-placeholder"),
                menu = $("#header-menu"),
                menuH = menu.outerHeight(),
                topHeaderH = $('#header-topbar').outerHeight() || 0,
                middleHeaderH = $('#header-middlebar').outerHeight() || 0,
                targrtScroll = topHeaderH + middleHeaderH;
            if ($(window).scrollTop() > targrtScroll) {
                menu.addClass('rt-sticky');
                stickyPlaceHolder.height(menuH);
            } else {
                menu.removeClass('rt-sticky');
                stickyPlaceHolder.height(0);
            }
        }
    });

    /*-------------------------------------
        Google Map
    -------------------------------------*/
    if ($("#googleMap").length) {
        window.onload = function() {
            var styles = [{
                featureType: 'water',
                elementType: 'geometry.fill',
                stylers: [{
                    color: '#b7d0ea'
                }]
            }, {
                featureType: 'road',
                elementType: 'labels.text.fill',
                stylers: [{
                    visibility: 'off'
                }]
            }, {
                featureType: 'road',
                elementType: 'geometry.stroke',
                stylers: [{
                    visibility: 'off'
                }]
            }, {
                featureType: 'road.highway',
                elementType: 'geometry',
                stylers: [{
                    color: '#c2c2aa'
                }]
            }, {
                featureType: 'poi.park',
                elementType: 'geometry',
                stylers: [{
                    color: '#b6d1b0'
                }]
            }, {
                featureType: 'poi.park',
                elementType: 'labels.text.fill',
                stylers: [{
                    color: '#6b9a76'
                }]
            }];
            var options = {
                mapTypeControlOptions: {
                    mapTypeIds: ['Styled']
                },
                center: new google.maps.LatLng(-31.81618, 144.95692),
                zoom: 10,
                disableDefaultUI: true,
                mapTypeId: 'Styled'
            };
            var div = document.getElementById('googleMap');
            var map = new google.maps.Map(div, options);
            var styledMapType = new google.maps.StyledMapType(styles, {
                name: 'Styled'
            });
            map.mapTypes.set('Styled', styledMapType);

            var marker = new google.maps.Marker({
                position: map.getCenter(),
                animation: google.maps.Animation.BOUNCE,
                icon: '../static/todo/img/map-marker.png',
                map: map
            });
        };
    }

    /*-------------------------------------
    MeanMenu activation code
    --------------------------------------*/
    if ($.fn.meanmenu) {
        $('nav#dropdown').meanmenu({
            siteLogo: "<div class='mobile-menu-nav-back'><a class='logo-mobile' href=''><div class='lgo-img-t'></div></a></div>"
        });
    }
    /*-------------------------------------
    Offcanvas Menu activation code
    -------------------------------------*/
    $('#wrapper').on('click', '.offcanvas-menu-btn', function(e) {
        e.preventDefault();
        var $this = $(this),
            wrapper = $(this).parents('body').find('>#wrapper'),
            wrapMask = $('<div />').addClass('offcanvas-mask'),
            offCancas = $('#offcanvas-wrap'),
            position = offCancas.data('position') || 'left';

        if ($this.hasClass('menu-status-open')) {
            wrapper.addClass('open').append(wrapMask);
            $this.removeClass('menu-status-open').addClass('menu-status-close');
            offCancas.css({
                'transform': 'translateX(0)'
            });
        } else {
            removeOffcanvas();
        }

        function removeOffcanvas() {
            wrapper.removeClass('open').find('> .offcanvas-mask').remove();
            $this.removeClass('menu-status-close').addClass('menu-status-open');
            if (position === 'left') {
                offCancas.css({
                    'transform': 'translateX(-105%)'
                });
            } else {
                offCancas.css({
                    'transform': 'translateX(105%)'
                });
            }
        }
        $(".offcanvas-mask, .offcanvas-close").on('click', function() {
            removeOffcanvas();
        });

        return false;
    });

    /*-------------------------------------
    Carousel slider initiation
    -------------------------------------*/
    $(".rc-carousel").each(function() {
        var carousel = $(this),
            loop = carousel.data("loop"),
            Canimate = carousel.data("animate"),
            items = carousel.data("items"),
            margin = carousel.data("margin"),
            stagePadding = carousel.data("stage-padding"),
            autoplay = carousel.data("autoplay"),
            autoplayTimeout = carousel.data("autoplay-timeout"),
            smartSpeed = carousel.data("smart-speed"),
            dots = carousel.data("dots"),
            nav = carousel.data("nav"),
            navSpeed = carousel.data("nav-speed"),
            rXsmall = carousel.data("r-x-small"),
            rXsmallNav = carousel.data("r-x-small-nav"),
            rXsmallDots = carousel.data("r-x-small-dots"),
            rXmedium = carousel.data("r-x-medium"),
            rXmediumNav = carousel.data("r-x-medium-nav"),
            rXmediumDots = carousel.data("r-x-medium-dots"),
            rSmall = carousel.data("r-small"),
            rSmallNav = carousel.data("r-small-nav"),
            rSmallDots = carousel.data("r-small-dots"),
            rMedium = carousel.data("r-medium"),
            rMediumNav = carousel.data("r-medium-nav"),
            rMediumDots = carousel.data("r-medium-dots"),
            rLarge = carousel.data("r-large"),
            rLargeNav = carousel.data("r-large-nav"),
            rLargeDots = carousel.data("r-large-dots"),
            rExtraLarge = carousel.data("r-extra-large"),
            rExtraLargeNav = carousel.data("r-extra-large-nav"),
            rExtraLargeDots = carousel.data("r-extra-large-dots"),
            center = carousel.data("center"),
            custom_nav = carousel.data("custom-nav") || "";
        carousel.addClass('owl-carousel');
        var owl = carousel.owlCarousel({
            loop: loop ? true : false,
            animateOut: Canimate,
            items: items ? items : 1,
            lazyLoad: true,
            margin: margin ? margin : 0,
            autoplay: autoplay ? true : false,
            autoplayTimeout: autoplayTimeout ? autoplayTimeout : 1000,
            smartSpeed: smartSpeed ? smartSpeed : 250,
            dots: dots ? true : false,
            nav: nav ? true : false,
            navText: [
                '<i class="fa fa-angle-left" aria-hidden="true"></i>',
                '<i class="fa fa-angle-right" aria-hidden="true"></i>'
            ],
            navSpeed: navSpeed ? true : false,
            center: center ? true : false,
            responsiveClass: true,
            responsive: {
                0: {
                    items: rXsmall ? rXsmall : 1,
                    nav: rXsmallNav ? true : false,
                    dots: rXsmallDots ? true : false
                },
                576: {
                    items: rXmedium ? rXmedium : 1,
                    nav: rXmediumNav ? true : false,
                    dots: rXmediumDots ? true : false
                },
                768: {
                    items: rSmall ? rSmall : 1,
                    nav: rSmallNav ? true : false,
                    dots: rSmallDots ? true : false
                },
                992: {
                    items: rMedium ? rMedium : 1,
                    nav: rMediumNav ? true : false,
                    dots: rMediumDots ? true : false
                },
                1200: {
                    items: rLarge ? rLarge : 5,
                    nav: rLargeNav ? true : false,
                    dots: rLargeDots ? true : false
                },
                1240: {
                    items: rExtraLarge ? rExtraLarge : 5,
                    nav: rExtraLargeNav ? true : false,
                    dots: rExtraLargeDots ? true : false
                }
            },
        });

        if (custom_nav) {
            var nav = $(custom_nav),
                nav_next = $(".rt-next", nav),
                nav_prev = $(".rt-prev", nav);

            nav_next.on("click", function(e) {
                e.preventDefault();
                owl.trigger('next.owl.carousel');
                return false;
            });

            nav_prev.on("click", function(e) {
                e.preventDefault();
                owl.trigger('prev.owl.carousel');
                return false;
            });
        }
    });
    
    $(".toggle-password").click(function() {
        var input = $($(this).attr("toggle"));
        if (input.attr("type") == "password") {
            $(".toggle-password").text("Hide")
            input.attr("type", "text");
        } else {
            $(".toggle-password").text("Show")
            input.attr("type", "password");
        }
      });
})(jQuery);

//  ========================
//  Sign In
//  ========================
// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
//     container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
//     container.classList.remove("right-panel-active");
// });
// ---------------------
