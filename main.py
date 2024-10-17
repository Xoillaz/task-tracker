from sys import argv
from lib import Issues

act = argv[1]
arg_cnt = len(argv)

if act == "list" and arg_cnt == 2:
    Issues.ls("all")
elif arg_cnt == 3:
    opt = argv[2]
    if act == "add":
        Issues.add(opt)
    elif act == "delete":
        Issues.mk(opt, "deleted")
    elif act == "mark-in-progress":
        Issues.mk(opt, "in-progress")
    elif act == "mark-done":
        Issues.mk(opt, "done")
    elif act == "list":
        Issues.ls(opt)
    else:
        print("Invalid input, re-type please!")
elif act == "update" and arg_cnt == 4:
    Issues.mv(argv[2], argv[3])
else:
    print("Invalid input, re-type please!")
