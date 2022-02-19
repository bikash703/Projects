import os

def CreateNoExits(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername,files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")

files=os.listdir()
files.remove('main.py')

CreateNoExits('Images')
CreateNoExits('Docs')
CreateNoExits('Medias')
CreateNoExits('Zipfiles')
CreateNoExits('Csv_Files')
CreateNoExits('Others')
imgext=['.png','.jpg','.jpeg']
images=[file for file in files if os.path.splitext(file)[1].lower() in imgext ]
Docsext=['.txt','.docx','.doc','.pdf']
docs=[file for file in files if os.path.splitext(file)[1].lower() in Docsext] 
mediaext=['.mp4','.mp3','.flv']
media=[file for file in files if os.path.splitext(file)[1].lower() in mediaext] 
zipext=['.zip','.exe','.rar']
zipfiles=[file for file in files if os.path.splitext(file)[1].lower() in zipext]
csvext=['.csv','.xls','.xml','.excel']
csv_files=[file for file in files if os.path.splitext(file)[1].lower() in csvext]

other=[]
for file in files:
    fil=os.path.splitext(file)[1].lower()
    if (fil not in imgext) and (fil not in Docsext) and (fil not in mediaext) and (fil not in zipext) and (fil not in csvext) and os.path.isfile(file):
        other.append(file)

move('Images',images)
move('Docs',docs)
move('Medias',media)
move('Zipfiles',zipfiles)
move('Others',other)
move('Csv_Files',csv_files)
