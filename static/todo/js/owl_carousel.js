var temp = 4;
if (temp > 3) {
  $(function () {
    // Owl Carousel
    var owl = $(".owl-carousel");
    owl.owlCarousel({
      autoplay: true,
      items: 4,
      margin: 10,
      loop: true,
      nav: false,
      dots: true,
      autoplayTimeout: 5000,
      autoplayHoverPause: true,
      responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: false,
            loop: true,
            autoplay: true,
        },
        1000: {
            items: 4,
            nav: false,
            loop: true,
            autoplay: true,
        }
    }
    });
  });
} else {
}
