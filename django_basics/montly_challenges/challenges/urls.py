from django.urls import URLPattern, path

from . import views;

urlpatterns = [
    #dynamic path query
    #<str: will defined the type of the query (str: string, int: integer and so on...)
    #the rederect URL needs to be first in order to redirect to the final URL
    path("<int:month>", views.monthly_challenge_by_number),
                                                #this name is used to construct path URL's pointing at the URL specified( in this case "<str:month>")
    path("<str:month>", views.monthlyChallenge, name="month-challenge"),
    path("",  views.index, name="month-challenge")
]