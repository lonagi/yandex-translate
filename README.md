# Yandex Translate
Yandex translate application for Desktop    

![Yandex](favicon.png)

## Browser Support

![Windows 10](https://raw.githubusercontent.com/EgoistDeveloper/operating-system-logos/master/src/48x48/windows.png) | ![OS X](https://raw.githubusercontent.com/EgoistDeveloper/operating-system-logos/master/src/48x48/mac.png)
--- | --- |
Latest ✔ | Latest ✔ |

<!-- ## CLI

    $ ./yacli.py [text] [transl.langs]

**transl.langs** - ru-en is arg. by default

### For example 

![Example](carbon.png) -->

## Build binary file

With [pyinstaller](https://www.pyinstaller.org/) installed, run

    $ pyinstaller -F -w index.py -i "favicon.ico" --hidden-import=clr

Default resolution - `1280x720`  