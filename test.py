# a = 0 
# b = 1

# n = int(input("Enter n: "))
# for i in range(2, n):
#   temp = a + b
#   a = b
#   b = temp

# print(temp)

# shinobis = {"Naruto":"genin", "Sasuke":"genin", "Shikamaru":"chunin", "Kakashi":"chunin", "Tsunade":"Hokage", "Itachi":"rogue", "Orochimaru":"rogue"}

indents = {
  "ninja":["jutsu","shuriken","chakra"],
  "pirate":["devil fruit", "katana", "haki"],
  "saiyan":["martial arts", "android", "ki"]
}

responses = {
  "ninja":"Naruto",
  "pirate":"Luffy",
  "saiyan":"Goku"
}

user_input = input("Tell me what power/weapon/energy does you character use? ")

detected_indent = None

for indent, battle in indents.items():
  if user_input in battle:
    detected_indent = indent
    break

if detected_indent:
  print("Your character is", responses.get(detected_indent))
else:
  print("Yout character is not available.")