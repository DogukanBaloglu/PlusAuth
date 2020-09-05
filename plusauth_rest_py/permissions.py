import requests
from  plusauth_rest_py.base import  Base

base_url=Base().url()

class PermissionServise():

    def get(self , token , id ):
        """
            Args:\n
            token:str -> You must have the access token.\n
            id:str ->API id

            Returns: Get the permissions that this API uses

            Documentation: https://docs.plusauth.com/api/core/permissions/getApiPermissions?lang=python

        """
        headers = Base().headers_no_type(token)
        self.id= id
        res=requests.get(base_url+"apis/{}permissions".format(self.id), headers = headers )
        res_j=res.json()
        return res_j

    def create(self, token , id , name , description = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> API id \n
            name ->Name

            Returns: Add a new permission to this API.

            Documentation: https://docs.plusauth.com/api/core/permissions/createPermission?lang=python

        """
        headers = Base().headers_content_tpye_json(token)
        self.id = id
        payload ={'name':name , 'description': description}
        res=requests.post( base_url+"apis/{}/permissions".format(self.id), data = payload ,headers = headers )
        res_j=res.json()
        return res_j

    def delete(self , token , id , permission_id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> API id \n
            permission_id:str -> Permission id \n

            Returns: Delete permission

            Documentation: https://docs.plusauth.com/api/core/permissions/deletePermission?lang=python

        """
        headers = Base().headers_no_type(token)
        self.id = id
        self.permission_id = permission_id
        res=requests.delete( base_url+"apis/{}/permissions/{}".format(self.id , self.permission_id) ,headers = headers )
        return res
