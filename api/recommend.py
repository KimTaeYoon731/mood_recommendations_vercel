# api/recommend.py
from flask import Flask, request, jsonify
import openai, os

# 1) WSGI 앱 생성
app = Flask(__name__)

# 2) POST 엔드포인트 정의
@app.route("/get_recommendations", methods=["POST"])
def get_recommendations():
    data = request.get_json(force=True) or {}
    mood = data.get("mood", "").strip()
    if not mood:
        return jsonify({"error": "감정이 입력되지 않았습니다."}), 400

    # 3) OpenAI 호출
    openai.api_key = os.environ["OPENAI_API_KEY"]
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 감정에 따라 영화와 음악을 추천해주는 전문가입니다."},
            {"role": "user", "content": f"지금 기분이 {mood}일 때 어울리는 영화 3개와 노래 3개를 추천해주세요."}
        ]
    )

    result = resp.choices[0].message["content"]
    return result, 200, {"Content-Type": "text/plain"}
