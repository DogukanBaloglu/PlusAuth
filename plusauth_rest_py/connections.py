import requests
from  plusauth_rest_py.base import  baseUrl
from plusauth_rest_py.bearer_token import bearerToken

base_url=baseUrl()

class ConnectionService():

    def getAll(self , token , page = '' , itemsPerPage = '' , sortBy = '' , sortDesc = '' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            page -> The number of records you wish to skip before selecting records \n
            itemsPerPage -> Limit the number of results returned \n
            sortBy -> Properties that should be ordered by \n
            sortDesc -> Descending or ascending or nothing \n

            Returns: List Connections.
        """
        headers = bearerToken(token)
        payload = {'page': page, 'itemsPerPage': itemsPerPage, 'sortBy': sortBy, 'sortDesc': sortDesc}
        res = requests.get(base_url +"federated" , params = payload , headers = headers )
        res_j =res.json()
        return res_j

    def creat(self , token , name , type , settings = '' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            name:str -> Name \n
            type:str -> Type \n
            settings -> Settings |n

            Returns: Create new Connection.
        """
        headers = bearerToken(token)
        payload = {'name': name, 'type': type, 'settings': settings }
        res= requests.post(base_url+"federated" , data= payload , headers = headers )
        res_j=res.json()
        return res_j

    def get(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Connection ID

            Returns: Retrieve Connection.
        """
        headers = bearerToken(token)
        self.id = id
        res =requests.get(base_url+"federated/{}".format(self.id) , headers = headers )
        res_j = res.json()
        return res_j

    def update(self , token , id , created_at = '' , updated_at = '' , tenant_id = '' , name = '' , type =  ''  ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Connection ID \n
            created_at -> Created at \n
            updated_at -> Updated at \n
            tenant_id -> Tenant ID  \n
            name -> Name \n
            type -> Type \n

            Returns: Update Connection.
        """
        headers = bearerToken(token)
        self.id = id
        payload = { 'created_at':created_at , 'update_at': updated_at , 'tenant_id' : tenant_id , 'name':name , 'type' : type }
        res= requests.patch( base_url+"federated/{}".format(self.id) , data = payload , headers = headers )
        res_j = res.json()
        return  res_j

    def delete(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Connection ID \n

            Returns: Delete Connection.
        """
        headers = bearerToken(token)
        self.id = id
        res = requests.delete( base_url + "federated/{}".format(self.id) , headers = headers )
        return  res
