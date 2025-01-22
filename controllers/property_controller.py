from odoo import http
from odoo.http import request, Response,HTTPRequest
import json

class PropertyController(http.Controller):

  # **Controller Class Definition**
  # This code defines a class named `PropertyController` that inherits from `http.Controller`.
  # Controllers handle HTTP requests coming to your Odoo application.

  # **Create Operation**
  @http.route('/api/property/json', type='json', auth='none', methods=['POST'], csrf=False)
  def create_property(self ):
    """
    Create a new property.
    """
    try:
      # Get JSON data from the request body
      data = request.HTTPRequest.data.decode()
      vals=json.leads(data)

      # Access the Odoo model 'real.estate.property' through the environment
      new_property = request.env['real.estate.property'].sudo().create(vals)

      # Return a success response with the property ID
      return {
          'status': 'success',
          'property_id': new_property.id,
          'name': new_property.name,
          'price': new_property.price,
          'agent_id': new_property.agent_id,
      } 
    except Exception as e:
      # Handle exceptions and return an error response
      return {
          'status': 'error',
          'error': str(e),
      }

  # **Read Operation (Get All Properties)**
  @http.route('/api/properties', type='http', auth='public', methods=['GET'], csrf=False)
  def get_properties(self, **kwargs):
    """
    Retrieve all properties.
    """
    try:
      # Search for all properties using the 'real.estate.property' model
      properties = request.env['real.estate.property'].search([])

      # Prepare a list to store property data
      property_data = []

      # Loop through each property and extract relevant information
      for property in properties:
        property_data.append({
          'id': property.id,
          'name': property.name,
          'price': property.price,
          'state': property.state,
          'property_type': property.property_type,
        })

      # Return a JSON response with the list of properties
      return Response(
          json.dumps(property_data),
          content_type='application/json',
          status=200
      )
    except Exception as e:
      # Handle exceptions and return an error response
      return Response(
          json.dumps({'error': str(e)}),
          content_type='application/json',
          status=500
      )

  # **Read Operation (Get Single Property)**
  @http.route('/api/properties/<int:property_id>', type='json', auth='public', methods=['GET'], csrf=False)
  def get_property(self, property_id, **kwargs):
    """
    Retrieve a single property by ID.
    """
    try:
      # Search for the property by ID using the 'real.estate.property' model
      property = request.env['real.estate.property'].browse(property_id)

      # Check if the property exists
      if not property.exists():
        # Return a "not found" error response
        return Response(
            json.dumps({'error': 'Property not found'}),
            content_type='application/json',
            status=404
        )

      # Prepare a dictionary with the property data
      property_data = {
          'id': property.id,
          'name': property.name,
          'price': property.price,
          'state': property.state,
          'property_type': property.property_type,
      }

      # Return a JSON response with the property data
      return Response(
          json.dumps(property_data),
          content_type='application/json',
          status=200
      )
    except Exception as e:
      # Handle exceptions and return an error response
      return Response(
          json.dumps({'error': str(e)}),
          content_type='application/json',
          status=500
      )

  # **Update Operation**
  @http.route('/api/properties/<int:property_id>', type='json', auth='public', methods=['PUT'], csrf=False)
  def update_property(self, property_id, **kwargs):
    """
    Update an existing property.
    """
    try:
      # Get JSON data from the request body
      # Get JSON data from the request body
      data = request.jsonrequest

      # Search for the property by ID
      property = request.env['real.estate.property'].browse(property_id)

      # Check if the property exists
      if not property.exists():
        return {
            'status': 'error',
            'error': 'Property not found',
        }

      # Update the property with the provided data
      property.write(data)

      # Return a success response with the updated property ID
      return {
          'status': 'success',
          'property_id': property.id,
      }
    except Exception as e:
      # Handle exceptions and return an error response
      return {
          'status': 'error',
          'error': str(e),
      }

  # **Delete Operation**
  @http.route('/api/properties/<int:property_id>', type='json', auth='public', methods=['DELETE'], csrf=False)
  def delete_property(self, property_id, **kwargs):
    """
    Delete a property by ID.
    """
    try:
      # Search for the property by ID
      property = request.env['real.estate.property'].browse(property_id)

      # Check if the property exists
      if not property.exists():
        return {
            'status': 'error',
            'error': 'Property not found',
        }

      # Delete the property
      property.unlink()

      # Return a success response
      return {
          'status': 'success',
          'message': 'Property deleted',
      }
    except Exception as e:
      # Handle exceptions and return an error response
      return {
          'status': 'error',
          'error': str(e),
      }