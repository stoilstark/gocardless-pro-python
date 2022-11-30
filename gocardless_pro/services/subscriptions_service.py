# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class SubscriptionsService(base_service.BaseService):
    """Service class that provides access to the subscriptions
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Subscription
    RESOURCE_NAME = 'subscriptions'


    def create(self,params=None, headers=None):
        """Create a subscription.

        Creates a new subscription object

        Args:
              params (dict, optional): Request body.

        Returns:
              Subscription
        """
        path = '/subscriptions'
        
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
        """List subscriptions.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        subscriptions. Please note if the subscriptions are related to
        customers who have been removed, they will not be shown in the
        response.

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of Subscription instances
        """
        path = '/subscriptions'
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  

    def get(self,identity,params=None, headers=None):
        """Get a single subscription.

        Retrieves the details of a single subscription.

        Args:
              identity (string): Unique identifier, beginning with "SB".
              params (dict, optional): Query string parameters.

        Returns:
              Subscription
        """
        path = self._sub_url_params('/subscriptions/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def update(self,identity,params=None, headers=None):
        """Update a subscription.

        Updates a subscription object.
        
        This fails with:
        
        - `validation_failed` if invalid data is provided when attempting to
        update a subscription.
        
        - `subscription_not_active` if the subscription is no longer active.
        
        - `subscription_already_ended` if the subscription has taken all
        payments.
        
        - `mandate_payments_require_approval` if the amount is being changed
        and the mandate requires approval.
        
        - `number_of_subscription_amendments_exceeded` error if the
        subscription amount has already been changed 10 times.
        
        - `forbidden` if the amount is being changed, and the subscription was
        created by an app and you are not authenticated as that app, or if the
        subscription was not created by an app and you are authenticated as an
        app
        
        - `resource_created_by_another_app` if the app fee is being changed,
        and the subscription was created by an app other than the app you are
        authenticated as
        

        Args:
              identity (string): Unique identifier, beginning with "SB".
              params (dict, optional): Request body.

        Returns:
              Subscription
        """
        path = self._sub_url_params('/subscriptions/:identity', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {self._envelope_key(): params}

        response = self._perform_request('PUT', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def pause(self,identity,params=None, headers=None):
        """Pause a subscription.

        Pause a subscription object.
        No payments will be created until it is resumed.
        
        This can only be used when a subscription is collecting a fixed number
        of payments (created using `count`),
        when they continue forever (created without `count` or `end_date`) or
        the subscription is already paused for a number of cycles.
        
        When `pause_cycles` is omitted the subscription is paused until the
        [resume endpoint](#subscriptions-resume-a-subscription) is called.
        If the subscription is collecting a fixed number of payments,
        `end_date` will be set to `null`.
        When paused indefinitely, `upcoming_payments` will be empty.
        
        When `pause_cycles` is provided the subscription will be paused for the
        number of cycles requested.
        If the subscription is collecting a fixed number of payments,
        `end_date` will be set to a new value.
        When paused for a number of cycles, `upcoming_payments` will still
        contain the upcoming charge dates.
        
        This fails with:
        
        - `forbidden` if the subscription was created by an app and you are not
        authenticated as that app, or if the subscription was not created by an
        app and you are authenticated as an app
        
        - `validation_failed` if invalid data is provided when attempting to
        pause a subscription.
        
        - `subscription_paused_cannot_update_cycles` if the subscription is
        already paused for a number of cycles and the request provides a value
        for `pause_cycle`.
        
        - `subscription_cannot_be_paused` if the subscription cannot be paused.
        
        - `subscription_already_ended` if the subscription has taken all
        payments.
        
        - `pause_cycles_must_be_greater_than_or_equal_to` if the provided value
        for `pause_cycles` cannot be satisfied.
        

        Args:
              identity (string): Unique identifier, beginning with "SB".
              params (dict, optional): Request body.

        Returns:
              Subscription
        """
        path = self._sub_url_params('/subscriptions/:identity/actions/pause', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def resume(self,identity,params=None, headers=None):
        """Resume a subscription.

        Resume a subscription object.
        Payments will start to be created again based on the subscriptions
        recurrence rules.
        The `charge_date` on the next payment will be the same as the
        subscriptions `earliest_charge_date_after_resume`
        
        This fails with:
        
        - `forbidden` if the subscription was created by an app and you are not
        authenticated as that app, or if the subscription was not created by an
        app and you are authenticated as an app
        
        - `validation_failed` if invalid data is provided when attempting to
        resume a subscription.
        
        - `subscription_not_paused` if the subscription is not paused.
        

        Args:
              identity (string): Unique identifier, beginning with "SB".
              params (dict, optional): Request body.

        Returns:
              Subscription
        """
        path = self._sub_url_params('/subscriptions/:identity/actions/resume', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def cancel(self,identity,params=None, headers=None):
        """Cancel a subscription.

        Immediately cancels a subscription; no more payments will be created
        under it. Any metadata supplied to this endpoint will be stored on the
        payment cancellation event it causes.
        
        This will fail with a cancellation_failed error if the subscription is
        already cancelled or finished.

        Args:
              identity (string): Unique identifier, beginning with "SB".
              params (dict, optional): Request body.

        Returns:
              Subscription
        """
        path = self._sub_url_params('/subscriptions/:identity/actions/cancel', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  
