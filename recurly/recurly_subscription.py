class RecurlySubscription(RecurlyObject):

  URI = '/accounts/%s/subscription'

  ATTRIBUTES = [
    'plan_code',
    'coupon_code',
    'unit_amount_in_cents',
    'trial_ends_at'
  ]

# Retrieve the subscription for an accout

# Create a subscription for an account
#
# Change this subscription
#
# Cancel this subscription
