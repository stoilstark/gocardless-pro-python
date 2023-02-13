# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class SchemeIdentifiersService(base_service.BaseService):
    """Service class that provides access to the scheme_identifiers
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.SchemeIdentifier
    RESOURCE_NAME = 'scheme_identifiers'


    def create(self,params=None, headers=None):
        """Create a scheme identifier.

        Creates a new scheme identifier. The scheme identifier must be [applied
        to a creditor](#creditors-apply-a-scheme-identifier) before payments
        are taken using it. The scheme identifier must also have the `status`
        of active before it can be used. For some schemes e.g. faster_payments
        this will happen instantly. For other schemes e.g. bacs this can take
        several days.
        

        Args:
              params (dict, optional): Request body.

        Returns:
              SchemeIdentifier
        """
        path = '/scheme_identifiers'
        
        if params is not None:
            params = {self._envelope_key(): params}

        try:
          response = self._perform_request('POST', path, params, headers,
                                            retry_failures=True)
        except errors.IdempotentCreationConflictError as err:
          if self.raise_on_idempotency_conflict:
            raise err
          return self.get(identity=err.conflicting_resource_id,
                          params=params,
                          headers=headers)
        return self._resource_for(response)
  

    def list(self,params=None, headers=None):
        """List scheme identifiers.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        scheme identifiers.

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of SchemeIdentifier instances
        """
        path = '/scheme_identifiers'
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  

    def get(self,identity,params=None, headers=None):
        """Get a single scheme identifier.

        Retrieves the details of an existing scheme identifier.

        Args:
              identity (string): Unique identifier, usually beginning with "SU".
              params (dict, optional): Query string parameters.

        Returns:
              SchemeIdentifier
        """
        path = self._sub_url_params('/scheme_identifiers/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  