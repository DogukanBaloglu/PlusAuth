import requests
from  plusauth_rest_py.base import  baseUrl
from plusauth_rest_py.bearer_token import bearerToken

base_url=baseUrl()

class ApiService():

    def getAll(self, token, page='', itemsPerPage='', sortBy='', sortDesc=''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            page  -> The number of records you wish to skip before selecting records \n
            itemsPerPage -> Limit the number of results returned \n
            sortBy:array<string> -> Properties that should be ordered by \n
            sortDesc:boolean ->Descending or ascending or nothing \n

            Returns: List all created APIs.
        """
        headers = bearerToken(token)
        payload = {'page': page, 'itemsPerPage': itemsPerPage, 'sortBy': sortBy, 'sortDesc': sortDesc}
        res = requests.get(base_url+"apis" , params=payload , headers=headers  )
        res_j = res.json()
        return res_j

    def creat(self , token ,name, audience , description = '' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            name -> Name for Api\n
            audience -> Identifier for the Api. It cannot be changed after created. Received tokens will contain this field as aud parameter. \n
            description -> Additional information about Api \n

            Returns: Create new APIs
        """
        headers = bearerToken(token)
        payload = {'name': name, 'audience': audience , 'description':description}
        res = requests.post(base_url+"apis",data=payload , headers=headers)
        res_j = res.json()
        return res_j

    def get(self ,token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> API id

            Returns: Retrieve API
        """
        headers = bearerToken(token)
        self.id =id
        res = requests.get(base_url+"apis/{}".format(self.id) , headers=headers)
        res_j = res.json()
        return res_j

    def update(self, token, id , name='' , description='' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> API id \n
            name -> Updated name of Api \n
            description -> Updated description of Api \n

            Returns: Update an existing API.
        """
        headers = bearerToken(token)
        self.id =id
        data= {'name': name ,'description': description}
        res =requests.patch(base_url+"apis/{}".format(self.id) ,data=data , headers=headers  )
        res_j=res.json()
        return res_j

    def delete(self , token , id  ):
        """
            Args: \n
            id:str -> API id \n

            Returns: Delete an existing API.
        """
        headers = bearerToken(token)
        self.id = id
        res =requests.delete(base_url+"apis/{}".format(self.id), headers= headers)
        return res

    def getAuthorizedClients(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> API id

            Returns: Get clients authorized for the api.
        """
        headers = bearerToken(token)
        self.id = id
        res = requests.get(base_url+"apis/{}/authorized_clients".format(self.id), headers=headers )
        res_j = res.json()
        return res_j

    def authorizeClients(self , token , id , client_ids ='' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id -> API id
            client_ids -> Client ID's

            Returns: Authorize Clients to Api .
        """
        headers = bearerToken(token)
        self.id = id
        data= {'client_ids': client_ids }
        res=requests.post(base_url+"apis/{}/authorized_clients".format(self.id),data=data , headers=headers)
        res_j=res.json()
        return  res_j

    def unauthorizeClients(self , token , id , *client_id):
        """
            Args:\n
            token:str -> You must have the access token.\n
            id -> API id
            client_ids -> Client ID's

            Returns: Unauthorize client/s for the api.
        """
        headers = bearerToken(token)
        self.id= id
        client_id_array=list(client_id)
        payload ={'client_id': client_id_array }
        res=requests.delete(base_url+"apis/{}/authorized_clients".format(self.id) , data= payload ,headers=headers )
        res_j=res.json()
        return res_j

    def getPermissions(self, token , id , client_id , page = '', itemsPerPage='', sortBy='', sortDesc=''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Role Group id
            client_id:str -> Client id
            page  -> The number of records you wish to skip before selecting records \n
            itemsPerPage -> Limit the number of results returned \n
            sortBy (array<string>) -> Properties that should be ordered by \n
            sortDesc (boolean)  ->Descending or ascending or nothing \n

            Returns: Retrieve authorized permissions of an api to a client.
        """
        headers = bearerToken(token)
        self.id = id
        self.client_id = client_id
        payload = {'page': page, 'itemsPerPage': itemsPerPage, 'sortBy': sortBy, 'sortDesc': sortDesc}
        res = requests.get(base_url+"apis/{}/authorized_clients/{}/permissions".format(self.id,self.client_id), params = payload, headers=headers)
        res_j = res.json()
        return res_j

    def authorizePermission(self , token ,id , client_id , *permission_id ):
        """
            Args:\n
            token:str -> You must have the access token.\n
            id -> API id
            client_ids -> Client ID
            permission_id -> Permission Id's

            Returns: Authorize permissions for the client
        """
        headers = bearerToken(token)
        self.id=id
        self.client_id =client_id
        permission_id_array=list(permission_id)
        data = {'permission_id_array': permission_id_array}
        res=requests.post(base_url+"apis/{}/authorized_clients/{}/permissions".format(self.id,self.client_id), data=data ,headers=headers)
        res_j=res.json()
        return res_j

    def unauthorizePermission(self , token ,id , client_id , *permission_id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id -> API id
            client_ids -> Client ID
            permission_id -> Permission Id's

            Returns: Unauthorize permissions for the client
        """
        headers = bearerToken(token)
        self.id = id
        self.client_id = client_id
        permission_id_array = list(permission_id)
        data = {'permission_id_array': permission_id_array}
        res = requests.delete(base_url + "apis/{}/authorized_clients/{}/permissions".format(self.id, self.client_id),data=data, headers=headers)
        res_j = res.json()
        return res_j

    def deleteClient(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id ->Client id

            Returns: Delete Client.
        """
        headers = bearerToken(token)
        self.id=id
        res=requests.delete(base_url+"clients/{}".format(self.id), headers=headers )
        return res.text



