/* This JS integrates jquery.galleryview with the EEA site. */
(function($) {
    /* wrap code in self calling anonymous function with $ as parameter
      to avoid namespace polution and conflicts with libraries that use $ */
$(document).ready(function() {
    if ($.fn.galleryView !== undefined) {
        var $gallery_view = $('#galleryView');
        if ($gallery_view.length ) {
            var $gallery_parent = $gallery_view.parent();
            var $gallery_class = $gallery_parent[0].className;
            var gallery_width = $gallery_class === 'gallery_fancybox_view' ? 640 : 613;
            var gallery_height = $gallery_class === 'gallery_fancybox_view' ? 433 : 413;
            $('#galleryView').galleryView({
                panel_width: gallery_width,
                panel_height: gallery_height,
                frame_width: 50,
                frame_height: 50,
                transition_speed: 350, 
                transition_interval: 10000
            });
        }
    }
});
}(jQuery));
