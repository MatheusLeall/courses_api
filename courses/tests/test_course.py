import requests


class TestCurso:
    
    URL_BASE_COURSES = 'http://127.0.0.1:8000/api/v2/courses/'
    URL_OBTAIN_TOKEN = 'http://127.0.0.1:8000/api/token/'
    data_request_token = {
        'username':'matheus',
        'password': 'admin12345'
    }

    request_authorization = requests.post(url=URL_OBTAIN_TOKEN, data=data_request_token)
    headers = {'Authorization' : f"Bearer {request_authorization.json()['access']}"}

    def test_get_courses(self):
        get_courses = requests.get(url=self.URL_BASE_COURSES, headers=self.headers)
        assert get_courses.status_code == 200

    def test_get_course(self):
        get_course = requests.get(url=f'{self.URL_BASE_COURSES}1/', headers=self.headers)
        assert get_course.status_code == 200

    def test_post_course(self):
        post_data = {
            'title': 'Análise de dados com R',
            'url': 'https://www.geekuniversity.com.br/cursos/analise-dados-R'
        }

        post_course = requests.post(url=self.URL_BASE_COURSES, headers=self.headers, data=post_data)
        
        assert post_course.status_code == 201
        assert post_course.json()['title'] == post_data['title']
    
    def test_put_curso(self):
        put_data = {
            'title': 'Criação de APIs REST com DRF',
            'url': 'https://www.geekuniversity.com.br/cursos/criacao-api-drf'
        }

        put_course = requests.put(url=f'{self.URL_BASE_COURSES}1/', headers=self.headers, data=put_data)

        assert put_course.status_code == 200
        assert put_course.json()['title'] == put_data['title']
    
    def test_delete_curso(self):
        delete_course = requests.delete(url=f'{self.URL_BASE_COURSES}9/', headers=self.headers)

        assert delete_course.status_code == 204 and len(delete_course.text) == 0

    
