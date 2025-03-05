$(document).ready(function(){
    $('.slider').slick({
        dots: true,        // Show navigation dots
        infinite: true,    // Infinite loop
        speed: 650,        // Transition speed
        slidesToShow: 1,   // Number of slides visible
        autoplay: true,    // Auto-play enabled
        autoplaySpeed: 2000, // 2 seconds per slide
        arrows: true       // Enable next/prev arrows
    });
});