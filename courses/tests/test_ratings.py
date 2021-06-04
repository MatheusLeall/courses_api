import requests


class TestRate:

    URL_BASE_RATINGS = 'http://127.0.0.1:8000/api/v2/ratings/'
    URL_OBTAIN_TOKEN = 'http://127.0.0.1:8000/api/token/'
    data_request_token = {
        'username':'matheus',
        'password': 'admin12345'
    }

    request_authorization = requests.post(url=URL_OBTAIN_TOKEN, data=data_request_token)
    headers = {'Authorization' : f"Bearer {request_authorization.json()['access']}"}

    def test_get_ratings(self):
        get_ratings = requests.get(url=self.URL_BASE_RATINGS, headers=self.headers)
        
        assert get_ratings.status_code == 200
    
    def test_get_rate(self):
        get_rate = requests.get(url=f'{self.URL_BASE_RATINGS}1/', headers=self.headers)
        
        assert get_rate.status_code == 200

    def test_post_rate(self):
        post_data = {
            'course': 1,
            'name': 'Mateus Leal',
            'email': 'matheuslealphb@email.com',
            'comment': 'Muito bom o curso! mas faltou fazer o deploy',
            'rate': '4'
        }

        post_rate = requests.post(url=self.URL_BASE_RATINGS, headers=self.headers, data=post_data)

        assert post_rate.status_code == 201

    def test_put_rate(self):
        put_data = {
            "course": 1,
            "name": "Matheus Leal",
            "email": "matheusleal@gmail.com",
            "comment": "Muito bom o curso! mas faltou fazer o deploy",
            "rate": "4"
        }

        put_rate = requests.put(url=f'{self.URL_BASE_RATINGS}1/', headers=self.headers, data=put_data)

        assert put_rate.status_code == 200

    def test_delete_rate(self):
        delete_rate = requests.delete(url=f'{self.URL_BASE_RATINGS}7/', headers=self.headers)

        assert delete_rate.status_code == 204 and len(delete_rate.text) == 0
