from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        url='/users/',
        json={
            'username': 'teste',
            'email': 'teste@teste.com',
            'password': '12345',
        },
    )
    expected_response = {
        'id': 1,
        'username': 'teste',
        'email': 'teste@teste.com',
    }

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == expected_response


def test_read_users(client):
    response = client.get(url='/users/')
    expected_response = {
        'users': [
            {
                'id': 1,
                'username': 'teste',
                'email': 'teste@teste.com',
            }
        ]
    }

    assert response.json() == expected_response


def test_read_users_with_user_id(client):
    response = client.get(url='/users/1')
    expected_response = {
        'id': 1,
        'username': 'teste',
        'email': 'teste@teste.com',
    }

    assert response.json() == expected_response


def test_read_wrong_user(client):
    response = client.get(url='/users/-1')
    expected_response = {'detail': 'User not found'}

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == expected_response


def test_update_user(client):
    response = client.put(
        url='/users/1',
        json={
            'username': 'matheus',
            'email': 'matheus@hotmail.com',
            'password': '123456',
        },
    )
    expected_response = {
        'id': 1,
        'username': 'matheus',
        'email': 'matheus@hotmail.com',
    }

    assert response.status_code == HTTPStatus.OK
    assert response.json() == expected_response


def test_update_wrong_user(client):
    response = client.put(
        url='/users/-1',
        json={
            'username': 'matheus',
            'email': 'matheus@hotmail.com',
            'password': '123456',
        },
    )
    expected_response = {'detail': 'User not found'}

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == expected_response


def test_delete_user(client):
    response = client.delete(url='/users/1')
    expected_response = {'message': 'User deleted'}

    assert response.status_code == HTTPStatus.OK
    assert response.json() == expected_response


def test_delete_wrong_user(client):
    response = client.delete(url='/users/-1')
    expected_response = {'detail': 'User not found'}

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == expected_response
