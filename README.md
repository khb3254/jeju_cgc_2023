# 🍊JEJU🥕
- 제주도 특산물 가격 예측 Ai

  
- 💻사이트 주소 : https://jeju.pythonanywhere.com/welcome


- ✨Period : 2023.10.30 ~ 2023.11.29


- 🌴Developer
  - 강나영
  - 오영환
  - 안병선
  - 유정민


## 🏆수상
<div>
  <p>2023년 KIT 해커톤 제 1회 SW 및 Ai융합 공모전 장려상 수상</p>
  <img src="공모전 수상내역.png" width = "300">
</div> 
</br>


## ⚒️ Tools 
<p>
<img src="https://img.shields.io/badge/PyCham-forestgreen?style=plastic&logo=PyCham&logoColor=000000"/>
<img src="https://img.shields.io/badge/Jupyter Notebook-orangered?style=plastic&logo=Jupyter&logoColor=F37626"/>
<img src="https://img.shields.io/badge/Tableau Public-royalblue?style=plastic&logo=Tableau&logoColor=E97627"/>
<img src="https://img.shields.io/badge/GitHub-rebeccapurple?style=plastic&logo=GitHub&logoColor=181717"/>
</p>
  

<div style="display : flex; align-items : center;">
  <img src="도매가 가격 달력 이미지.png" alt = "도매가 가격 달력" width = "500" style = "margin-right: 40px;">
  <img src="특산품 예상 금액 이미지.png" width = "500">
</div>



## 📖 Description
- 2019년 1월 1일 ~ 2023년 3월 3일의 감귤, 브로콜리, 무, 당근, 양배추 유통가격에 대해 LSTM, Random Forest모델을 사용하여 2023년 11월 ~ 12월 가격 예측


## 프로젝트 목표
- 특산물들의 안정적이고 효율적인 수급을 위해서 해당 특산물들의 가격에 대한 정확한 예측이 필요


## 서비스 활용방안 및 기대효과
- 특산물 시장의 효율성을 증진시키고 소비자 만족도를 높일 수 있다.
- 제품의 생산 비용이나 운송 비용이 고정되어 있으면, 이로 인해 가격이 안정될 수 있다.
- 소비자는 합리적인 미래 선물 가격을 통해 미래 소비에 대한 예산 계획을 세울 수 있다.


## 시행착오
- 매일의 가격을 예상할 때 한달씩 값이 유지되는 컬럼들이 긍정적인 영향을 미치지 못한다고 판단
- 감귝의 대체제인 오렌지가 감귤의 가격에 영향을 주고 있을 것이라고 예상하여 오렌지의 무역 관련 데이터를 학습에 포함하였을 때 긍정적인 영향을 줄지 고민함
- 예를 들어서 종속변수인 price(kg당)에 맞춰서 생성한 '오렌지의 수입금액/수입중량', '감귤의 수출금액/수출중량'컬럼의 특성 중요도가 낮지 않았음에도 한 달 단위로 측정된 값이기 때문에 매일의 가격을 예측해야하는 모델에 긍정적인 영향을 미치지 못했다고 판다
