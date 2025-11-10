import streamlit as st

st.set_page_config(page_title="반응속도 테스트", layout="centered")
st.title("반응속도 테스트 🎯")
st.write("초록색이 되면 클릭하세요!")

# HTML + JS 코드 직접 삽입
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
    body { display:flex; flex-direction:column; align-items:center; justify-content:center;
           height:100vh; font-family:sans-serif; background:#333; color:white; text-align:center;}
    #box { width:300px; height:300px; background:red; margin:20px; cursor:pointer;
           display:flex; align-items:center; justify-content:center; font-size:24px; user-select:none;}
    #score { font-size:24px; }
</style>
</head>
<body>
<h1>반응속도 테스트</h1>
<p>초록색이 되면 클릭하세요!</p>
<div id="box">준비</div>
<div id="score">반응시간: -- ms</div>
<script>
let box = document.getElementById('box');
let scoreDisplay = document.getElementById('score');
let startTime, timeoutID, waiting = true;

function startTest() {
    box.style.backgroundColor = 'red';
    box.textContent = '기다리세요...';
    waiting = true;
    let delay = Math.random()*2000+1000;
    timeoutID = setTimeout(()=>{
        box.style.backgroundColor='green';
        box.textContent='클릭!';
        startTime = new Date().getTime();
        waiting=false;
    }, delay);
}

box.addEventListener('click', ()=>{
    if(waiting){
        clearTimeout(timeoutID);
        box.textContent='너무 빨랐어요! 다시 시도';
        setTimeout(startTest,1000);
    }else{
        let endTime = new Date().getTime();
        let reactionTime = endTime - startTime;
        scoreDisplay.textContent = '반응시간: ' + reactionTime + ' ms';
        startTest();
    }
});

startTest();
</script>
</body>
</html>
"""

# Streamlit에서 HTML 렌더링
st.components.v1.html(html_code, height=550)
