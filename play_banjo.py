"""Play Banjo.

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:
name + " plays banjo" 
name + " does not play banjo"
"""
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        name = f"{name} plays banjo"
    else:
        name = f"{name} does not play banjo"
    return name


result = are_you_playing_banjo("rick")
print(result)



# Other Solution:

# 1. 
# def areYouPlayingBanjo(name):
#     return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";

# 2. 
# def areYouPlayingBanjo(name):
#    return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"

# 3. 
# def areYouPlayingBanjo(name):
#     if name[0].lower() == 'r':
#         return "{} plays banjo".format(name)
#     return "{} does not play banjo".format(name)