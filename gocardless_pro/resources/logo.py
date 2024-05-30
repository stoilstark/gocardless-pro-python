# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class Logo(object):
    """A thin wrapper around a logo, providing easy access to its
    attributes.

    Example:
      logo = client.logos.get()
      logo.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def id(self):
        return self.attributes.get('id')
  


  

