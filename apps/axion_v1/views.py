from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import requests, json, os

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def index(request):
    return render(request, "axion_v1.html")

@csrf_exempt
def chat(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        prompt = data.get("prompt", "").strip()
        if not prompt:
            return HttpResponse(json.dumps({"response": "⚠️ Prompt kosong."}),
                                content_type="application/json; charset=utf-8")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_KEY}",
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "Kamu adalah Axion v1, AI pembimbing coding MNK Digital."},
                {"role": "user", "content": prompt},
            ],
        }

        res = requests.post("https://api.openai.com/v1/chat/completions",
                            headers=headers, json=payload)
        if res.status_code != 200:
            return HttpResponse(json.dumps(
                {"response": f"⚠️ OpenAI Error {res.status_code}: {res.text[:100]}"}),
                content_type="application/json; charset=utf-8")

        data = res.json()
        reply = data["choices"][0]["message"]["content"]

        # kirim mentah, tanpa escape tambahan
        return HttpResponse(
            json.dumps({"response": reply}, ensure_ascii=False),
            content_type="application/json; charset=utf-8"
        )

    except Exception as e:
        return HttpResponse(
            json.dumps({"response": f"⚠️ Server error: {str(e)}"}),
            content_type="application/json; charset=utf-8"
        )
