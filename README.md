# KDT-NLPproject
노래 가사와 소리를 통한 노래 장르 유추하기

# 프로젝트 기간 
2024/04/03~2024/04/05

# 역할분담
**1. 자연어 처리**         

 - 임소영 : RNN 모델을 활용한 가사로 장르 분류하기 
 - 이화은 : LSTM 모델을 활용한 가사로 장르 분류하기 
    
 
**2. 주파수 분석**
- 손예림 : RandomForest 모델을 활용하여 주파수로 장르 분류하기 
- 이윤서 : CNN과 LSTM을 활용하여 주파수로 장르 분류하기 

# 세부 내용 (이름 클릭 시 상세내용 확인 가능)
<details>
<summary> 임소영 <a href="https://github.com/YimSoYoung1001" height="5" width="10" target="_blank">
	<img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"/><a> : RNN 모델을 활용한 가사로 장르 분류하기  / ppt 04p~20p </summary>
<div markdown="1">
- 크롤링을 사용하여 멜론 웹사이트에서 노래 관련 정보 수집하였습니다.
- 수집된 정보를 전처리 실시하였습니다.

   (노이즈 데이터 제거, 토큰화, 불용어 제거, 단어 사전 생성, 인코딩 및 패딩 시행)
- RNN 모델 및 함수 구성하였습니다.       

   | 기능           | 사용        |
   |--------------|-----------|
   | CrossEntropy | Adam      |
   | 손실함수      | optimizer |
   |모델 |RNN|
   |임베딩|Embedding|

- 학습 진행 후 성능평가 실시했습니다.        

   | 성능 평가 요소  | 결과    |
   |-----------|-------|
   | Loss      | 2.09  |
   | Accuracy  | 0.76  |
   | Precision | 0.11  |
   | Recall    | 0.142 |
   | F1_Score  | 0.125 |
</div>
</details>
<!--❤️여기서부터 화은언니❤️-->
<details>
<summary> 이화은 <a href="https://github.com/Skylee0310" height="5" width="10" target="_blank">
	<img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"/><a> : LSTM 모델을 활용한 가사로 장르 분류하기 / ppt 21p~45p </summary>
<div markdown="1">
 

### 📝 주제 -

✏ **주제 선정 배경**

- 멜로디와 가사의 분위기가 다른 경우가 많다.
    
    예 ) 멜로디는 신나지만 가사에는 슬픈 내용이 담긴 경우.
    
- 과연 가사와 멜로디만으로 장르를 분류할 수 있을까?

| 📄 개인 주제 | Kkma와 LSTM을 활용한 K-POP 노래 가사 장르 분류 |
| --- | --- |
| 🙍🏻‍♂️ 팀원 | 손예림, 이윤서, 이화은, 임소영 |
| 📊 PPT | https://buly.kr/58QEINW |

✏ **개인** **주제 선정 배경**

- '수업시간에 주로 다루었던 Okt와 RNN 모델이 아닌 Kkma와 LSTM 모델을 사용하면 어떤 성능 차이가 있을 것인가?'에 대한 의문으로 모델을 선택.
- Kkma의 특성 상 어근과 어미, 조사 등으로 분류되어 어근만 분리 되어 정확도를 올릴 수 있을 것으로 예상하였음
    
    ⇒ 어미와 조사를 직접 삭제해야 해야 했음.

 1) 데이터 준비 : 크롤링 후 Dateframe으로 불러오기
 2) 전처리
	- 불용어 처리(1) \n 삭제, 영어, 한글 제외 문제 삭제, 영어 소문자로 통일
 	- 토큰화
  	- 불용어 처리(2) : 영어 불용어 삭제
  	- 불용어 처리(3) - 한국어 불용어 삭제 어말어미 정리 (하드코딩으로 stopword 추가 삭제)
  	- 불용어 처리(4) - 영어 불용어 아포스토로피 삭제.
  	- 인코딩
  	- 패딩
  	- 라벨 인코딩
  	- 파일 저장.
  3) 모델 학습 :
  	  - 파일 불러오기
  	  - 피처 라벨 분리
  	  - 데이터 분리
  	  - 텐서 변환
  	  - 데이터셋 - 데이터 로더 생성
  	  - LSTM 모델 클래스 생성
  	  - 학습
  	  - 성능평가(정확도 0.13으로 저조)
  	 
  4) 예측
     	  - 가사를 넣으면 장르 예측

  ✏ **예측 실패 원인 분석 :**

- 다중 분류를 하기에는 자료 양이 적었음.
- 그 결과 정확도가 낮아졌고 입력 시 장르가 계속 변경 됨.

</div>
</details>



<!--❤️여기서부터 이윤서❤️-->
<details>
<summary> 이윤서 <a href="https://github.com/voo0o08" height="5" width="10" target="_blank">
	<img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"/><a> : CNN과 LSTM을 활용하여 주파수로 장르 분류하기 / ppt 46p~61p </summary>
<div markdown="1">
발라드곡과 댄스곡을 30초 단위로 편집하여 장르 분석

## ✏️음성 데이터의 특징

- 주파수 domain에서는 시간적 특성을 볼 수 없음
    
![image](https://github.com/voo0o08/KDT5_NLP_PROJECT/assets/155411941/bf999f9b-6545-4059-bc3d-e8c6094a2ec9)

    
- 진동수가 작으면 저음
- wav 파일이란?
    - 소리를 일정한 시간 간격마다 기록한 **실수배열 → 디지털**

| 이미지 | 오디오 |
| --- | --- |
| RGB 픽셀의 값  | 소리의 세기 |
| 해상도 | sampling rate (1초당 샘플의 개수, 1초당 Hz) → X축 해상도<br>bit depth → y축 해상도 <br>일반적인 음원 샘플링 속도 : 44,100 Hz /48,000 Hz<br>일반적인 음성인식 작업 : 16,000 Hz / 8,000 Hz|<br>

→ 용량을 생각하여 16,000 Hz로 샘플링

---

![image](https://github.com/voo0o08/KDT5_NLP_PROJECT/assets/155411941/20019441-c79e-4878-8687-565ae1ab4c5d)


x축을 시간으로 두고 y축을 소리의 크기로 두었을 때 베이스, 드럼이 많이 들어가는 댄스곡이 소리가 튀는 부분이 많은 것을 확인할 수 있음

→ 주파수 영역과 시간 영역을 모두 고려하기 위해 spectrogram 사용 

## ✏️spectrogram이란?

- 시간에 따라 변하는 신호의 주파수 영역에서 **시각적**으로 표현한 것
- x = 시간, y = 주파수, z = 진폭

![image](https://github.com/voo0o08/KDT5_NLP_PROJECT/assets/155411941/f9ce96ad-8bcb-4d87-b5b7-88bbe2595b12)


## ✏️CNN

### 1. 데이터 불러오기

음원 샘플 SR -> 44,100Hz / 일반 음성 작업 -> 16,000Hz

```python
# sr = 1초당 몇개의 데이터를 샘플링을 할지 
y, sr = librosa.load(path+"/"+file_name, sr=16000)
```

### 2. mfcc 피쳐 뽑기

n_ffcc -> 추출할 MFCC 계수의 수
n_fft -> 푸리에 변환할 윈도우 크기
hop_length -> 두 윈도우 사이의 샘플링 간격

```python
n_fft = 2048 # window의 크기
hop_length = 512  # window간 겹치는 부분 일반적으로 n_fft / 4

mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20, n_fft=n_fft, hop_length=hop_length) # sr 주의!!! 
```

### 3. 이미지로 저장

![image](https://github.com/voo0o08/KDT5_NLP_PROJECT/assets/155411941/9a9733cf-ac50-4839-8da4-a17a7eab35e6)


```python
 librosa.display.specshow(mfcc, sr=16000, hop_length=hop_length) # vmin=min_value, vmax=max_value
  plt.savefig(save_path, pad_inches = 0, bbox_inches = 'tight')
```

### 4. 학습

80개 이미지 -> train
10개 이미지 -> Test
10개 이미지 -> 예측용으로 빼두기

![image](https://github.com/voo0o08/KDT5_NLP_PROJECT/assets/155411941/87ffd3d2-fc16-4f31-a8b8-30f21f02441a)
![image](https://github.com/voo0o08/KDT5_NLP_PROJECT/assets/155411941/1c573bc1-a9c6-436a-a826-a091c2e11fcb)


### 5. 새로운 데이터 예측 결과

발라드 10개 -> 10개 정답

댄스곡 10개 -> 10개 정답

---

## ✏️LSTM

이지의 x축이 시간 timestamp니까 LSTM으로도 학습이 가능하지 않을까?

### 데이터 전처리

```python
# 전처리를 위한 변환
preprocessing = transforms.Compose([
    transforms.Resize((100, 100)),  # 이미지 크기 조정
    transforms.Grayscale(),  # 이미지를 흑백으로 변환
    transforms.ToTensor(),  # 텐서로 변환
])
```

LSTM이 4차원은 못받아서 Grayscale로 변환
문장과는 달리 이미지는 사이즈가 모두 같기때문에 패딩과정 불필요

### 결과

score → 0.5

- LSTM을 하기엔 feature의 수가 적음

---

## ✏️결론

- 음성 데이터도 이미지로 표현이 가능함
- RNN은 글만, CNN은 사진만 들어가는 것이 아님

</div>
</details>

<!--❤️여기서부터 예림언니❤️-->
<details>
<summary> 손예림 <a href="https://github.com/	osllzd" height="5" width="10" target="_blank">
	<img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"/><a> : RandomForest 모델을 활용하여 주파수로 장르 분류하기 / ppt 62p~77p </summary>
<div markdown="1">
내용추가해주세요
</div>
</details>



