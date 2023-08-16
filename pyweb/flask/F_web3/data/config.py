from pathlib import Path    #root잡고 'data/users.db' 하면 database 호출됨

SECRET_KEY = b'r9\xee*\x13\x96\xf7L\x9c8\x98\x8aM\xfb\x8e~'
DATABASE = Path()/'data/users.db'
print(DATABASE)

'''
[SECRET_KEY]
<python console>
import os
os.urandom(16)
b'\xac\xdfS\x01;y\x9cU\xd2\xf1\x13d\x16\xff)\x11'
이렇게 해서 키값 그냥 줬다..!

or

import secrets
print(secrets.token_hex())
bb76eca1b2a2de21966b99b7009a1addac53140d1bedcc9a0f7d61c8d873c80b
'''
