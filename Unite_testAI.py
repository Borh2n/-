from django.test import TestCase, Client
from rest_framework import status
from .models import Field, Booking

class FieldAPITests(TestCase):

    def setUp(self):
        self.client = Client()
        self.field = Field.objects.create(name='Field1', location='Location1', availability=True)

    def test_get_field_availability(self):
        response = self.client.get('/api/fields/', {'location': 'Location1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Field1')

    def test_book_field(self):
        data = {
            'field': self.field.id,
            'date': '2024-12-20',
            'time_slot': '10:00-11:00',
            'user': 'User1'
        }
        response = self.client.post('/api/fields/book/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Booking successful!')

        # Check that the booking was actually created
        self.assertTrue(Booking.objects.filter(field=self.field, date='2024-12-20', time_slot='10:00-11:00').exists())
