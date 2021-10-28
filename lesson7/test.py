import os

print(os.name, os.uname())

# for root, dirs, files in os.walk('/home/tolic/tol/bat'):
#     # for d in dirs:
#     #     print(os.path.join(root, d) + os.path.sep)
#     for f in files:
#         print(os.path.join(root, f))

f_name = "/home/tolic/tol/bat/commands/translate/translate_textbox_to_english.sh"
f_item = 'dummy'
while f_item:
    f_name, f_item = os.path.split(f_name)
    print(f_item)
