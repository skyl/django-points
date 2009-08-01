$(function () {
    $('form#edit-point').submit( function() {
        $('input#id_zoom').val(map.map.getZoom());
    });
});
