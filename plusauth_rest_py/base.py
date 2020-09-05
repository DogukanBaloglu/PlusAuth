
class Base () :

    def url(self):
        return "https://dogukan.plusauth.com/api/v1/"

    def headers_no_type(self, token):
        Bearer_token = 'Bearer {}'.format(token)
        headers = {'Authorization': Bearer_token}
        return headers

    def headers_content_tpye_json(self ,token):
        Bearer_token = 'Bearer {}'.format(token)
        headers = {'Authorization': Bearer_token ,'content-type' : 'application/json'}
        return headers

    def headers_content_type_text(self , token ):
        Bearer_token = 'Bearer {}'.format(token)
        headers = {'Authorization': Bearer_token, 'content-type': 'text/plain'}
        return headers
