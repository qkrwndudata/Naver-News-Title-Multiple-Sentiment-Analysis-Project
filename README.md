## 주제: 뉴스 제목을 통한 다중 감성 분석 프로젝트

#### 🔍<주제 설명>
- 네이버 뉴스 제목과 공감을 크롤링 해 해당 기사가 독자에게 '좋은', ' 훈훈한', '슬픈', '화난', 후속 기사를 원하는' 내용일지 예측해 보는 프로젝트
![image](https://user-images.githubusercontent.com/79184083/219857438-b6a009ae-7533-4edc-b006-587b89620e1e.png)

#### 📚 <분석 과정>

1. 데이터 수집
- 다양한 분야의 뉴스 제목과 반응별 공감 수 크롤링 진행
- 각 기사 제목 별 독자들의 공감을 라벨링 이후 최종 데이터셋 생성

2. 데이터 전처리
- 정규표현식을 사용한 불용어 제거
- KONLP의 Okt를 사용한 토큰화
- 단어 리스트를 벡터화한 이후 패딩 진행

3. 모델링
- 불균형 문제 해결: SMOTE / class weight / focal loss 성능 비교
- 6가지 모델 비교: LSTM / KoBERT / ML(RF, SVM, NB, LR)

#### 💻<결과>

![image](https://user-images.githubusercontent.com/79184083/219857622-41145aa8-ea8b-4d8d-b8e3-7682bf646aef.png)

