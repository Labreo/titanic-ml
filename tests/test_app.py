import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Titanic Survival Prediction' in response.data

def test_questions(client):
    response = client.get('/questions')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'What is your passenger class?' in html
    assert 'What is your gender?' in html
    assert 'What is your age?' in html
    assert 'How many siblings or spouses aboard?' in html
    assert 'How many parents or children do you have aboard?' in html
    assert 'What was your fare?' in html

def test_predict(client):
    data = {
    'Pclass': '1',
    'Sex': 'female',
    'Age': '30',
    'Siblings/Spouses Aboard': '0',
    'Parents/Children Aboard': '0',
    'Fare': '100'

    }
    
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'Yes,you will survive the Titanic!' in html or 'No,you will not survive the Titanic!' in html
