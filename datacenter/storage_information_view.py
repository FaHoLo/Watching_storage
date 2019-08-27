from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    people_in_storage = Visit.objects.filter(leaved_at=None)  
    non_closed_visits = [collect_non_closed_visit_info(visit) for visit in people_in_storage]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

def collect_non_closed_visit_info(visit):
    visit_info = {
        'who_entered': visit.passcard.owner_name,
        'entered_at': visit.entered_at,
        'duration': visit.get_formatted_duration(),
    }
    return visit_info