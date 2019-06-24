# 课后作业(1)

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'liang'
COURSE_FEES_SEC = 16666.88888
COURSE_FEES_liang  = 2415.999

# 传统技术
# line1 = 'Department1 name:%-8s Manager:%-9s COURSE FEES:%-10.3f The End!' % (department1, depart1_m, COURSE_FEES_SEC)
# line2 = 'Department2 name:%-8s Manager:%-9s COURSE FEES:%-10.3f The End!' % (department2, depart2_m, COURSE_FEES_liang)

# 新方法
line1 = "Department1 name:{0:<9}" "Manager:{1:<9}" "COURSE FEES:{2:<10.2f}" "The End!".format(department1, depart1_m, COURSE_FEES_SEC)
line2 = "Department1 name:{0:<9}" "Manager:{1:<9}" "COURSE FEES:{2:<10.2f}" "The End!".format(department2, depart2_m, COURSE_FEES_liang)

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
