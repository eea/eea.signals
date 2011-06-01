/* This JS integrates jquery.galleryview with the EEA site. */
(function($) {
    /* wrap code in self calling anonymous function with $ as parameter
      to avoid namespace polution and conflicts with libraries that use $ */
$(document).ready(function() {
    if ($.fn.galleryView !== undefined) {
        $('#galleryView').galleryView({
            panel_width: 768,
            panel_height: 511,
            frame_width: 50,
            frame_height: 50,
            transition_speed: 350,
            transition_interval: 0
        });
    }
});
}(jQuery));
