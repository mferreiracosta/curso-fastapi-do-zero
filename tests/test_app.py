from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_root_html_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/html')
    expected_response = """
    <html>
        <head>
            <title>Nosso olá mundo!</title>
        </head>
        <body>
            <h1>Olá Mundo!</h1>
            <h2>Minha primeira página.</h2>
        </body>
    </html>"""

    assert response.status_code == HTTPStatus.OK
    assert response.text == expected_response
