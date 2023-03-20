# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class Event(object):
    """A thin wrapper around a event, providing easy access to its
    attributes.

    Example:
      event = client.events.get()
      event.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def action(self):
        return self.attributes.get('action')
  

    @property
    def created_at(self):
        return self.attributes.get('created_at')
  

    @property
    def customer_notifications(self):
        return self.attributes.get('customer_notifications')
  

    @property
    def details(self):
        return self.Details(self.attributes.get('details'))
  

    @property
    def id(self):
        return self.attributes.get('id')
  

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))
  

    @property
    def metadata(self):
        return self.attributes.get('metadata')
  

    @property
    def resource_type(self):
        return self.attributes.get('resource_type')
  


  

  

  

  
    class Details(object):
        """Wrapper for the response's 'details' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def bank_account_id(self):
            return self.attributes.get('bank_account_id')
    
        @property
        def cause(self):
            return self.attributes.get('cause')
    
        @property
        def currency(self):
            return self.attributes.get('currency')
    
        @property
        def description(self):
            return self.attributes.get('description')
    
        @property
        def not_retried_reason(self):
            return self.attributes.get('not_retried_reason')
    
        @property
        def origin(self):
            return self.attributes.get('origin')
    
        @property
        def _property(self):
            return self.attributes.get('property')
    
        @property
        def reason_code(self):
            return self.attributes.get('reason_code')
    
        @property
        def scheme(self):
            return self.attributes.get('scheme')
    
        @property
        def will_attempt_retry(self):
            return self.attributes.get('will_attempt_retry')
    
  

  

  
    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def bank_authorisation(self):
            return self.attributes.get('bank_authorisation')
    
        @property
        def billing_request(self):
            return self.attributes.get('billing_request')
    
        @property
        def billing_request_flow(self):
            return self.attributes.get('billing_request_flow')
    
        @property
        def creditor(self):
            return self.attributes.get('creditor')
    
        @property
        def customer(self):
            return self.attributes.get('customer')
    
        @property
        def customer_bank_account(self):
            return self.attributes.get('customer_bank_account')
    
        @property
        def instalment_schedule(self):
            return self.attributes.get('instalment_schedule')
    
        @property
        def mandate(self):
            return self.attributes.get('mandate')
    
        @property
        def mandate_request_mandate(self):
            return self.attributes.get('mandate_request_mandate')
    
        @property
        def new_customer_bank_account(self):
            return self.attributes.get('new_customer_bank_account')
    
        @property
        def new_mandate(self):
            return self.attributes.get('new_mandate')
    
        @property
        def organisation(self):
            return self.attributes.get('organisation')
    
        @property
        def parent_event(self):
            return self.attributes.get('parent_event')
    
        @property
        def payer_authorisation(self):
            return self.attributes.get('payer_authorisation')
    
        @property
        def payment(self):
            return self.attributes.get('payment')
    
        @property
        def payment_request_payment(self):
            return self.attributes.get('payment_request_payment')
    
        @property
        def payout(self):
            return self.attributes.get('payout')
    
        @property
        def previous_customer_bank_account(self):
            return self.attributes.get('previous_customer_bank_account')
    
        @property
        def refund(self):
            return self.attributes.get('refund')
    
        @property
        def scheme_identifier(self):
            return self.attributes.get('scheme_identifier')
    
        @property
        def subscription(self):
            return self.attributes.get('subscription')
    
  

  

  

