from points.forms import PointForm

form = PointForm()

def ol_media(request):
    '''provides the media for an olwidget for maps data being dyn-ajax

    '''

    return {
            'points_form_media': form.media.render(),

            }
