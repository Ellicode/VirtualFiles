from virtualfiles import File,Directory
rootdir = Directory()
mydir = Directory("python", rootdir)

myfile = File("abc.py", "AABBCC", mydir)
mydir = Directory("images", rootdir)
imgfile = File("123.png", "AABBCC", mydir)
imgfile.edit("123.png", "AABBCC. I am an image",)

print(rootdir.contents)
