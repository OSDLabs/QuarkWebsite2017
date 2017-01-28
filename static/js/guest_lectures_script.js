    $(document).ready(function() {
        $('.carousel').carousel();
        $('.carousel.carousel-slider').carousel({ full_width: true });

        $(document).keydown(function(e) {
            switch (e.which) {
                case 37: // left
                	$('.carousel').carousel('prev');
                    break;

                case 39: // right
                $('.carousel').carousel('next');
                    break;


                default:
                    return; // exit this handler for other keys
            }
            e.preventDefault(); // prevent the default action (scroll / move caret)
        });
    });
