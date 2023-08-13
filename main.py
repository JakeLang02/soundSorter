import os 
import shutil

# path to splice directory
dir_path = '/Users/jlang/Splice/sounds/packs' 
tar_path = '/Users/jlang/Desktop/samples/'

dirAndKeys = {}
samp_name_and_orig_path = {}

def main():
    
    print("\nEnter the keywords you want me to associate with each directory as a space seperated list.\n")
    print("Example: \n")
    print("Directory Name: risers\n")
    print("(the next line would be your input)\n")
    print("riser sweep\n")
    
    tar_path = '/Users/jlang/Desktop/samples/'
    drum_tar_path = '/Users/jlang/Desktop/samples/drums/'
    # kicks snares loops percs
    
    obj = os.scandir(tar_path)
    
    for entry in obj:
        
        if entry.is_dir():
            
            if(entry.name == 'misc'):
                continue
            
            else:
                print("Directory Name: " + entry.name)
                keyWords = input()
                keyList = keyWords.split()
                dirAndKeys[entry.name] = keyList
    
    for root_dor, cur_dir, files in os.walk(dir_path): 
        
        if(files)!= []:
            
            for i in files:
                
                rel_path = os.path.join(root_dor,i)
                samp_name_and_orig_path[i] = rel_path


               
    for sample, path in samp_name_and_orig_path.items():
        
        tar_path = '/Users/jlang/Desktop/samples/'
        assigned = False 
        
        for directory, keywords in dirAndKeys.items():
            tar_path = '/Users/jlang/Desktop/samples/'
            
            for word in keywords: 
                tar_path = '/Users/jlang/Desktop/samples/'
                
                if (word in sample.lower()):
                    
                    if(word == "kick"):
                        shutil.copy(path, (drum_tar_path + "kicks/"))
                        assigned = True
                        
                    elif(word == "snare"):
                        shutil.copy(path, (drum_tar_path + "snares/"))
                        assigned = True
                    
                    elif(word == "perc"):
                        shutil.copy(path, (drum_tar_path + "percs/"))
                        assigned = True
                    
                    elif(word == "loop"):
                        shutil.copy(path, (drum_tar_path + "loops/"))
                        assigned = True
                    else:
                        tar_path += (directory + "/")
                        shutil.copy(path, tar_path)
                        assigned = True
        
        if(assigned == False):
            tar_path += ("misc/")
            shutil.copy(path, tar_path)
        

        


    





'''
if('fx' in i.lower()):
                        tar_path = '/Users/jlang/Desktop/samples/fx/'
                        rel_path = os.path.join(root_dor,i)
                        shutil.copy(rel_path,tar_path+i)
'''


main()
        
