# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class BillingRequestFlowsService(base_service.BaseService):
    """Service class that provides access to the billing_request_flows
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.BillingRequestFlow
    RESOURCE_NAME = 'billing_request_flows'


    def create(self,params=None, headers=None):
        """Create a billing request flow.

        Creates a new billing request flow.

        Args:
              params (dict, optional): Request body.

        Returns:
              ListResponse of BillingRequestFlow instances
        """
        path = '/billing_request_flows'
        
        if params is not None:
            params = {self._envelope_key(): params}

        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def initialise(self,identity,params=None, headers=None):
        """Initialise a billing request flow.

        Returns the flow having generated a fresh session token which can be
        used to power
        integrations that manipulate the flow.

        Args:
              identity (string): Unique identifier, beginning with "BRQ".
              params (dict, optional): Request body.

        Returns:
              ListResponse of BillingRequestFlow instances
        """
        path = self._sub_url_params('/billing_request_flows/:identity/actions/initialise', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  
