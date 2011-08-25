class RecurlyObject:
  
  ATTRIBUTES = []

  PRIMARY_KEY = 'account_code'

  URI = ''

  CLIENT = RecurlyClient(URI)

  def __init__( self, attributes={} ):
    for attr_string in ATTRIBUTES:
      self.__dict__[attr_string] = attributes[attr_string]
      self.client = RecurlyClient(self, URI)

  def uri( self )
    URI % self.__dict__[PRIMARY_KEY]

# TODO:
#   1. Add RecurlyClient code
#   2. Any other shared code between recurly_objects
  pass
