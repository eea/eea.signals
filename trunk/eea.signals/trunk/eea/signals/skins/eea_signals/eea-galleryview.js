/* This JS integrates jquery.galleryview with the EEA site. */
(function($) {
    /* wrap code in self calling anonymous function with $ as parameter
      to avoid namespace polution and conflicts with libraries that use $ */
$(document).ready(function() {
    if ($.fn.galleryView !== undefined) {
        var $gallery_view = $('#galleryView'),
            $gallery_parent, $gallery_class,
            parent_width, parent_height,
            gallery_width, gallery_height;
        if ($gallery_view.length ) {
            $gallery_parent = $gallery_view.parent();
            $gallery_class = $gallery_parent[0].className;

            parent_width = $gallery_parent.width() - 10;
            parent_height = Math.round((parent_width /4)*3);
            gallery_width = $gallery_class === 'gallery_fancybox_view' ? 640 : parent_width;
            gallery_height = $gallery_class === 'gallery_fancybox_view' ? 433 : parent_height;
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
