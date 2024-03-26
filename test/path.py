import pathlib
import os
import urllib.request
from PIL import Image
from flask import current_app

u_id = 2
img_path = os.path.join(pathlib.Path(__file__).parent, 'user_account_imgs')

if not os.path.exists(os.path.join(pathlib.Path(__file__).parent, 'user_account_imgs')):
    os.makedirs(os.path.join(pathlib.Path(__file__).parent, 'user_account_imgs'))
    print('made')