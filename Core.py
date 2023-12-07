import os
import eel
from flask import Flask, render_template
from github import Github

def check_for_updates():
    repo_owner = 'donatkauler22'  # Замените на имя пользователя владельца репозитория
    repo_name = 'VesendisLauncher'   # Замените на название вашего репозитория
    current_version = '1.0'  # Замените на текущую версию вашего приложения

    try:
        g = Github()
        repo = g.get_repo(f"{repo_owner}/{repo_name}")
        latest_release = repo.get_latest_release().tag_name

        if latest_release != current_version:
            print(f"Найдено обновление: {latest_release}. Обновление будет установлено.")
            os.system('pip install --upgrade git+https://github.com/{repo_owner}/{repo_name}.git')

    except Exception as e:
        print(f"Ошибка при проверке обновлений: {e}")

check_for_updates()

app = Flask(__name__, template_folder='web')
eel.init('web')

@app.route('/')
def index():
    return render_template('index.html')

@eel.expose
def get_data_from_python():
    return "Привет из Python!"

if __name__ == '__main__':
    eel.start('index.html', size=(300, 500), mode='chrome', position=(300, 300))
