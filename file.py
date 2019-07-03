# 文件作业
import os

os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1', 'w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2', 'w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3', 'w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')


print('文件中包含"qytang"关键字的文件为:')
print('方案一')
for a in os.listdir(os.getcwd()):             # 在返回指定的当前目录下的'文件或目录'
    if os.path.isfile(a):
        for b in (open(a, 'r')):
            if 'qytang' in b:
                print('    ', a)


# topdown的默认值是True，表示首先返回根目录树下的文件，然后遍历目录树下的子目录。
# topdown的值设为False时，则表示先遍历目录树下的子目录，返回子目录下的文件，最后返回根目录下的文件
print('方案二:')
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for a in files:
        for b in (open(a, 'r')):
            if 'qytang' in b:
                print('    ', a)



# 完成清理工作
os.chdir('..')
for root, dirs, files in os.walk('test', topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.removedirs('test')