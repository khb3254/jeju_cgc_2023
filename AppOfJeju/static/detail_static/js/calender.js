const resvTab = document.querySelector('.resv-wrapper');
const exitBtn = document.querySelector('.resv-close');
exitBtn.addEventListener('click', ()=>{resvTab.classList.remove('open');});


// 날짜별로 이벤트 등록용 함수 및 변수
const selDate = []
const dateFunc = ()=>{
    const year = document.querySelector('.year');
    const month = document.querySelector('.month');
    const dates = document.querySelectorAll('.date');
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
//        i.removeEventListener('click', dateClickHandler); // 기존 이벤트 리스터 제거
//        i.addEventListener('click', dateClickHandler); // 새 이벤트 리스터 추가
    });
};

function dateClickHandler(event) {
    // 'closest' 함수를 사용하여 클릭된 요소의 상위에 있는 '.date' 클래스 요소를 찾습니다.
    let dateElement = event.target.closest('.date');

    // 클릭된 요소가 .date 클래스를 가진 요소가 아니면 함수를 종료합니다.
    if (!dateElement) {
        console.error("Clicked element does not have a .date class.");
        return;
    }

    // 선택된 날짜 데이터가 있는지 확인합니다.
    // let selectedDate = dateElement.dataset.date;
    let selectedDate = (dateElement.textContent).trim();
    if (!selectedDate) {
        console.error(dateElement);
        console.error("The selected date is undefined or does not have a data-date attribute.");
    }
    // AJAX 요청을 생성하고 설정하기
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/get-data/?date=' + selectedDate, true);
    xhr.onload = function() {
        if (this.status === 200) {
            // 서버로부터 반환된 데이터로 UI 업데이트
            document.querySelector('#datatablesSimple tbody').innerHTML = this.responseText;
        } else {
            // 에러 처리
            console.error('An error occurred during your request: ' + this.status + ' ' + this.statusText);
            return;
        }
    };
    xhr.onerror = function() {
        // 요청 자체에 문제가 있을 경우의 에러 처리
        console.error('The request failed');
    };
    // 요청 보내기
    xhr.send();
};

// 초기화 함수
const reset = ()=>{
    selDate.length=0;
    dateFunc(); // dateFunc 함수를 호출하여 이벤트 리스너를 추가합니다.
};

// 로드시 Nav 버튼들 이벤트 등록 및 초기화
window.onload=()=>{
    const navBtn = document.querySelectorAll('.nav-btn');
    navBtn.forEach(inf=>{
        if(inf.classList.contains('go-prev')){
            inf.addEventListener('click', ()=>{prevMonth(); reset();});
        }else if(inf.classList.contains('go-today')){
            inf.addEventListener('click', ()=>{goToday(); reset();});
        }else if(inf.classList.contains('go-next')){
            inf.addEventListener('click', ()=>{nextMonth(); reset();});
        }
    });
    reset();
};