from odoo import http
from odoo.http import request, Response
import json

class PropertyController(http.Controller):

    @http.route('/api/properties', type='http', auth='none', methods=['GET'], csrf=False)
    def get_properties(self, **kwargs):
        """
        GET endpoint to retrieve all properties.
        """
        print("inside get methoooooooooooooooooodddddddd")
        try:
            # Fetch all properties
            properties = request.env['real_estate_property'].search([])
            
            # Prepare response data
            property_data = []
            for property in properties:
                property_data.append({
                    'id': property.id,
                    'name': property.name,
                    'description': property.description,
                    'price': property.price,
                    'living_area': property.living_area,
                    'bedrooms': property.bedrooms,
                    'bathrooms': property.bathrooms,
                    'garage': property.garage,
                    'garden': property.garden,
                    'garden_area': property.garden_area,
                    'total_area': property.total_area,
                    'availability_date': property.availability_date,
                    'postcode': property.postcode,
                    'state': property.state,
                    'property_type': property.property_type,
                })
            
            # Return JSON response
            return Response(
                json.dumps(property_data),
                content_type='application/json',
                status=200
            )
        except Exception as e:
            return Response(
                json.dumps({'error': str(e)}),
                content_type='application/json',
                status=500
            )

    @http.route('/api/properties', type='json', auth='public', methods=['POST'], csrf=False)
    def create_property(self, **kwargs):
        """
        POST endpoint to create a new property.
        """
        try:
            # Parse JSON data from the request body
            data = request.jsonrequest
            
            # Create a new property
            new_property = request.env['real_estate_property'].create({
                'name': data.get('name'),
                'description': data.get('description'),
                'price': data.get('price'),
                'living_area': data.get('living_area'),
                'bedrooms': data.get('bedrooms'),
                'bathrooms': data.get('bathrooms'),
                'garage': data.get('garage', False),
                'garden': data.get('garden', False),
                'garden_area': data.get('garden_area', 0.0),
                'availability_date': data.get('availability_date'),
                'postcode': data.get('postcode'),
                'state': data.get('state', 'draft'),
                'property_type': data.get('property_type', 'apartment'),
            })
            
            # Return success response
            return {
                'status': 'success',
                'property_id': new_property.id,
            }
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
            }