import os
import shutil
path1 = '/Users/IMAN/Documents/Machine Learning/DSKC/Dataset fix/training/surat18'
path2 = '/Users/IMAN/Documents/Machine Learning/DSKC/Dataset fix/training/surat2'
path3 = '/Users/IMAN/Documents/Machine Learning/DSKC/Dataset fix/training/surat3'
files1 = os.listdir(path1)
files2 = os.listdir(path2)
files3 = os.listdir(path3)
for file in files1:
    print(file)
#     os.rename(os.path.join(path1, file),  os.path.join(path1, file[:-4] +'_28' + '.wav'))
# for file in files2:
#     os.rename(os.path.join(path2, file),  os.path.join(path2, file[:-4] +'_29' + '.wav'))
# for file in files3:
#     os.rename(os.path.join(path3, file),  os.path.join(path3, file[:-4] +'_30' + '.wav'))
# os.rename(os.path.join(path1, files1[0]),  os.path.join(path1, files1[0][:-4] +'_19' + '.wav'))
# os.rename(os.path.join(path2, files2[0]),  os.path.join(path2, files2[0][:-4] +'_20' + '.wav'))
# os.rename(os.path.join(path3, files3[0]),  os.path.join(path3, files3[0][:-4] +'_21' + '.wav'))