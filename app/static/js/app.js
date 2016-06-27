jQuery(document).foundation();

jQuery(document).ready(function () {
  jQuery('#scroll-to-form').click(function () {
    jQuery(window).scrollTo(450);
  });

  $('#registration').mask('000.000.000-00');
});
