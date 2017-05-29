skills = '''Illumiination
Light Binding
Prismatic Barrier
Lucent Singularity
Final Spark'''

len(skills)

f = open('skills.txt', 'wt')
f.write(skills)
f.close()

try:
    f = open('skills.txt', 'xt')
except FileExistsError:
    print('File is already exist')
print('Program terminate')

f = open('skills.txt', 'rt')
skills = f.read()
f.close()
print(skills)

# 자동으로 파일 닫기
with open('skills.txt', 'wt') as f:
    f.write(skills

