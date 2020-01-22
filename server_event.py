import analytics
import random
import string

analytics.write_key = "COCYcKj6Jnm6ZSzHAlfcQ2dW6LuwLg7r"

def on_error(error, items):
    print("An error occurred:", error)

def randomUserID(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(stringLength))

#user_id = randomUserID(5)
analytics.debug = True
analytics.on_error = on_error

user_id = random.choice([1,2,3,4])
name = random.choice(["John Zoidberg", "Philip Fry", "Leela Turanga", "Lisa Simpson"])
email = random.choice(["email_1@mail.com", "email_2@mail.com", "email_3@mail.com", "email_4@mail.com"])
plan = random.choice(["premium", "almost-premium", "starter", "business"])
device = random.choice(["iphone_id", "winphone_id", "android_id", "blackberry_id"])
event_name = random.choice(["like_button_clicked", "product_added", "coupon_added", "product_viewed"])
'''alytics.identify("user_id_for_amplitude_2", 
{
  
  "email": "amplitude@user.com",
  "company" : "AMPLITUDE",
  "name": "Ampli Tude",
  "title": "Mr",
  "department": "accounting" 


}


)


0f776aebd41be0a3ff445e28978315f1
Amplitude
b13f9cfb5dfeb9e838e9c3e012dca8a2

'''
analytics.track("user_id_for_amplitude_2", "card_added",
{
  "card_type": "visa!"
},
)

print("Track done")
''' 
print("Identify done")

analytics.identify("999", 
{
  "name": "RRR RRR",
  "email": "steve@martin.com",
  "title": "Herr",
  "company": "ACME Corp",
  "department": "Sales!",

},
integrations= {
    "Salesforce": True
  }
)

print("Identify done")

analytics.track("111", "Payment_COMMITTED",
{
  "plan": plan,
  "amount": 100000
},
)

print("Track done")


analytics.track("1234567890", "product_added",
{
  "plan": plan,
  "spend": 100000
}

  )

print("Track done")


### Group call
analytics.group("00Q6g000001F2h5","0016g000007f8MF",
{
  "name": "Donut Company3",
  "org_id": "donut_id",
  "description": "ORG DESC"
},
integrations= {
    "Salesforce": True
}
)

print("Group done")



analytics.identify("1234567890", 
{
  "acc_number": "0016g000007f1BE",
  "email": "mary@doe.com"

},
integrations= {
    "Salesforce": True
  }
)


analytics.track("1234", "product_added",
{
  "email": "qwerty@gmail.com",
  "revenue": 11111
},
{
  "device":{
    "id":"my_dev_id"
  }
}
  )
analytics.track("999000", "product_added", 
{
  "plan": plan,
  "revenue": 333
}
  )  


analytics.page("uid_xyz", "button_clicked", {
  "user_plan": "Enterprise"

})
'''

