import webview

webview.create_window("Яндекс Переводчик", url='https://translate.yandex.ru/', width=1280, height=720)
webview.start()

# pyinstaller -F -w index.py -i "D:\NVG\projects\yandex-translate\favicon.ico" --hidden-import=clr