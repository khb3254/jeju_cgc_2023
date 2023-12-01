// 원본 코드
const resvTab = document.querySelector('.resv-wrapper');
const exitBtn = document.querySelector('.resv-close');
exitBtn.addEventListener('click', ()=>{resvTab.classList.remove('open');});



// 서버에 GET 요청을 보내는 함수
// 특정 날짜, 농산물 품목이 무엇인지 전달
function sendGetRequestWithDate(date, type) {
    fetch(`${type}/?date=${date}`)
        .then(response => response.json())
        .then(data => {
             // 서버로부터 받은 데이터를 처리합니다.
            updatePageWithData(data); // HTML을 업데이트하는 함수
        })
        .catch(error => console.error('Error:', error));
}


// 페이지를 업데이트하는 함수
function updatePageWithData(data) {

    const companyNames = {
        'A': '행복농원',
        'B': '예린농산',
        'C': '다솜농장',
        'D': '하늘농원',
        'E': '미래농산',
        'F': '땅과바다',
        '': '시장가격'
    };

    // 업데이트할 테이블 또는 페이지 부분을 찾습니다
    const tableBody = document.querySelector('.datatable-table tbody');
    tableBody.style.visibility = 'visible';

    tableBody.innerHTML = ''; // 기존 테이블 데이터를 지웁니다

    // 데이터를 반복하면서 테이블 바디에 행을 추가합니다
    data.forEach(item => {
        const companyName = companyNames[item.supplier] || '시장가격';
        const formattedPrice = item.crop_price.toLocaleString();
        const row = `<tr>
                        <td>${companyName}</td>
                        <td>${formattedPrice}원</td>
                        <td>${item.crop_date}</td>
                     </tr>`;
        tableBody.innerHTML += row;
    });
}




// 원본 코드
// 날짜별로 이벤트 등록용 함수 및 변수
const selDate = []
const dateFunc = ()=>{
    var year = document.querySelector('.year');
    var month = document.querySelector('.month');
    var dates = document.querySelectorAll('.date');
    dates.forEach((i)=>{
        i.addEventListener('click', ()=>{
            if(i.classList.contains('other') || i.classList.contains('selected')){
                dates.forEach((ig)=>{ig.classList.remove('selected');});
                i.classList.remove('selected');
                selDate.length=0;
            }else if(selDate.length > 0){
                dates.forEach((ig)=>{ig.classList.remove('selected');});
                selDate.length=0;
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                resvTab.classList.add('open');
            }else{
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                resvTab.classList.add('open');
            }
        })
    });
};


// 원본 코드
// 초기화 함수
const reset = ()=>{
    selDate.length=0;
    dateFunc(); // dateFunc 함수를 호출하여 이벤트 리스너를 추가합니다.
};


document.addEventListener('DOMContentLoaded', function () {
    // 모든 초기화 코드를 여기에 넣으세요
    // 예를 들면, 이벤트 리스너를 추가하는 함수 등


        // 새 코드
        // 날짜 요소에 이벤트 리스너를 추가하는 함수
        function addEventListenersToDateElements() {
            document.querySelectorAll('.date, .date-itm').forEach(function(dateElement) {
                dateElement.addEventListener('click', function(event) {
                    // 선택된 날짜를 저장
                    var year = document.querySelector('.year').textContent;
                    var month = document.querySelector('.month').textContent;
                    var date = event.target.textContent.trim().slice(0, 2);
                    var type = window.location.pathname;

                    // 선택된 날짜를 특산품 예상 금액 섹션에 표시
                    document.getElementById('selected-date-span').textContent = `${year}년 ${month}월 ${date}일`;

                    // 월과 일이 한 자리 숫자일 경우 앞에 '0'을 추가합니다.
                    if (month.length === 1) {
                        month = '0' + month;
                    }
                    if (date.length === 1) {
                        date = '0' + date;
                    }
                    // YYYY-MM-DD 형식으로 날짜를 결합합니다.
                    var selectedDate = `${year}-${month.padStart(2, '0')}-${date.padStart(2, '0')}`;
                    // 서버에 GET 요청을 보내는 함수 호출
                    sendGetRequestWithDate(selectedDate, type);
                });
            });
        }


    reset();
    addEventListenersToDateElements();

    // MutationObserver를 설정하는 코드도 여기에 포함될 수 있습니다.
    // DOM 변화를 관찰하는 MutationObserver 초기화
    var observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList') {
                // 달력의 DOM에 변화가 감지될 때마다 이벤트 리스너를 다시 추가
                addEventListenersToDateElements();
            }
        });
    });

    // 관찰 대상 요소 및 관찰 설정
    var targetNode = document.querySelector('.calendar'); // 달력 요소의 부모 요소를 지정
    var config = { childList: true, subtree: true };

    // 관찰 시작
    observer.observe(targetNode, config);

    // 다른 모든 함수들도 이 안에서 호출할 수 있습니다.
    // 예를 들어, 나비게이션 버튼 이벤트를 등록하는 코드 등
    const navBtn = document.querySelectorAll('.nav-btn');
    navBtn.forEach(inf => {
        if (inf.classList.contains('go-prev')) {
            inf.addEventListener('click', () => { prevMonth(); reset(); });
        } else if (inf.classList.contains('go-today')) {
            inf.addEventListener('click', () => { goToday(); reset(); });
        } else if (inf.classList.contains('go-next')) {
            inf.addEventListener('click', () => { nextMonth(); reset(); });
        }
    });
});