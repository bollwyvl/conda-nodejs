import hashlib
import os
try:
    from urllib.request import urlretrieve
except:
    from urllib import urlretrieve

import zipfile
import tempfile
import shutil
import glob


CHECKSUMS = {
    "x86": {
        "node.exe": "4e9ca71d4bd56df6b2afa51c2a0937ff94ae7c3f04c1306a4d3bd77ca232cea8",
        "node.lib": "fd653c44129836021be6ad5f2822807158fb50f92c4bc4c91eda3e19ce0e0c40",
    },

    "x64": {
        "node.exe": "3b595ef2e9232b5bebabc69dbf52316d0e7a7c2b2a2e62abae89787e6f001e44",
        "node.lib": "6863f29249ce79ddccb2ffcf1966d630e4f6efea695c6b20695d4d6a64828799",
    }

}

ARCH = {
    "32": "x86",
    "64": "x64",
}[os.environ["ARCH"]]

ROOT_URL = "https://nodejs.org/dist/v4.2.6/win-{}/".format(ARCH)
FILES = ["node.exe", "node.lib"]
TARGET_DIR = os.path.join(os.environ["PREFIX"], "Scripts")
if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)

for filename in FILES:
    url = "{}{}".format(ROOT_URL, filename)
    full_filename = os.path.join(TARGET_DIR, filename)
    urlretrieve(url, full_filename)

    with open(full_filename, "rb") as f:
        contents = f.read()
    assert hashlib.sha256(contents).hexdigest() == CHECKSUMS[ARCH][filename]

tmpdir = tempfile.mkdtemp()

NPM_PATH = os.path.join(TARGET_DIR, "node_modules", "npm")

try:
    urlretrieve("https://github.com/npm/npm/archive/v3.7.1.zip",
                os.path.join(tmpdir, "npm.zip"))

    with zipfile.ZipFile(os.path.join(tmpdir, "npm.zip"), "r") as z:
        z.extractall(tmpdir)

    shutil.copytree(
        os.path.join(tmpdir, "npm-3.7.1"),
        NPM_PATH
    )

    shutil.copy(
        os.path.join(NPM_PATH, "bin", "npm.cmd"),
        os.path.join(TARGET_DIR)
    )

    print(glob.glob(os.path.join(NPM_PATH)))

except Exception as err:
    raise err
finally:
    shutil.rmtree(tmpdir)
