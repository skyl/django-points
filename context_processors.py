from points.forms import PointForm

form = PointForm()

def ol_media(request):
    '''provides the media for an olwidget for maps data being dyn-ajax

    '''
    string = form.media.render()

    return {
        'points_form_media': string,
    }

def GAK(request):
    ''' Provides settings.GOOGLE_API_KEY as GAK

    '''

    from django.conf import settings
    GAK = settings.GOOGLE_API_KEY
    return {
            'GAK': GAK
    }
