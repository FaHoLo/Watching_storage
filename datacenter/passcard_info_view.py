from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits_of_pass = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = [collect_visit_info(visit) for visit in visits_of_pass]

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

def collect_visit_info(visit):
    visit_info = {
            'entered_at': visit.entered_at,
            'duration': visit.get_formatted_duration(),
            'is_strange': is_visit_long(visit),
    }
    return visit_info

def is_visit_long(visit, strange_visit_limit=3600):
    visit_duration = visit.get_duration().seconds    
    return visit_duration >= strange_visit_limit
