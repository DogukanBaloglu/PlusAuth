import requests
from  plusauth_rest_py.base import  baseUrl
from plusauth_rest_py.bearer_token import bearerToken

base_url=baseUrl()

class TenantsService():

    def gertAll(self , token , page = '' , itemsPerPage = '' , sortBy = '' , sortDesc = '' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            page -> The number of records you wish to skip before selecting records \n
            itemsPerPage -> Limit the number of results returned \n
            sortBy -> Properties that should be ordered by \n
            sortDesc -> Descending or ascending or nothing \n

            Returns: List all Tenants
        """
        headers = bearerToken(token)
        payload = {'page': page, 'itemsPerPage': itemsPerPage, 'sortBy': sortBy, 'sortDesc': sortDesc}
        res = requests.get(base_url + "tenants", params=payload, headers=headers)
        res_j = res.json()
        return res_j

    def creat(self , token , tenant_id , region ,settings = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            tenant_id:str -> Tenant id \n
            region -> str \n
            settings -> Read documentation

            Returns: Create Tenant
        """
        headers = bearerToken(token)
        payload = { 'tenant_id' :tenant_id , 'region' : region , 'settings' : settings }
        res =requests.post(base_url+"tenants" , data = payload , headers =headers )
        res_j =res.json()
        return  res_j

    def delete(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Tenant id

            Returns: Delete Tenant
        """
        headers = bearerToken(token)
        self.id = id
        res = requests.delete(base_url + "tenants/{}".format(self.id), headers=headers)
        return res

    def getSettings(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Tenant id

            Returns: Get Tenant settings
        """
        headers = bearerToken(token)
        self.id = id
        res = requests.get(base_url + "tenants/{}/settings".format(self.id), headers=headers)
        res_j=res.json()
        return res_j

    def updateSettings(self , token , id , mfa = '' , email = '' , social = '' , defaultStrategy = '' , autoSiggnIn = ''
                       ,registerEnabled = '' , forceEmailVerification = '' , forgotPasswordEnabled = '' , extraParams = ''
                       , extraScopes = '' , hashFunction = '' , tenantLoginUrl = '' , ttl = '', passwordPolicy = '' ):
        """
            Args:\n
            token:str -> You must have the access token.\n
            id:str -> Tenant id \n
            Setting options  -> optional

            Returns: Update Tenant settings
        """
        headers = bearerToken(token)
        self.id = id
        payload ={'mfa' : mfa , 'email': email , 'social': social, 'defaultStrategy' :defaultStrategy, 'autoSiggnIn' : autoSiggnIn ,
                  'registerEnabled' :registerEnabled , 'forceEmailVerification': forceEmailVerification ,
                  'forgotPasswordEnabled':forgotPasswordEnabled,'extraParams': extraParams , 'extraScopes':extraScopes,'hashFunction': hashFunction ,
                  'tenantLoginUrl':tenantLoginUrl ,'ttl':ttl , 'passwordPolicy': passwordPolicy }
        res = requests.patch(base_url + "tenants/{}/settings".format(self.id), data = payload , headers=headers)
        res_j=res.json()
        return res_j