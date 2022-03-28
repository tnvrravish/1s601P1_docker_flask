"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/flask">Flask</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_cicd(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"Continous Integration/Continous Deployment" in response.data

def test_request_flask(client):
    """This makes the index page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"Python-Flask" in response.data

def test_request_git(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git/Github" in response.data

def test_request_oop(client):
    """This makes the index page"""
    response = client.get("/oop")
    assert response.status_code == 200
    assert b"OOP" in response.data

def test_request_pylint(client):
    """This makes the index page"""
    response = client.get("/pylint")
    assert response.status_code == 200
    assert b"pylint" in response.data

def test_request_solid(client):
    """This makes the index page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID" in response.data

def test_request_aaa(client):
    """This makes the index page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"AAA" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
