

from darknet_commands import make_commands
import glob


dir_ref = r"~\darknet\build\darknet\x64\BCCD"
datasets = ["train", "valid", "test"]

for d in datasets:
    img_paths = glob.glob(f"{dir_ref}/{d}/*.jpg")
    with open(f"{dir_ref}/{d}.txt", "w") as f:
        data = "\n".join(img_paths)
        f.write(data)

with open(f"{dir_ref}/train/_darknet.labels", "r") as f, \
        open(f"{dir_ref}/classes.names", "w") as f2:
    data = f.readlines()
    n_class = len(data)
    f2.writelines(data)

with open(f"{dir_ref}/obj.data", "w") as f:
    f.write(f"classes = {n_class}\n")
    f.write(f"train = {dir_ref}/train.txt" + "\n")
    f.write(f"valid = {dir_ref}/valid.txt" + "\n")
    f.write(f"names = {dir_ref}/classes.names" + "\n")
    f.write(f"backup = {dir_ref}/backup")

versions = [3, 4]
modes = ["train", "test"]
for v in versions:
    for m in modes:
        with open(f"{dir_ref}/yolov{v}_{m}.cfg", "w") as f, \
                open(f"darknet_cfg/yolov{v}_{m}.cfg", "r") as data:
            original = data.readlines()
            yolo_index = [i for i, s in enumerate(original) if "[yolo]" in s]
            for i in yolo_index:
                if "filters" not in original[i - 4]:
                    print(
                        f"yolov{v}.cfg is different from original. check darknet.")
                else:
                    original[i - 4] = f"filters={(n_class + 5) * 3}\n"

                if "classes" not in original[i + 3]:
                    print(
                        f"yolov{v}.cfg is different from original. check darknet.")
                else:
                    original[i + 3] = f"classes={n_class}\n"
            f.writelines(original)


darknet_dir = r"~\darknet\build\darknet\x64"
for v in versions:
    commands = make_commands(dir_ref, darknet_dir, v)
    with open(f"{dir_ref}/commands{v}.txt", mode="w") as f:
        f.write(commands)
