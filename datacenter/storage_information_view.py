from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    people_in_storage = Visit.objects.filter(leaved_at=None)  
    non_closed_visits = []

    for visit in people_in_storage:
        visitor_name = visit.passcard.owner_name
        visitor_entered_at = visit.entered_at
        visit_duration = visit.get_format_duration()
        non_closed_visits.append({
            'who_entered': visitor_name,
            'entered_at': visitor_entered_at,
            'duration': visit_duration,
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
