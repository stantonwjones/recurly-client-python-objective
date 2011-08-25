URI = '/accounts%s'

ATTRIBUTES = [
  'account_code',
  'username',
  'first_name',
  'last_name',
  'email',
  'company_name',
  'hosted_login_token',
  'accept_language'
]

class RecurlyAccount(RecurlyObject):

  def __init__(self, attributes = {}):
    for attr_string in ATTRIBUTES:
      self.__dict__[attr_string] = attributes[attr_string]

# List all accounts for this site (paginated)
  @staticmethod
  def list:
    pass

# Get a specific account for this site
  @staticmethod
  def get(account_code = ''):
    pass

# Update this account's information
  def update(self):
    pass

# Close this account
  def close(self):
    pass
