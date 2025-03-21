import os,shutil,subprocess,re
def file_type(file):
        command=f'""file "{folder_path}/{file}"'
        result=subprocess.run(command,capture_output=True,text=True, shell=True)
        reply=result.stdout
        #print(reply)
        start_index=reply.index(": ")+2
        reply=reply[start_index:]
        end_index=reply.find(",")
        reply=reply[:end_index] if end_index!=-1 else reply.strip()
        return reply
folder_path=input("enter the folder path")
typesOfFiles=[]
if os.path.exists(folder_path):
    for file in os.listdir(folder_path):
        new_folder = re.sub(r'[\\/*?:"<>|]', "_", file_type(file))
        oldPath = os.path.join(folder_path, file)
        newPath = os.path.join(folder_path, new_folder)
        '''oldPath=f'"{folder_path}/{file}"'
        newPath=f'"{folder_path}/{new_folder}"'''
        if file.startswith("."):
            continue
        if(new_folder=="directory" or new_folder=="Directory"):
            continue
        if(os.path.exists(newPath)==False):
            try:
                os.makedirs(newPath)
            except Exception as e :
                print(f"failed to create a directory for {new_folder}")
            try:
                shutil.move(oldPath,newPath)
            except Exception as e:
                print(f"Failed to move file {file} to {new_folder}")
        else:
            try:
                shutil.move(oldPath,newPath)
            except Exception as e:
                print(f"Failed to move file {file} to {new_folder}")        
else:
    print("Entered path is not correct")