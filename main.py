from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаем запросы с Flutter (localhost и пр.)

ASSETS_DIR = "assets"

@app.route('/assets/<path:filename>')
def serve_asset(filename):
    return send_from_directory(ASSETS_DIR, filename)

@app.route('/habits')
def get_habits():
    habits = [
        "Выпей стакан воды",
        "Сделай 10 отжиманий",
        "Пройди 1000 шагов",
        "Прочитай 5 страниц книги",
        "Выключи уведомления на час",
        "Не смотри в экран 10 минут",
        "Напиши благодарность за день"
    ]
    return jsonify(habits)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
