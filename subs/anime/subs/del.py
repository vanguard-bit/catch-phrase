import os as os
print(os.getcwd())
for cf, sf, fn in os.walk('.'):
    for file in fn:
        if file.endswith('.ass'):
            print(file)
        # os.unlink(flie)
