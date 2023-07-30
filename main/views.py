from django.shortcuts import render
import requests

def index(request):
    # 만약 request.method가 POST라면
    if request.method == 'POST':
        # request.POST에 담긴 name="answer"에 input 데이터를 추출하여
        # 변수에 할당
        answer = request.POST.get('answer')
        print(answer)

        # https://estsoft-openai-api.jejucodingcamp.workers.dev/로 request를 post로 보내 응답을 받는다.
        # 들어온 post: 지구는 왜 파란가요?
        answer = [
            {"role": "system", "content": "assistant는 시인이다."},
            {"role": "user", "content": answer},
        ]
        response = requests.post('https://estsoft-openai-api.jejucodingcamp.workers.dev/', json=answer)
        # response에 담긴 json을 추출하여 출력
        print(response)
        print(response.json())
        answer = response.json()['choices'][0]['message']['content']
        print(answer)
        
        # 변수 answer를 html에 보여준다.
        return render(request, 'main/index.html', {'text': answer})
    
    # 만약 request.method가 GET이라면
    else:
        # html을 보여준다.
        return render(request, 'main/index.html')
