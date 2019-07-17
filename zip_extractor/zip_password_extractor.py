import zipfile, os, re

#move to the folder that has the zipfiles
folder = '/Users/syed.masud/Documents/Shoaib/Activities_for_customers/Phantom/Realogy/Scripts'
os.chdir(folder)
#Checking all the files in this folder
for i in os.listdir('zip_extractor'):
    if i.endswith('.zip'):
        os.chdir('/Users/syed.masud/Documents/Shoaib/Activities_for_customers/Phantom/Realogy/Scripts/zip_extractor')
        zip_file_obj = zipfile.ZipFile(i)
        print('Extracting %s' % i)
        try:
            zip_file_obj.extractall()
        except RuntimeError as e:
            if 'encrypted' in str(e):
                #zip_file_obj.extractall(pwd='infected')
                print('%s is password protected, trying again using pre-defined password' % i)
                try:
                    zip_file_obj.extractall(pwd='infected')
                except RuntimeError as f:
                    if 'Bad password' in str(f):
                        print('****%s is not extractable using the pre-defined password****' % i)

        zip_file_obj.close()
