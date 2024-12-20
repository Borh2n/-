import unittest
import views

class TestViews(unittest.TestCase):
    def setUp(self):
        Field.objects.create(name="Field 1", location="Location A", availability=True)
        Field.objects.create(name="Field 2", location="Location B", availability=False)

    def test_field_availability(self):
        available_fields = Field.objects.filter(availability=True)
        self.assertEqual(available_fields.count(), 1)

    def test_field_location_filter(self):
        filtered_fields = Field.objects.filter(location__icontains="Location A", availability=True)
        self.assertEqual(filtered_fields.count(), 1)
