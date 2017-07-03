def correct():
    print("You are logged in")
def wrong(tries):
    print("Wrong password, you have ",tries,"tries left")
def checkpwd():
    p=input("Enter passowrd")
    return p
def lockout():
    print("You are locked out of this account.")
def main():
    pwd="1234"
    tries=5
    print("Please enter your password to log in. You have a total of 5 tries")
    p=checkpwd()
    if p==pwd:
        correct()
    while p!=pwd:
        tries=tries-1
        wrong(tries)
        if tries<1:
            lockout()
            break
        p=checkpwd()
    else:
        correct()

main()
