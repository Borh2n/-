from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Field
from .serializers import FieldSerializer, BookingSerializer
from django.db.models import Q
from django.shortcuts import render


@api_view(['GET'])
def get_field_availability(request):
    location = request.query_params.get('location')
    filters = Q(availability=True)

    if location:
        filters &= Q(location__icontains=location)

    fields = Field.objects.filter(filters)
    serializer = FieldSerializer(fields, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def book_field(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Booking successful!"})
    return Response(serializer.errors, status=400)


def home(request):
    return render(request, 'booking/home.html') 
