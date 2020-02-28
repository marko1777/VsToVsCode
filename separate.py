import os

rootdir = "c:\\code\\m_sw_main\\"
targetdir = "e:\\exp\\sep\\m_sw_main\\"

for subdir, dirs, files in os.walk(rootdir):
    first = True
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".cpp") or filepath.endswith(".h"): 
            s = subdir.split('\\')
            r = targetdir + ('\\'.join(s[3:]))
            if first:
                first = False
                os.system("md " + r)
            
            ss = "mklink " + r + "\\" + file + " " + filepath
            os.system(ss)
            
        else:
            continue






# import os

# rootdir = "/mnt/c/code/m_sw_main/"
# targetdir = "/mnt/e/exp/sep/m_sw_main/"

# for subdir, dirs, files in os.walk(rootdir):
#     first = True
#     for file in files:
#         filepath = subdir + os.sep + file
#         if filepath.endswith(".cpp") or filepath.endswith(".h"): 
#             s = subdir.split('/')
#             r = targetdir + ('/'.join(s[5:]))
#             # if first:
#             #     first = False
#             #     os.system("mkdir -p " + r)
            
#             # ss = "ln -s " + filepath + " " + r + "/" +file
#             # os.system(ss)

#         else:
#             continue