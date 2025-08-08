from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from studentsapp.models import Student
from studentsapp.serializers import StudentSerializer
# Create your views here.


class StudentInsertView(APIView):

    def post(self, request):
        print("in POST Method")
        # Save or update student data here
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student data saved successfully!"}, status=201)
       
        return Response(serializer.errors, status=400)
    
    def put(self, request):
        print("in PUT Method")
        # Update student data here
        roll = request.GET.get('roll')
        if roll:
            try:
                student = Student.objects.get(roll_no=roll)
                serializer = StudentSerializer(student, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Student data updated successfully!"}, status=200)
                return Response(serializer.errors, status=400)
            except Exception as e:
                return Response({"error": str(e)}, status=404)
        else:
            return Response({"error": "Roll number is required"}, status=400)
        
    def patch(self, request):
        print("in PATCH Method")
        # Update student data here
        roll = request.GET.get('roll')
        if roll:
            try:
                student = Student.objects.get(roll_no=roll)
                serializer = StudentSerializer(student, data=request.data , partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Student data updated successfully!"}, status=200)
                return Response(serializer.errors, status=400)
            except Exception as e:
                return Response({"error": str(e)}, status=404)
        else:
            return Response({"error": "Roll number is required"}, status=400)



class StudentGetView(APIView):

    def get(self, request):
        print("in GET Method")
        # Retrieve single student data here
        roll = request.GET.get('roll')
        print(f"Roll number received: {roll}")
        if roll:
            try:
                student = Student.objects.get(roll_no=roll)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=200)
            except Exception as e:
                return Response({"error": str(e)}, status=404)

        else:
            return Response({"error": "Roll number is required"}, status=400)
        

class StudentGetAllView(APIView):

    def get(self, request):
        print("in GET ALL Method")
        # Retrieve all students data here
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=200)
    

class StudentDeleteView(APIView):
    def delete(self, request):
        print("in DELETE Method")
        roll = request.GET.get('roll')
        print(f"Roll number received for deletion: {roll}")
        if roll:
            try:
                student = Student.objects.get(roll_no=roll)
                student.delete()
                return Response({"message": "Student deleted successfully!"}, status=204)
            except Exception as e:
                return Response({"error": str(e)}, status=404)
        else:
            return Response({"error": "Roll number is required"}, status=400)


class TaskforRachana(APIView):
    # This class is for testing purposes only, as per the request.
    # write add two number logic accepts two numbers in request body and returns the sum.
    def get(self, request):
        pass

    def post(self, request):
        pass

# write your own task inside a class TaskforRachana


class TaskforAnushka(APIView):
    def get(self,request):
        return Response("Task completed!")

class sakshidemoview(APIView):
    def get(self, request):
        return Response("this is a get request")
    

