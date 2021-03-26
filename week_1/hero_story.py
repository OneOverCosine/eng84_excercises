# code for the hero story task

# declare the variable 'story1' with keys: 'start', 'middle' and 'end'
# add values for each key
story1 = {
    "start": "They call me The Keeper. Of what, I do not know, but it was the name I was given, and it stuck.",
    "middle": "Over the years, I've come to be known as the 'Library Keeper'. It is a somewhat fitting name, though it doesn't explain why I was known as the 'The Keeper' for all those years before then. Maybe it is because of the knowledge I collect. Speaking of which... There have been odd creatures lurking around recently. People have started refering to them as 'Lurks' and I have begun researching them. They are elusive and tricky to handle, but they seem to pose no threat to us. Lighting a candle or a glowstone should be enough to scare them off when they get too close.",
    "end": "Those Lurks were not as... harmless as I'd once thought. More and more kept popping up and they started becoming violent. Three people were killed and many more went missing. They seemed to be drawn to my library. Blackberry placed a binding on it so I could burn it myself. I lost decades of research in a matter of minutes. And no one has seen Lurk since then."
}

print(story1) # printing out the whole dictionary
print(type(story1)) # printing out the type of 'story1'
print(story1.keys()) # printing only the keys of the dictionary
print(story1.values()) # printing only the values of the dictionary
# -----

# printing the values using the keys
for key in story1.keys():
    print(story1[key])

story1.update({"Hero": "Henrik, The Keeper"})

print("Our 'hero': {}.".format(story1["Hero"]))