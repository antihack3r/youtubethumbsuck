import re

youtubelink = input("Paste here a YouTube video link: ")
if "/watch?v=" not in youtubelink:
	print("String does not contain a YouTube link.")
	raise SystemExit
if "&" not in youtubelink:
	x = re.findall("/watch[?]v=(.*)",youtubelink)
	print("Your image link is https://i.ytimg.com/vi/"+x[0]+"/maxresdefault.jpg")
	raise SystemExit
x = re.findall("/watch[?]v=(.*)&",youtubelink)
print("Your image link is https://i.ytimg.com/vi/"+x[0]+"/maxresdefault.jpg")

# How this works:
# You have youtube.com/watch?v=SMTHING link
# So the thumbnail link will be https://i.ytimg.com/vi/SMTHING/maxresdefault.jpg