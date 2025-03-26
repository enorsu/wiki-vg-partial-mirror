import glob

def generate_index():
    files = glob.glob("./wikivg/*")
    html = """
<!DOCTYPE html>
<html>
<title>index</title>
<h1>Mirror of <a href='https://minecraft.wiki/w/Minecraft_Wiki:Projects/wiki.vg_merge'>minecraft.wiki/w/Minecraft_Wiki:Projects/wiki.vg_merge</a></h1>
<h1>Shitty mirror however</h1>

"""
    for x in files:
        
        html += "<a href='" + x + "'>" + x.removeprefix("./wikivg/") + "</a>\n"
        html += "<br>\n"
    html += "</html>"
    with open("index.html", "w") as y:
        y.write(html)

        

generate_index()
    


