sitemap = open("sitemap.xml", "w")
# for i in range(1,51):
#     url = "http://sweetspots.me/cities/id/" + str(i)
#     sitemap.write("\n<url>\n  <loc>" + url + "</loc>\n</url>")
# for i in range(1,151):
#     url = "http://sweetspots.me/attractions/id/" + str(i)
#     sitemap.write("\n<url>\n  <loc>" + url + "</loc>\n</url>")
# for i in range(1,151):
#     url = "http://sweetspots.me/restaurants/id/" + str(i)
#     sitemap.write("\n<url>\n  <loc>" + url + "</loc>\n</url>")

for i in range(1,51):
    url = "localhost:5000/cities/id/" + str(i)
    sitemap.write("\n<url>\n  <loc>" + url + "</loc>\n</url>")
for i in range(1,151):
    url = "localhost:5000/attractions/id/" + str(i)
    sitemap.write("\n<url>\n  <loc>" + url + "</loc>\n</url>")
for i in range(1,151):
    url = "localhost:5000/restaurants/id/" + str(i)
    sitemap.write("\n<url>\n  <loc>" + url + "</loc>\n</url>")
sitemap.close()