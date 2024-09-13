document.addEventListener("DOMContentLoaded", function() {
    var swiper = new Swiper(".mySwiper", {
        spaceBetween: 30,
        loop: true,
        autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
        pagination: {
          el: ".swiper-pagination",
          dynamicBullets: true,
        },
      });
  });