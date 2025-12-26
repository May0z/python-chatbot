# a = 0 
# b = 1

# n = int(input("Enter n: "))
# for i in range(2, n):
#   temp = a + b
#   a = b
#   b = temp

# print(temp)

# shinobis = {"Naruto":"genin", "Sasuke":"genin", "Shikamaru":"chunin", "Kakashi":"chunin", "Tsunade":"Hokage", "Itachi":"rogue", "Orochimaru":"rogue"}

# indents = {
#   "ninja":["jutsu","shuriken","chakra"],
#   "pirate":["devil fruit", "katana", "haki"],
#   "saiyan":["martial arts", "android", "ki"]
# }

# responses = {
#   "ninja":"Naruto",
#   "pirate":"Luffy",
#   "saiyan":"Goku"
# }

users = {
  "user1": {"name":"Aayush", "job":"Loser", "skills":["Java","PHP"]},
  "user2":{"name":"Rashmita", "job":"Asc. Developer", "skills":["Java","PHP","DevOps","SQL"]}
}
users.update({"user3":{"name":"Sudeep", "job":"Loser", "skills":["SEO","SQL"]}})
users["user2"]["skills"].append("PHP")
users["user3"]["skills"].append("React")

users["user1"]["skills"].remove("PHP")
for user_id, user_details in users.items():
  print(user_id)
  print('Name:',user_details["name"])
  print('Skills:')
  for skill in user_details['skills']:
    print('-', skill)

  print()