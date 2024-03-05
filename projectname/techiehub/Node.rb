require 'rubygems'
require 'twilio-ruby'

account_sid = 'AC221ca32b1a5350b9823cb32ceb6cecd6'
auth_token = '239ebf18d85aa398dc3aa100704ea148'
@client = Twilio::REST::Client.new(account_sid, auth_token)

message = @client.messages.create(
  body: 'TEST',
  from: 'whatsapp:+14155238886',
  to: 'whatsapp:+919791126625'
)

puts message.sid