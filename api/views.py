from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User


from django.http.request import HttpHeaders
from django.shortcuts import render

from django.http import HttpResponse
import requests
import json


from django.shortcuts import render

class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]
    # get list of all existing users
    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    # create new user
    def post(self, request):
        # print(f'\n post_invoked: {data} \n')
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )












# def send_notification(registration_ids , message_title , message_desc):
#     fcm_api = ""
#     url = "https://fcm.googleapis.com/fcm/send"
    
#     headers = {
#     "Content-Type":"application/json",
#     "Authorization": 'key='+fcm_api}

#     payload = {
#         "registration_ids" :registration_ids,
#         "priority" : "high",
#         "notification" : {
#             "body" : message_desc,
#             "title" : message_title,
#             "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
#             "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
#         }
#     }

#     result = requests.post(url,  data=json.dumps(payload), headers=headers )
#     print(result.json())





# def index(request):
#     return render(request , 'index.html')

# def send(request):
#     resgistration  = [
#     ]
#     send_notification(resgistration , 'Code Keen added a new video' , 'Code Keen new video alert')
#     return HttpResponse("sent")




# def showFirebaseJS(request):
#     data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
#          'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
#          'var firebaseConfig = {' \
#             apiKey: "",\
# authDomain: "",\
# projectId: "",\
# storageBucket: "",\
# messagingSenderId: "",\
# appId: "",\
# measurementId: "G-VZW1GPHPMJ"\
#          '        apiKey: "AIzaSyDj4xR6oaa7ylG2NmOc4R40FU_h3YmzT4k",' \
#          '        authDomain: "uzme-aec88.firebaseapp.com",' \
#          '        databaseURL: "uzme-aec88.appspot.com",' \
#          '        projectId: "uzme-aec88",' \
#          '        storageBucket: "557984028016",' \
#          '        messagingSenderId: "1:557984028016:web:101b8e8364cfe7783f2bb5",' \
#          '        appId: "",' \
#          '        measurementId: ""' \
#          ' };' \
#          'firebase.initializeApp(firebaseConfig);' \
#          'const messaging=firebase.messaging();' \
#          'messaging.setBackgroundMessageHandler(function (payload) {' \
#          '    console.log(payload);' \
#          '    const notification=JSON.parse(payload);' \
#          '    const notificationOption={' \
#          '        body:notification.body,' \
#          '        icon:notification.icon' \
#          '    };' \
#          '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
#          '});'

#     return HttpResponse(data,content_type="text/javascript")