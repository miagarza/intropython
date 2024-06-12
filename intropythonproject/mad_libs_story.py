#Creating madlibs story

#declaring variables

mythicalanimal= "unicorn"
charactername= "Charlie"
age= "750"
secondcharactername= "Sam"
secondcharacterjob= "dentist"
place1= "forest"
place2= "beach"
pluralnoun1= "nice water"
pluralnoun2= "cool waves"
action= "run"
adj1="happy"
adj2="relaxed"
pasttenseverb1="listened"
pasttenseverb2="watched"

story= " There was once a "+ mythicalanimal + " named " + charactername + " who lived to be " + age + " years old. He was friends with a " + secondcharacterjob + \
" named " + secondcharactername + " who lived in the " + place1 + ". However," + secondcharactername + \
" still loved to visit the " + place2 + " because of the " + pluralnoun1 + " and " + pluralnoun2 + ". Sometimes, " + secondcharactername + \
" would " + action + " on the " + place2 + " because it made him feel " + adj1 + " and " + adj2 + ". Afterwards, he would go home to the " + \
place1 + " and " +  pasttenseverb1 + " to music after he " + pasttenseverb2 + " some TV."

password = input("Enter the password: ")
if password == "PythonCoding":
    print(story)
else:
    print("Sorry, that's not the right password. Goodbye.")