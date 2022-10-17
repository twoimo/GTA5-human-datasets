import os

file_names=os.listdir()

for i in file_names:
    if(i[2:4]=='10'):
        os.rename(i,'0015'+i[4:])
for i in file_names:
    if(i[2:4]=='09'):
        os.rename(i,'0014'+i[4:])
for i in file_names:
    if(i[2:4]=='08'):
        os.rename(i,'0013'+i[4:])
for i in file_names:
    if(i[2:4]=='07'):
        os.rename(i,'0009'+i[4:])
for i in file_names:
    if(i[2:4]=='06'):
        os.rename(i,'0008'+i[4:])
for i in file_names:
    if(i[2:4]=='05'):
        os.rename(i,'0006'+i[4:])
for i in file_names:
    if(i[2:4]=='04'):
        os.rename(i,'0005'+i[4:])
for i in file_names:
    if(i[2:4]=='03'):
        os.rename(i,'0004'+i[4:])
for i in file_names:
    if(i[2:4]=='02'):
        os.rename(i,'0003'+i[4:])
    
    
    
    
    
    
    
    