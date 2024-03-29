from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, StaffSerializer, StudentSerializer

# this code for login logout and register
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# those packages for change and reset password
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated 

from rest_framework.views import APIView
from app_attendance_system.models import Staff,CustomUser,Student

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })




class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


  

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# api for staff
class CustomResponse():
    def successResponse(self,code,msg,data = dict()):
        context = {
            'status_code':code,
            'message':msg,
            'data':data,
            'error':[]
        }
        return context
    
    def errorResponse(self,code, msg,error=dict()):
        context = {
            'code':code,
            'message':msg,
            'data':[],
            'error':error
        }
        return context
    

class StaffApiView(APIView):
    def get(self,request):
        staff=Staff.objects.all()
        
        serializer= StaffSerializer(staff,many=True)
        

        return Response(CustomResponse.successResponse(200,"Staff List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer= StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(CustomResponse.successResponse(200, "Added successfully."),status=status.HTTP_200_OK)
        else:
            return Response(CustomResponse.successResponse(200," Validation Error.", serializer.errors))
        
class StaffApiIdView(APIView):
    def get_object(self,request,id):
        try:
            data = Staff.objects.get(id=id)
            return data
        except Staff.DoesNotExist:
            return None
        
    def get(self,request,id):
        instance= self.get_object(id=id)
        
        if not instance:
            return Response({"msg":"Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer= StaffSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self,request,id):
        instance= self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found."},status=status.HTTP_404_NOT_FOUND)
        serializer=StaffSerializer(data=request,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        instance=self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found."},status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"msg":"Your Data Deleted Successfully."}, status= status.HTTP_200_OK)
    
# student api view
class StudentApiView(APIView):
    def get(self,request):
        student=Student.objects.all()
        
        serializer= StudentSerializer(student,many=True)
        

        return Response(CustomResponse.successResponse(200,"Student List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(CustomResponse.successResponse(200, "Added successfully."),status=status.HTTP_200_OK)
        else:
            return Response(CustomResponse.successResponse(200," Validation Error.", serializer.errors))
        
class StudentApiIdView(APIView):
    def get_object(self,id):
        try:
            data = Student.objects.get(id=id)
            return data
        except Student.DoesNotExist:
            return None
        
    def get(self,id):
        instance= self.get_object(id=id)
        
        if not instance:
            return Response({"msg":"Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer= StudentSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self,request,id):
        instance= self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found."},status=status.HTTP_404_NOT_FOUND)
        serializer=StudentSerializer(data=request,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        instance=self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found."},status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"msg":"Your Data Deleted Successfully."}, status= status.HTTP_200_OK)

    