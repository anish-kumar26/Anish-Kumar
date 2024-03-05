const accountSid = 'AC221ca32b1a5350b9823cb32ceb6cecd6';
const authToken = '239ebf18d85aa398dc3aa100704ea148';
const client = require('twilio')(accountSid, authToken);

client.messages
    .create({
        body: 'TEST',
        from: 'whatsapp:+14155238886',
        to: 'whatsapp:+919791126625'
    })
    .then(message => console.log(message.sid))
    .done();