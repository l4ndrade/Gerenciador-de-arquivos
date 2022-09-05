import os

# Declaração de diretório
directory = '/home/l4ndrade/Downloads/'
file_names = os.listdir(directory)
# Declação de listas de formatos
image_ext = ['.jpg', '.jpeg', '.png', '.psd', '.gif']
audio_ext = ['.mp3', '.wav']
document_ext = ['.pdf', '.txt', '.xlsx', '.docx', '.pptx', '.json', '.rar', '.zip']
video_ext = ['.mp4', '.avi', '.m4v', '.mov', '.mpg', '.mpeg', '.wmv', '.asf']
code_ext = ['.js', '.py', '.html', '.css']

directory_list = ['dowloaded-images', 'dowloaded-audios', 'dowloaded-documents', 'dowloaded-videos', 'dowloaded-codes', 'others']

for folder in directory_list:
    if not os.path.isdir(os.path.join(directory, folder)):
        os.mkdir(os.path.join(directory, folder))

for file in file_names:
    if os.path.isdir(os.path.join(directory, file)):
        pass
    else:
        invfile = file[::-1]
        extention = invfile[invfile.index('.')::-1].lower()

        if extention in image_ext:
            new_dir = 'dowloaded-images'
        elif extention in audio_ext:
            new_dir = 'dowloaded-audios'
        elif extention in document_ext:
            new_dir = 'dowloaded-documents'
        elif extention in video_ext:
           new_dir = 'dowloaded-videos'
        elif extention in code_ext:
            new_dir = 'dowloaded-codes'
        else: # Outros
            new_dir = 'others'
        new_dir = os.path.join(directory, new_dir)
        os.rename(os.path.join(directory, file), os.path.join(new_dir, file))
