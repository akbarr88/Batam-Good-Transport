import os, shutil, glob
src = r"C:\Nutta\batam-good-transport\images\tamu"
dst = r"C:\Nutta\batam-good-transport\images\gallery"
os.makedirs(dst, exist_ok=True)
files = sorted(glob.glob(os.path.join(src, "*.webp")))
for i, f in enumerate(files, 1):
    out = os.path.join(dst, "gallery-%02d.webp" % i)
    shutil.copy2(f, out)
    print("%02d <- %s" % (i, os.path.basename(f)))
print("copied", len(files), "files to", dst)
