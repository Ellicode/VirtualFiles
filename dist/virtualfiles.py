import datetime
""" from typing import Union """
""" class XML(object):
    def __init__(self, data: Union[dict, bool], root='RootDirectory'):
        self.xml = f'<{root}>'
        self.xml += "\n"

        if isinstance(data, dict):
            for key, value in data.items():
                
                self.xml += str(XML(value, key))
                self.xml += "\n"

        elif isinstance(data, (list, tuple, set)):
            for item in data:
                self.xml += str(XML(item, 'File'))
                self.xml += "\n"


        else:
            self.xml += str(data)
            self.xml += "\n"
        self.xml += f'</{root}>'
        self.xml = str(self.xml)
    def __str__(self):
        return str(self.xml)
    def export(self, filename):
        with open("{}.xml".format(filename), "w") as f:
            f.write(self.xml) """

class Directory:
    def __init__(export, folderName='root', parent=False):
        export.contents = []
        if parent:
            parent.contents.append(
                {
                    folderName: export.contents,
                }
            )
        


        
class File:
    def __init__(self, filename, content, dir, **kwargs):
        self.filename = filename
        self.content = content
        self.kwargs = kwargs
        self.dir = dir
        self.dir.contents.append(
            {
                "FileName": self.filename,
                "Content": self.content,
                "Modified-at": datetime.datetime.now().strftime("%d %B %Y, %H:%M:%S")
            }
        )
    def delete(self):
        for i in range(len(self.dir.contents)):
            if self.dir.contents[i]['FileName'] == self.filename:
                del self.dir.contents[i]
                break
    def edit(self, filename, content, **kwargs ):
        for i in range(len(self.dir.contents)):
            if self.dir.contents[i]['FileName'] == self.filename:
                del self.dir.contents[i]
                break
        self.filename = filename
        self.content = content
        self.kwargs = kwargs
        self.dir.contents.append(
            {
                "FileName": self.filename,
                "Content": self.content,
                "Modified-at": datetime.datetime.now().strftime("%d %B %Y, %H:%M:%S")
            }
        )


rootdir = Directory()
mydir = Directory("python", rootdir)

myfile = File("abc.py", "AABBCC", mydir)
mydir = Directory("images", rootdir)
myfile = File("123.png", "AABBCC", mydir)
""" print(XML(mydir.contents)) """
print(rootdir.contents)
