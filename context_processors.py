from points.forms import PointForm

form = PointForm()

def ol_media(request):
    '''provides the media for an olwidget for maps data being dyn-ajax

    '''

    custom = '''
    <style>
        div#id_point_map { clear:both; }
    </style>

    <script>
        $(function () {
            $('form#edit-point').submit( function() {
                $('input#id_zoom').val(map.map.getZoom());
            });
        });
    </script>
    '''

    string = form.media.render() #+ custom

    return {
            'points_form_media': string,

            }
