import os


with open("/model/run.sh", 'w') as f:
    _, vids, _ = next(os.walk("/dataset"))

    f.write("mkdir /model/results\n")

    for vid in vids:
        f.write(f"python3 /model/TIP/demo_my.py --testset_dir /dataset --video_name {vid} --save_result_dir /model/results --degradation BD\n")

    f.write("chmod -R 0777 /model\n")

os.system("chmod 0777 /model/run.sh")
os.system("/model/run.sh")
