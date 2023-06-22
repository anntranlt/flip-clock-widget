import webview, requests

webview.DRAG_REGION_SELECTOR = "body"
html_file = "index.html"
css_file = "styles.css"
js_file = "flip-animation.js"

def readFile(name):
    file = open(name, "r")
    return file.read()

def load(window):
    load_css(window)
    evaluate_js(window)

def display_screen_info():
    screens = webview.screens
    print('Available screens are: ' + str(screens))

def toggle_fullscreen(window):
    window.toggle_fullscreen()

def load_css(window):
    css = readFile(css_file)
    window.load_css(css)

def evaluate_js(window):
    js = readFile(js_file)
    window.evaluate_js(js)


html = readFile(html_file)

if __name__ == '__main__':
    window = webview.create_window(
        'Run custom JavaScript', 
        html=html, 
        frameless=True, 
        easy_drag=False,
        transparent=True,
        width=1000,
        height=400
    )    
    webview.start(load, window)
