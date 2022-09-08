import os
from sys import executable

# Declaração de diretório
directory = '/home/l4ndrade/Downloads/'
file_names = os.listdir(directory)
# Declação de listas de formatos
image_ext = ['.jpg', '.jpeg', '.png', '.psd', '.gif']
audio_ext = ['.mp3', '.wav']
document_ext = ['.pdf', '.txt', '.xlsx', '.docx', '.pptx', '.json', '.rar', '.zip']
video_ext = ['.mp4', '.avi', '.m4v', '.mov', '.mpg', '.mpeg', '.wmv', '.asf']
code_ext = ['.js', '.py', '.html', '.css']
executable_ext = ['.deb', '.exe']

directory_list = ['dowloaded-images', 'dowloaded-audios', 'dowloaded-documents', 'dowloaded-videos', 'dowloaded-codes','downloaded-executables', 'others']

for folder in directory_list:
    if not os.path.isdir(os.path.join(directory, folder)):
        os.mkdir(os.path.join(directory, folder))

for file in file_names:
    if os.path.isdir(os.path.join(directory, file)):
        pass
    else:
        try:
            invfile = file[::-1]
            extention = invfile[invfile.index('.')::-1].lower()
        except:
            new_dir = directory_list[6]
        else:
            if extention in image_ext:
                new_dir = directory_list[0]
            elif extention in audio_ext:
                new_dir = directory_list[1]
            elif extention in document_ext:
                new_dir = directory_list[2]
            elif extention in video_ext:
                new_dir = directory_list[3]
            elif extention in code_ext:
                new_dir = directory_list[4]
            elif extention in executable_ext:
                new_dir = directory_list[5]
            else: # Outros
                new_dir = directory_list[6]
        new_dir = os.path.join(directory, new_dir)
        os.rename(os.path.join(directory, file), os.path.join(new_dir, file))
