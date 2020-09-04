
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

#                                    Homapage
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

class home_view(APIView):

    template_name = 'homepage.html'

    def get(self, request):
        try:
            return render(request, self.template_name)
        
        except Exception as e:
            print ("Error : ", e)
            return Response({"Error" : "Inetrnal Error."})


