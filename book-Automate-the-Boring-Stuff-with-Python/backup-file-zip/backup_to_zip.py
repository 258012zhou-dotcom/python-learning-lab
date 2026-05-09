import zipfile,os
from pathlib import Path
def backup_to_zip(folder):
    folder=Path(folder).resolve()

    number=1
    while True:
        zip_filename=Path(folder.parts[-1]+'_'+str(number)+'.zip')
        if not zip_filename.exists():
            break
        number+=1

    print(f'creat {zip_filename}')
    # backup_zip=zipfile.ZipFile( zip_filename,'w')
    #
    # for folder_name, subfolders, filenames in os.walk(folder):
    #     folder_name=Path(folder_name)
    #     print(f'adding files in folder {folder_name}')
    #     for filename in filenames:
    #         print(f'adding file {filename}')
    #         backup_zip.write(folder_name / filename)
    # backup_zip.close()

    with zipfile.ZipFile(zip_filename,'w',zipfile.ZIP_DEFLATED) as backup_zip:
        for file in folder.rglob('*'):
            if file.is_file():
                print(f'adding file: {file.relative_to(folder)}')
                backup_zip.write(file,arcname=file.relative_to(folder))
    print('done.')
backup_to_zip(Path.home() / 'spam')

