
def bearerToken(token):
    Bearer_token = 'Bearer {}'.format(token)
    headers = {'Authorization': Bearer_token}
    return headers
