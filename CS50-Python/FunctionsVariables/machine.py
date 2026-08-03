emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")
    say("how are you ?")
    emoticon = ":("
    say("I am really sorry to heard that")

def say(phrase):
    print(phrase + " " +emoticon)

main()