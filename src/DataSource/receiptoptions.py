def email_get():
    emailaddress =input("Please enter email address for recipt to be sent to. ")
    print("emailing " + emailaddress)
    print("in full application printer will be called here")

def print_or_email()
    print("by defult this application gives digital recipts ")
    printoptions = input("Do you want a paper recipt, Y/N ")
    if printoptions == "Y":
        print("printing")
        print("in full application printer will be called here")
        emailoptions = input("Do you also want a digital recipt, Y/N")
        if emailoptions == "Y":
            email_get()
    else:
        email_get()
