import datetime
import json
from tests.test_main import MainTest

"""This class contains unit tests for the menu apis and functions"""
class OrderTestCase(MainTest):

    def test_api_customer_create_order(self):
        # A customer can create an order
        
        # Send a post with customer credentials
        res = self.client.post('/api/v1/auth/login/', data=self.customer,content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertTrue(res_data['message'] == 'Successfully logged in')
        self.assertTrue(res_data['access_token'])

        self.assertEqual(res.status_code, 200)
        res = self.client.post('/api/v1/orders/', data=self.order,
        content_type='application/json',
        headers=dict(Authorization='JWT '+ res_data['access_token']))
        self.assertEqual(res.status_code, 201)
        today = datetime.date.today().strftime("%Y-%m-%d")
        self.assertIn(today, str(res.data))

    def test_api_caterer_should_not_create_order(self):
        # A customer can create an order
        
        # Send a post with customer credentials
        res = self.client.post('/api/v1/auth/login/', data=self.caterer,content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertTrue(res_data['message'] == 'Successfully logged in')
        self.assertTrue(res_data['access_token'])
        self.assertEqual(res.status_code, 200)

        second_res = self.client.post('/api/v1/orders/', data=json.dumps(self.order),content_type='application/json',headers=dict(Authorization='JWT '+ res_data['access_token']))
        self.assertEqual(second_res.status_code, 403)
        self.assertIn('An admin(caterer) is not allowed to post an order', str(second_res.data))

    def test_api_customer_should_not_get_orders(self):
        #Test API can get an order with GET request

        res = self.client.post('/api/v1/auth/login/', data=self.customer,content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertTrue(res_data['message'] == 'Successfully logged in')
        self.assertTrue(res_data['access_token'])

        second_res = self.client.post('/api/v1/meals/', data=json.dumps({"name": "Posho & Peas",
            "price": "11.5"}),content_type='application/json',headers=dict(Authorization='JWT '+ res_data['access_token']))
        self.assertEqual(second_res.status_code, 403)
        self.assertIn('You must be an admin to access this resource', str(second_res.data))

    def test_api_customer_update_order(self):
        #Test API can edit an existing order with PUT request

        res = self.client.post('/api/v1/auth/login/', data=self.customer,content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertTrue(res_data['message'] == 'Successfully logged in')
        self.assertTrue(res_data['access_token'])

        res = self.client.post('/api/v1/orders/',data=json.dumps({'meal_id':7, 'user_id': 8}),
        content_type='application/json',
        headers=dict(Authorization='JWT '+ res_data['access_token']))
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data.decode())
        new_order_id = data['order']['id']
        rs = self.client.put('/api/v1/orders/'+str(new_order_id), 
        data=json.dumps({'meal_id':5, 'user_id': 1}),
        content_type='application/json',
        headers=dict(Authorization='JWT '+ res_data['access_token']))
        self.assertEqual(rs.status_code, 202)
        results = self.client.get('/api/v1/orders/'+str(new_order_id),
        content_type='application/json',
        headers=dict(Authorization='JWT '+ res_data['access_token']))
        self.assertIn('5', str(results.data))

    def test_api_customer_delete_order(self):
        '''Test API can delete an existing order with DELETE request'''
        res = self.client.post('/api/v1/auth/login/', data=self.customer,content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertTrue(res_data['message'] == 'Successfully logged in')
        self.assertTrue(res_data['access_token'])

        res = self.client.post('/api/v1/orders/',data=json.dumps({'meal_id':5, 'user_id': 1}),
        content_type='application/json',
        headers=dict(Authorization='JWT '+ res_data['access_token']))
        self.assertEqual(res.status_code, 201)
        response_data = json.loads(res.data.decode())
        new_id = response_data['order']['id']
        res = self.client.delete('/api/v1/orders/'+str(new_id),
        content_type='application/json',
        headers=dict(Authorization='JWT '+ res_data['access_token']))
        self.assertEqual(res.status_code, 202)
        '''Test to see if it does not exist, should return a 404'''
        result = self.client.get('/api/v1/orders/'+str(new_id),
        content_type='application/json',
        headers=dict(Authorization='JWT '+ res_data['access_token']))
        self.assertEqual(result.status_code, 404)

if __name__ == "__main__":
    unittest.main()