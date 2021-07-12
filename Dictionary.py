Chat_Abbreviations = {
    "BRB":"Be right back",
    "BTW":"By the way",
    "CWLY":"Chat with you later",
    "DIY":"Do it yourself",
    "DM":"Direct Message",
    "GB":"Goodbye",
    "GL":"Goodluck",
    "GR8":"Great",
    "IDK":"I don't know",
    }

print(Chat_Abbreviations)

print(Chat_Abbreviations["CWLY"])

print(len(Chat_Abbreviations))

print(type(Chat_Abbreviations ))

print(Chat_Abbreviations.keys())

print(Chat_Abbreviations.items())

if "DM" in Chat_Abbreviations:
    print("Yes, DM means 'Direct Message'")

Chat_Abbreviations["IK"] = "I know"
print(Chat_Abbreviations)


Chat_Abbreviations.pop("GB")
Chat_Abbreviations.popitem()

print(Chat_Abbreviations)
