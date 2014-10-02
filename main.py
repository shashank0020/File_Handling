###############################################
#1.Accept File as input
#2.Parse File.
#3.Insert logs in csv file format.
###############################################
import os,sys,glob,

class Sfile(object):
    
    def __init__(self):
        #os.stat()
        print "****************MENU*********************\n\
****************** [1]. File?\n\
*******************[2]. Directory?"
        menu_input=raw_input(">>")
        if menu_input =='1':print 'Initializing File Fun()';self.File_fun()
        elif menu_input =='2':print 'Initializing Dir Fun()';self.Dir_fun(menu_input)
        else: print 'Program Terminated',sys.exit(0)

        
            


        :m_input=raw_input("Example:\n /home/folder/my_file.extension");\
                                    while(m_input=='')
                                     if m_input:self.File_Fun(m_input);print 'Calling File Function'
                                    
                                                            
        
        
        
            
        
        
        
        '/home/your_directory/file_name' ")
        return 'Class Initialized'


    def __del__(self):
        return 'Object Destroyed'

    def File_fun(self):
        '''Handle FIle parsing'''
        m_input=raw_input("Example:\n /home/folder")
        count=0
        if m_input:stat=os.stat(m_input)
            
        pass  else  count+=1;self.__init__()
        
            

    def Dir_fun(self,inp):
        '''Handle Dir parsing'''
        
    
