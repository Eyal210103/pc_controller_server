import subprocess

# configure and add more
APP_TO_PATH = {
    'chrome': r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
}


def launch_application(application_name: str):
    if application_name in APP_TO_PATH:
        application_name = APP_TO_PATH[application_name]
    subprocess.call(application_name)
