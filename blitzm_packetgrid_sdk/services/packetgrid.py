from blitzm_packetgrid_sdk import Configuration, ApiClient, NotificationsApi, ClientTokenApi

HOST_PRODUCTION = 'https://api.packetgrid.io/api'
HOST_SANDBOX = 'https://sandbox.api.packetgrid.io/api'


class PacketGrid:

    def __init__(self, tenant_id, api_key, is_production):
        """

        :param tenant_id: Your PacketGrid tenant id
        :param api_key: Your PacketGrid API key
        :param is_production: Use the production or the sandbox
        """

        configuration = Configuration()
        # set the api key
        configuration.api_key['Authorization'] = api_key
        configuration.api_key_prefix['Authorization'] = 'Token'
        # set the url
        if is_production:
            configuration.host = HOST_PRODUCTION
        else:
            configuration.host = HOST_SANDBOX

        api_client = ApiClient(configuration)
        # set the tenant header
        api_client.set_default_header('Tenant-Id', tenant_id)
        # instance the callable api to use
        self.notifications = NotificationsApi(api_client)
        self.client_tokens = ClientTokenApi(api_client)
