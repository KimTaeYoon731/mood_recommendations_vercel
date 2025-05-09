import openai
import os

def handler(request):
    openai.api_key = os.environ["OPENAI_API_KEY"]

    try:
        data = request.json()
        mood = data.get("mood")

        if not mood:
            return {
                "statusCode": 400,
                "body": "감정이 입력되지 않았습니다."
            }

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 감정에 따라 영화와 음악을 추천해주는 전문가입니다."},
                {"role": "user", "content": f"{mood}일 때 어울리는 영화 3개와 노래 3개 추천해줘."}
            ]
        )

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/plain"},
            "body": response.choices[0].message["content"]
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"오류 발생: {str(e)}"
        }
