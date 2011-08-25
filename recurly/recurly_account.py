class RecurlyAccount(RecurlyObject):

  URI = '/accounts%s'

  ATTRIBUTES = [
    'account_code',
    'first_name',
    'last_name',
    'email',
    'company'
  ]

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
