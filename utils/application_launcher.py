import subprocess

# configure and add more
APP_TO_PATH = {
    'chrome': r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    # 'discord': r'"C:\Users\eyal darmon\AppData\Local\Discord\app-1.0.9004'
}


def launch_application(application_name: str):
    if application_name in APP_TO_PATH:
        application_name = APP_TO_PATH[application_name]
    subprocess.call(application_name)


# if __name__ == '__main__':
#     launch_application('discord')
