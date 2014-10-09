
###############################################
#1.Accept File as input
#2.Parse File.
#3.Insert logs in csv file format.
###############################################
import os,sys,glob,csv,collections

class Sfile(object):
    count=0
    def __init__(self):
        #os.stat()
        print "****************MENU*********************\n\
****************** [1]. File?\n\
*******************[2]. Directory?"
        count+=1
        menu_input=raw_input(">>")
        if menu_input =='1':print 'Initializing File Fun()';self.File_fun()
        elif menu_input =='2':print 'Initializing Dir Fun()';self.Dir_fun(menu_input)
        else: print 'Program Terminated',sys.exit(0)


    def Csv_fun(self,data):
        #self.data=data
        #check path
        if type(data)== dict:
            print data
            cwd=os.getcwd()
            if os.path.isfile(cwd+'my_csv.csv'):
                with open(cwd+'my_csv.csv','a') as csvfile:
                    csv_writer=csv.writer(csvfile)
                    csv_writer.writerow(data)

            else:
                
                with open(cwd+'my_csv.csv','w') as csvfile:
                    headers=['FIle Name','st_mode: protection bits' ,'st_ino: inode number','st_dev: device','st_nlink: number of hard links',\
                             'st_uid: user id of owner','st_gid: group id of owner','st_size: size of file, in bytes','st_atime: time of most recent access',\
                             'st_mtime: time of most recent content modification','st_ctime: time of most recent metadata change']
                    csv_writer=csv.writer(csvfile)
                    csv_writer.writerow(headers)
                    self.Csv_fun(data)
            
            
        else:
            
            print data
            cwd=os.getcwd()
            if os.path.isfile(cwd+'my_csv.csv'):
                with open(cwd+'my_csv.csv','a') as csvfile:
                    csv_writer=csv.writer(csvfile)
                    csv_writer.writerow(data)

            else:
                
                with open(cwd+'my_csv.csv','w') as csvfile:
                    headers=['FIle Name','st_mode: protection bits' ,'st_ino: inode number','st_dev: device','st_nlink: number of hard links',\
                             'st_uid: user id of owner','st_gid: group id of owner','st_size: size of file, in bytes','st_atime: time of most recent access',\
                             'st_mtime: time of most recent content modification','st_ctime: time of most recent metadata change']
                    csv_writer=csv.writer(csvfile)
                    csv_writer.writerow(headers)
                    self.Csv_fun(data)
        return data

        
    def __del__(self):
        return 'Object Destroyed'

    def File_fun(self):
        '''Handle FIle parsing'''
        m_input=raw_input("Example:\n /home/folder/my_file.extension")
        
        if m_input:
            try:
                data=collections.OrderedDict()
                stat=str(s.stat(m_input))
                for i in stat:
                    if '=' in i:
		a1=i.split('=')
		data[a1[0]]=a1[1]
            except IOError as E:
                if  count>3: print 'Maximum Trial Exceeded!!!';break
                    
                else:print 'Path is NuLL**********Application Restarted!!!!!!!!';self.__init__()
      
            
                
        else:
             self.__init__()
             print 'Maximum Trial Exceeded!!!';break if count>=3  else self.__init__()
        #data['flag']='File_fun'
             li.insert(0,'File_Fun')
        self.Csv_fun(data)

         return 'File Fun() successfully implemented'
        
                

    def Dir_fun(self,inp):
        '''Handle Dir parsing'''
        m_input=raw_input("Example:\n /home/folder/")
        
        if m_input:
            try:
                
                files=os.listdir(m_input);os.chdir(m_input)
                li=[]
                for f_ile in files:
                    stat=str(s.stat(f_ile))
                    data=collections.OrderedDict()
                    for i in stat:
                        if '=' in i:
                            a1=i.split('=')
                            data[a1[0]]=a1[1]
                    li.append(data)
            except Exception ,e:
                print 'Invalid Directory'
                if  count>3: print 'Maximum Trial Exceeded!!!';break
                else:print '******Application Restarted!!!!!!!!';self.__init__()
        else:
             self.__init__()
             print 'Maximum Trial Exceeded!!!';break if count>=3  else self.__init__()
        li.insert(0,'Dir_fun')
        self.Csv_fun(data)

         return 'Dir Fun() successfully implemented'
