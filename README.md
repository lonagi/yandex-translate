# Yandex Translate
Yandex translate application for Windows Desktop  
![Yandex](favicon.png)

## Build

With [pyinstaller](https://www.pyinstaller.org/) installed, run

    $ pyinstaller -F -w index.py -i "favicon.ico" --hidden-import=clr

Default resolution - `1280x720`