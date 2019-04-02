/* This JS integrates jquery.galleryview with the EEA site. */
(function($) {
    /* wrap code in self calling anonymous function with $ as parameter
      to avoid namespace polution and conflicts with libraries that use $ */
    $(document).ready(function() {
        if ($.fn.galleryView !== undefined) {
            $.fn.eeaGalleryView = function(gallery_opts) {
                return this.each(function() {
                    if ($.data(this, 'visited')) {
                        return;
                    }
                    var $this = $(this);
                    var $gallery_parent = $this.parent(),
                        $gallery_class = $gallery_parent[0].className,
                        parent_width, parent_height,
                        gallery_width, gallery_height;
                    parent_width = $gallery_parent.width() - 10;
                    parent_height = Math.round((parent_width / 4) * 3);
                    gallery_width = $gallery_class === 'gallery_fancybox_view' ? 640 : parent_width;
                    gallery_height = $gallery_class === 'gallery_fancybox_view' ? 433 : parent_height;

                    var defaults = {
                        panel_width: gallery_width,
                        panel_height: gallery_height,
                        show_filmstrip: true,
                        show_filmstrip_nav: true,
                        fade_panels: false,
                        frame_width: 50,
                        frame_height: 50,
                        transition_speed: 350,
                        transition_interval: 10000
                    };
                    var gal_options = $.extend(defaults, gallery_opts);

                    $this.galleryView(gal_options);
                    $.data(this, 'visited', 'true');
                });

            };
            $("#galleryView, .galleryView").each(function(idx, el) {
                var gal_opts = {};
                if (el.className.indexOf('js-noFilmstrip') !== -1) {
                    gal_opts.show_filmstrip = false;
                    gal_opts.fade_panels = true;
                    gal_opts.show_filmstrip_nav = false;
                    gal_opts.keep_nav_buttons_visible = true;
                }
                if (!$.isEmptyObject(gal_opts)) {
                    $(el).eeaGalleryView(gal_opts);
                }
                else {
                    $(el).eeaGalleryView();
                }
            });
        }
    });
}(jQuery));