from ast import arg
from email import message
from operator import index
import re
from django.shortcuts import redirect, render
from django.http  import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthlyChallenges = {
    "january": "getting to know each other",
    "february": "reading more",
    "march": "eat less carbs",
    "april": "drink less alchohol",
    "may": "Do more exercise",
    "june": "cookie challenge",
    "july": "challenge de la ballena",
    "august": "august challenge"
}

def index(request):
    list_items = ""
    months = list(monthlyChallenges.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"

    response_data = f"""
        <ul>
            {list_items}
        </ul>
    """
    return HttpResponse(response_data)

#redirecting urls
def monthly_challenge_by_number(request, month):
    months = list(monthlyChallenges.keys())
    
    if(month > len(months)):
        return HttpResponseNotFound("invalid month")
    
    redirected_month = months[month - 1]
    #now with the reverse function we can build dynamic URL, ot only needs the "constructor "path name + the args as shown in the next line
    redirect_path = reverse("month-challenge", args=[redirected_month])
    return HttpResponseRedirect(redirect_path);

# Create your views here.
def monthlyChallenge(request, month):
    try:
        challenge_text = f"<h1>{monthlyChallenges[month]}<h1>"
    except:
        return HttpResponseNotFound("<h1>Month not supported<h1>")
    
    return HttpResponse(challenge_text);