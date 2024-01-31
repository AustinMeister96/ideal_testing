from .models import Mandatory_questionaire

def mandatory_questionaire(request):
    participant_id = request.GET.get('participant_id')
    first_name = 'Martin'
    try:
        mandatory_questionaire = Mandatory_questionaire.objects.get(participant_num_id=participant_id)
    except Mandatory_questionaire.DoesNotExist:
        mandatory_questionaire = None

    return {'mandatory_questionaire': mandatory_questionaire}