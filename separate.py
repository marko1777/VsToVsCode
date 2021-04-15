import os

# rootdir = "c:\\code\\m_sw_main\\"
# rootdir = "c:\\code\\m_sw_main\\NUCLINE\\Camera\\Drivers\\XRay\\"
rootdir = "c:\\code\\m_sw_main\\NUCLINE\\Camera\\Drivers\\"
# rootdir = "c:\\code\\m_sw_main\\NUCLINE\\Camera\\Applications\\PlugIns\\FlatCT"
# rootdir = "c:\\code\\m_sw_main\\NUCLINE\\_tests\\FlatCT\\"
# rootdir = "e:\\code\\honeycomb\\"
targetdir = "e:\\exp\\sep\\m_sw_main\\"
# targetdir = "e:\\exp\\sep\\honeycomb\\"

for subdir, dirs, files in os.walk(rootdir):
    first = True
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".cpp") or filepath.endswith(".h") or filepath.endswith(".cu"): 
            s = subdir.split('\\')
            r = targetdir + ('\\'.join(s[3:]))
            if first:
                first = False
                os.system("md " + r)
            
            ss = "mklink " + r + "\\" + file + " " + filepath
            os.system(ss)
            
        else:
            continue



# mklink e:\code\feature\MSC_SDK\DataFilters2\include\MExtrema2.h c:\code\honeycomp_filter\MSC_SDK\DataFilters2\include\MExtrema2.h
# mklink e:\code\feature\MSC_SDK\DataFilters2\include\MHoneycomp.h c:\code\honeycomp_filter\MSC_SDK\DataFilters2\include\MHoneycomp.h
# mklink e:\code\feature\MSC_SDK\DataFilters2\source\MHoneycomp.cpp c:\code\honeycomp_filter\MSC_SDK\DataFilters2\source\MHoneycomp.cpp
# mklink e:\code\feature\MSC_SDK\ScientificApplications\include\MRoiPoly.h c:\code\honeycomp_filter\MSC_SDK\ScientificApplications\include\MRoiPoly.h
# mklink e:\code\feature\MSC_SDK\DataFilters2\include\MFspecial.h c:\code\honeycomp_filter\MSC_SDK\DataFilters2\include\MFspecial.h



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