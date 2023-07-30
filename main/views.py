from django.shortcuts import render
import requests

def index(request):
    # 만약 request.method가 POST라면
    if request.method == 'POST':
        # request.POST에 담긴 name="answer"에 input 데이터를 추출하여 변수에 할당
        answer = request.POST.get('answer')
        print(answer)

        # input으로 '지구는 왜 파란가요?'라고 입력하고 submit으로 제출하여 post에 answer로 들어온 상태이고, 이 answer는 아래 user에 content항목으로 들어갑니다. 그리고 그렇게 만들어진 리스트를 다시 answer로 다시 할당합니다.
        # 만약 DB에 저장할 것이라면 이 부분에서 저장을 하셔야 합니다. 
        answer = [
            {"role": "system", "content": "assistant는 시인이다."},
            {"role": "user", "content": answer},
        ]
        # https://estsoft-openai-api.jejucodingcamp.workers.dev/로 request를 post로 보내 응답을 받습니다.
        # 1차 과제에서 진행했던 request, response항목과 같으며 1차 과제 명세에서 자세한 내용은 확인바랍니다.
        response = requests.post('https://estsoft-openai-api.jejucodingcamp.workers.dev/', json=answer)
        # response에 담긴 json을 추출하여 출력합니다. 서비스를 만들 때에는 이렇게 출력되는 것들은 주석처리 해주세요.
        print(response)
        print(response.json())
        answer = response.json()['choices'][0]['message']['content']
        print(answer)
        
        # 변수 answer를 html에 보여줍니다.
        return render(request, 'main/index.html', {'text': answer})
    
    # 만약 request.method가 GET이라면
    else:
        # html을 보여줍니다.
        return render(request, 'main/index.html')
