from odoo.tests.common import TransactionCase

class TestRealEstateProperty(TransactionCase):
    def setUp(self):
        """
        Set up test data.
        """
        super(TestRealEstateProperty, self).setUp()
        
        # Create a test property
        self.property = self.env['real_estate_property'].create({
            'name': 'Test Property',
            'description': 'This is a test property',
            'price': 100000.0,
            'living_area': 120,
            'bedrooms': 3,
            'bathrooms': 2,
            'garage': True,
            'garden': False,
            'garden_area': 0.0,
            'availability_date': '2023-12-31',
            'postcode': '12345',
            'state': 'draft',
            'property_type': 'apartment',
        })

    def test_property_creation(self):
        """
        Test that a property is created correctly.
        """
        property_id=self.property
        self.assertRecordValues(property_id,[{
            'name': 'Test Property',
            'description': 'This is a test property',
            'price': 100000.0,
            'living_area': 120,
            'bedrooms': 3,
            'bathrooms': 2,
            'garage': True,
            'garden': False,
            'garden_area': 0.0,
            'availability_date': '2023-12-31',
            'postcode': '12345',
            'state': 'draft',
            'property_type': 'apartment',
        }])
        # self.assertEqual(self.property.price, 100000.0)
        # self.assertEqual(self.property.state, 'draft')
        # self.assertEqual(self.property.property_type, 'apartment')

    # def test_compute_total_area(self):
    #     """
    #     Test the computation of the total area.
    #     """
    #     # Set living area and garden area
    #     self.property.living_area = 120
    #     self.property.garden_area = 30
    #     self.property._compute_total_area()

    #     # Check if the total area is computed correctly
    #     self.assertEqual(self.property.total_area, 150)

    # def test_change_state_to_available(self):
    #     """
    #     Test changing the state of the property to 'available'.
    #     """
    #     self.property.state = 'available'
    #     self.assertEqual(self.property.state, 'available')

    # def test_change_state_to_sold(self):
    #     """
    #     Test changing the state of the property to 'sold'.
    #     """
    #     self.property.state = 'sold'
    #     self.assertEqual(self.property.state, 'sold')

    # def test_property_name_required(self):
    #     """
    #     Test that the 'name' field is required.
    #     """
    #     with self.assertRaises(Exception):
    #         self.env['real_estate_property'].create({
    #             'description': 'This property has no name',
    #             'price': 100000.0,
    #         })

    # def test_property_price_positive(self):
    #     """
    #     Test that the 'price' field must be positive.
    #     """
    #     with self.assertRaises(Exception):
    #         self.env['real_estate_property'].create({
    #             'name': 'Invalid Price Property',
    #             'price': -1000.0,
    #         })

    # def test_property_type_selection(self):
    #     """
    #     Test that the 'property_type' field only accepts valid selections.
    #     """
    #     with self.assertRaises(Exception):
    #         self.env['real_estate_property'].create({
    #             'name': 'Invalid Property Type',
    #             'property_type': 'invalid_type',
    #         })