import requests
from  plusauth_rest_py.base import  baseUrl
from plusauth_rest_py.bearer_token import bearerToken

base_url=baseUrl()

class ClientService():

    def getAll(self , token , page = '' , itemsPerPage = '' , sortBy = '' , sortDesc = '' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            page -> The number of records you wish to skip before selecting records \n
            itemsPerPage -> Limit the number of results returned \n
            sortBy -> Properties that should be ordered by \n
            sortDesc -> Descending or ascending or nothing \n

            Returns: List all Clients
        """
        headers = bearerToken(token)
        payload = {'page' : page , 'itemsPerPage' : itemsPerPage , 'sortBy': sortBy , 'sortDesc' : sortDesc }
        res=requests.get(base_url+"clients" , params = payload , headers = headers )
        res_j =res.json()
        return res_j

    def creat(self , token , client_name  , update_at = '' , created_at = '' , client_id = '' , client_metadata = ''  ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            client_name:str -> Client name. \n
            update_at -> Update at \n
            created_at -> Created at \n
            client_id -> Client ID \n
            client_metadata:object -> Client metadata \n

            Returns: Create new Clients.
        """
        headers = bearerToken(token)
        payload = { 'client_name':client_name , 'update_at':update_at , 'created_at':created_at , 'client_id':client_id  , 'client_metadata':client_metadata }
        res = requests.post( base_url+"clients" , data= payload , headers = headers )
        res_j=res.json()
        return  res_j

    def get(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Client id

            Returns: Retrieve Client
        """
        headers = bearerToken(token)
        self.id =id
        res = requests.get( base_url+"clients/{}".format(self.id), headers = headers )
        res_j=res.json()
        return res_j

    def update(self , token , id , updated_at = '' , created_at = '' , client_name = ''
               , client_id = '' , client_metadata = '' , system = '' , audience = '' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Client id \n
            client_name -> Client name. \n
            update_at -> Update at \n
            created_at -> Created at \n
            client_id -> Client ID \n
            client_metadata:object -> Client metadata \n
            system -> system \n
            audience -> audience \n

            Returns: Update CLIENT
        """
        headers = bearerToken(token)
        self.id = id
        payload = {'client_name': client_name, 'update_at': update_at, 'created_at': created_at, 'client_id': client_id,
                   'client_metadata': client_metadata , 'system': system , 'audience' : audience }
        res =requests.patch( base_url+"clients/{}".format(self.id) , data= payload , headers = headers )
        res_j=res.json()
        return res_j


