import yaml
data_file = open("website/site.yaml")
data = yaml.load(data_file, Loader=yaml.FullLoader)

with open("website/site.yaml", "r") as stream:
    out = yaml.load(stream, Loader=yaml.FullLoader)

a = data["ingridients"]
ing = len(a)

def list_make():
    x = []
    i = 0
    while i < ing:
        x.append("<li>")
        x.append(a[i])
        x.append("</li>")
        i += 1
    return ''.join(x)


def file_get():
    f = open("website/template.html", "r")
    return (f.read())

def replace():
    html = file_get()
    x = html.replace("<!--title-->", data["title"])
    y = x.replace("<!--name-->", data["title"])
    z = y.replace("<!--instructions-->", data["recepie"])
    q = z.replace("<!--list-->", list_make())
    return(q)

print(replace())

b = data["title"]
c = b.replace(" ", "_")

def new_file():
    f = open(c + ".html", "x")
    f.write(replace())
    f.close()