import requests
from  plusauth_rest_py.base import  baseUrl
from plusauth_rest_py.bearer_token import bearerToken

base_url=baseUrl()

class ViewsService():

    def get(self , token , type ) :
        """
            Args: \n
            token:str -> You must have the access token.\n
            type:str -> View type

            Returns: Get View

            Documentation: https://docs.plusauth.com/api/core/views/getView
            
        """
        headers = bearerToken(token)
        self.type =type
        res =requests.get(base_url+"views/{}".format(self.type) , headers = headers )
        res_j =res.json()
        return res_j

    def update(self , token , type , html_content = ''):
        """
            Args: Args: \n
            token:str -> You must have the access token.\n
            type:str -> View type\n
            html_content -> View html content

            Returns: Update View

            Documentation: https://docs.plusauth.com/api/core/views/updateView

        """
        headers = bearerToken(token)
        headers['content-type'] = ' text/plain'
        self.type = type
        payload = {'html_content' : html_content}
        res = requests.patch(base_url + "views/{}".format(self.type), data = payload , headers=headers)
        res_j = res.json()
        return res_j
