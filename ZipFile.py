import os
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
import io
from datetime import date


def zip_files_directories(folder='awesome-2021'):

    def dev():
        source_dir = '/tmp/abc/'
        file_name = f'{folder}-{date.today().strftime("%Y%m%d")}'
        relroot = f'/tmp/{file_name}/abc/'
        archive = io.BytesIO()
        with ZipFile(archive, 'w') as zip_archive:
            for root, dirs, files in os.walk(source_dir):
                zip_archive.write(root, os.path.relpath(root, relroot))
                for file_path in files:
                    with open(file_path, 'r') as file:
                        zip_entry_name = file.name
                        zip_file = ZipInfo(zip_entry_name)
                        zip_archive.writestr(zip_file, file.read())

            archive.seek(0)
            zip_archive.extractall('/tmp/testing/')

    def prod():
        source_dir = '/tmp/abc/'
        file_name = f'{folder}-{date.today().strftime("%Y%m%d")}'
        relroot = f'/tmp/{file_name}/abc/'
        archive = io.BytesIO()
        with ZipFile(archive, 'w', ZIP_DEFLATED) as zipfile:
            for root, dirs, files in os.walk(source_dir):
                zipfile.write(root, os.path.relpath(root, relroot))
                for file in files:
                    filename = os.path.join(root, file)
                    if os.path.isfile(filename):
                        arcname = os.path.join(
                            # os.path.relpath(root, relroot),
                            relroot,
                            file
                        )
                        zipfile.write(filename, arcname)

            archive.seek(0)
            zipfile.extractall('/tmp/testing')

    dev()


zip_files_directories()
