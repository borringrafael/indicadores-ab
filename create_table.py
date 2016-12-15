import os
import sys
import re
from simpledbf import Dbf5


class CreateDB(object):

    def __init__(self, folders, folder_tmp):
        self.folders = []
        for folder in folders:
            if os.path.isdir(folder):
                self.folders.append(folder)
        self.folder_tmp = folder_tmp
        self.dbfs = []
        CreateDB.test_folder_tmp(self)

    def test_folder_tmp(self):
        if os.path.isdir(self.folder_tmp):
            os.system('rm -rf %s' % self.folder_tmp)
            os.mkdir(self.folder_tmp)
        else:
            os.mkdir(self.folder_tmp)
        CreateDB.test_files_dbf(self)

    def test_files_dbf(self):
        for folder in self.folders:
            print(folder)
            files = list(filter(
                                lambda x: re.match('.*dbf$', x, re.I),
                                sorted(os.listdir(folder)),
                                ))
            print('... %s OK!' % files[0])
            self.dbfs.append('%s/%s' % (folder, files[0]))
        CreateDB.createsql(self)

    def createsql(self):
        tables = []
        for file in self.dbfs:
            name = file.split('/')[-1][:-4]
            rename = re.match(r'[^\d_]*', name, re.I)
            print('Importando tabela de %s' % file)
            dbf = Dbf5(file, codec='latin-1')
            dbf.to_textsql('%s/%s.sql' % (
                                          self.folder_tmp,
                                          name,
                                          ), '/dev/null', sqltype='postgres')
            file_r = open('%s/%s.sql' % (
                                         self.folder_tmp,
                                         file.split('/')[-1][:-4],
                                         ), 'r', encoding='utf-8')
            sub = re.sub(name, rename.group(0).lower(), file_r.read())
            delline = re.sub(r'\\copy.*', '\n', sub)
            removeinvalid = re.sub(r'\00[\w]*', '', delline)
            file_r.close()
            file_w = open('%s/%s.sql' % (
                                         self.folder_tmp,
                                         file.split('/')[-1][:-4]),
                                         'w', encoding='utf-8',
                                         )
            file_w.write(removeinvalid)
            file_w.close()
            tables.append(removeinvalid)
        sql = open('createdb.sql', 'w')
        for table in tables:
            sql.write(table)
        sql.close()


if __name__ == '__main__':
    CreateDB(sys.argv, '/var/tmp/pgcreate')
