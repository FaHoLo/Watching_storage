from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits_of_pass = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits_of_pass:
        visit_info = collect_visit_info(visit)
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

def collect_visit_info(visit):
    visitor_entered_at = visit.entered_at
    visit_duration = visit.get_format_duration()
    visit_is_strange = is_visit_long(visit)

    visit_info = {
            'entered_at': visitor_entered_at,
            'duration': visit_duration,
            'is_strange': visit_is_strange
        }
    return visit_info

def is_visit_long(visit):
    strange_visit_limit = 3600
    visit_duration = visit.get_duration().seconds    
    if visit_duration >= strange_visit_limit:
        return True
    else:
        return False
