from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import YogaRegistration, OnlineRegistration, OfflineRegistration
from django.conf import settings
import json
import traceback

def clean_date(date_str):
    try:
        return date_str[:10]
    except:
        return None

@csrf_exempt
def yoga_webhook(request):
    if request.method == "POST":
        if request.headers.get("X-GHL-TOKEN") != settings.GHL_SECRET:
            return JsonResponse({"error": "Unauthorized"}, status=401)
        try:
            data = json.loads(request.body)
            print("Incoming Yoga Data:", data)

            cleaned_data = {
                "first_name": data.get("first_name", ""),
                "last_name": data.get("last_name", ""),
                "email": data.get("email", ""),
                "phone": data.get("phone", ""),
                "registration_number": data.get("Registration number", ""),
                "branch": data.get("Radio 3quv", ""),
                "health_condition": data.get("Are any of these affecting currently you?", ""),
                "other_health_issues": data.get("Other", ""),
                "acknowledgement": "Agree" in data.get("I consent to the above statements and affirm my honesty regarding my health.", []),
                "submission_date": clean_date(data.get("Today's Date", "")),
                "terms_agreed": True,
                "date_of_birth": clean_date(data.get("date_of_birth", ""))
            }

            YogaRegistration.objects.create(**cleaned_data)
            return JsonResponse({'status': 'yoga saved'})
        except Exception as e:
            print("❌ Error in Yoga Webhook:", str(e))
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def online_webhook(request):
    if request.method == "POST":
        if request.headers.get("X-GHL-TOKEN") != settings.GHL_SECRET:
            return JsonResponse({"error": "Unauthorized"}, status=401)
        try:
            data = json.loads(request.body)
            print("Incoming Online Data:", data)

            cleaned_data = {
                "first_name": data.get("first_name", ""),
                "last_name": data.get("last_name", ""),
                "email": data.get("email", ""),
                "phone": data.get("phone", ""),
                "date_of_birth": clean_date(data.get("date_of_birth", "")),
                "gender": data.get("What is your gender?", ""),
                "year_of_study": data.get("Year of Study", ""),
                "preferred_contact_method": data.get("Preferred Contact Method:", ""),
                "fitness_goals": data.get("What are your primary fitness goals? ", []),
                "roll_no": data.get("Registration number", ""),
                "department": data.get("Radio 3quv", ""),
                "fitness_challenges": data.get("Do you have any specific fitness challenges or limitations we should be aware of?", ""),
                "gym_member_before": data.get("Have you been a member of a gym before?", ""),
                "terms_agreed": "Agree" in data.get("I consent to the above statements and affirm my honesty regarding my health.", []),
            }

            OnlineRegistration.objects.create(**cleaned_data)
            return JsonResponse({'status': 'online saved'})
        except Exception as e:
            print("❌ Error in Online Webhook:", str(e))
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def offline_webhook(request):
    if request.method == "POST":
        if request.headers.get("X-GHL-TOKEN") != settings.GHL_SECRET:
            return JsonResponse({"error": "Unauthorized"}, status=401)
        try:
            data = json.loads(request.body)
            print("Incoming Offline Data:", data)

            cleaned_data = {
                "first_name": data.get("first_name", ""),
                "last_name": data.get("last_name", ""),
                "email": data.get("email", ""),
                "phone": data.get("phone", ""),
                "date_of_birth": clean_date(data.get("date_of_birth", "")),
                "gender": data.get("What is your gender?", ""),
                "year_of_study": data.get("Year of Study", ""),
                "preferred_contact_method": data.get("Preferred Contact Method:", ""),
                "fitness_goals": data.get("What are your primary fitness goals? ", []),
                "roll_no": data.get("Registration number", ""),
                "department": data.get("Radio 3quv", ""),
                "fitness_challenges": data.get("Do you have any specific fitness challenges or limitations we should be aware of?", ""),
                "gym_member_before": data.get("Have you been a member of a gym before?", ""),
                "terms_agreed": "Agree" in data.get("I consent to the above statements and affirm my honesty regarding my health.", []),
            }

            OfflineRegistration.objects.create(**cleaned_data)
            return JsonResponse({'status': 'offline saved'})
        except Exception as e:
            print("❌ Error in Offline Webhook:", str(e))
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)
