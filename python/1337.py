""" 1337 .py

Given a message, convert it into 1337 sp34k

Henry Mendler

November 2025 """


TEST_MESSAGE = "Hello World!"

##TEST_SUBSTITUTIONS = [['e','3']]
SUBSTITUTIONS = 

#### Function Section
def encode_message(message, substitutions) :
    for s in substitutions:
    """Take a string message and apply each of the subtitutions
    provided. Subtitutions should be a list, the elements of
    substitutions need to be lists of length 2 of the form
    (old_string, new_string) """


#### Testing Section
converted_text = encode_messageTEST_MESSAGE, TEST_SUBSTITUTIONS)
print(converted_text)



for s in substitutions:

    old = s[0]

    new = s[1]

    converted = message.replace(old,new)


return converted


#### Testing Section

message = raw_input("Type the message to be encoded here: ")
converted_text = encode_message(message, TEST_SUBSTITUTIONS)
print(message)
print(converted_text)
print(converted_text)


