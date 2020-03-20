/* HTTP API source writekey*/
const segmentWriteKey = "<STRING>"
const personasSpaceId = "<STRING>"

/* Provide Personas access secret (long string) as API Key for this function. See here: https://segment.com/docs/personas/profile-api/#set-up-access */
async function onIdentify(event, settings) {
  /* Fetch computed traits from the event */
  event.traits = event.traits || {}
  var email = event.traits.email
  var user_id = event.userId 
  
  /* Fetch lastname and company from Personas DB via Profile API. Lookup field = user email */

  /* 1. Make GET request to Profile API */
  /* You can use userId value instead of email as a lookup field. In this case, insert "user_id:${userId_variable}" in Profile API URL instead of "email:${email_variable}"*/
  const profileAPIEndpoint = `https://profiles.segment.com/v1/spaces/${personasSpaceId}/collections/users/profiles/email:${email}/traits?include=lastName,company,name`
  const req = await fetch(profileAPIEndpoint, {
    headers: new Headers({
      "Authorization": 'Basic ' + btoa(settings.apiKey + ':'),
      "Content-Type": "application/json",
    }),
    method: "get",
  })
  
  const user = await req.json()
  
  /* 2. Pull lastname and company */
  var lastname = user.traits.lastName || user.traits.name.split(" ").splice(-1)[0] //If last name is not in the traits, grab last word from 'name' trait

  var company = user.traits.company || 'n/a'
  
  /* Merge lastname and company into a single object */ 
  var ln_comp = {
    lastname: lastname,
    company: company
  }

  /* Create new event sans writekey, timestamp, messageID, which will 
  be added automatically by HTTP API source */
  var traits = _.merge(ln_comp, event.traits) // Create new traits object 

  var http_api_event = {
   type: "identify",
   userId: user_id, 
   traits:   traits,
   integrations: {
     Salesforce: true
   }
}

  console.log(JSON.stringify(http_api_event))

  /* Send new event to Segment API, i.e. emit the event from HTTP API source */
  const res = await fetch('https://api.segment.io/v1/identify', {
    body: JSON.stringify(http_api_event),
    headers: new Headers({
      "Authorization": 'Basic ' + btoa(segmentWriteKey + ':'),
      "Content-Type": "application/json",
    }),
    method: "post",
  })

  return await res.json()
}