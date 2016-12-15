import os
import sys
import re
from simpledbf import Dbf5


class CreateCsvs(object):

    def __init__(self, folders):
        self.folders = []
        for folder in folders:
            if os.path.isdir(folder):
                self.folders.append(folder)

        self.dbfs = []
        CreateCsvs.test_files_dbf(self)

    def test_files_dbf(self):
        for folder in self.folders:
            print(folder)
            files = list(filter(
                                lambda x: re.match('.*dbf$', x, re.I),
                                sorted(os.listdir(folder)),
                                ))
            for file in files:
                print('... %s OK!' % file)
                self.dbfs.append('%s/%s' % (folder, file))
        CreateCsvs.createsql(self)

    def createsql(self):
        if os.path.isdir('Csvs'):
            os.system('rm -rf %s' % 'Csvs')
            os.mkdir('Csvs')
        else:
            os.mkdir('Csvs')
        for file in self.dbfs:
            name = file.split('/')[-1][:-4]
            rename = re.match(r'[^\d_]*', name, re.I)
            print('Importando dados de %s' % file)
            if not os.path.isdir('Csvs/%s' % rename.group(0)):
                os.mkdir('Csvs/%s' % rename.group(0))
            dbf = Dbf5(file, codec='latin-1')
            dbf.to_textsql('/dev/null', 'Csvs/%s/%s.csv' % (
                                                            rename.group(0),
                                                            name),
                                                            sqltype='postgres',
                                                            )

if __name__ == '__main__':
    CreateCsvs(sys.argv)
