const _ = require('lodash');

const mission = [
  '디바 4인궁 이상 성공하기',
  '겐지 용검 4검 이상 성공하기',
  '정크랫 똥에 10번 맞아죽기',
  '메르시로 딜금먹기',
  '마이크쓰는 친구 만들어오기',
  '송하나 메카탑승에 깔려 죽기',

]

let shuffled = _.shuffle(mission)

const spinBtn = document.querySelector('.btn-zone button.spin')
const resultWindow = document.querySelector('.roulette p.result')

function count(endpoint, index=0, delay=20) {

  let result

  if (index < endpoint) {

    setTimeout(() => {

      result = shuffled[index % shuffled.length]
      resultWindow.textContent = result

      count(endpoint, index + 1, index < endpoint - 30 ? 20 : delay + 16) /* index가 70 이상 넘어가면 delay가 10씩 누적으로 증가 */
    }, delay)
  } 
  else if (index > endpoint) {
    setTimeout(() => {
      if (Math.random() < 0.5) {
        result = shuffled[index % shuffled.length]
        resultWindow.textContent = result
        resultWindow.style.cssText = `
          background-color : #FAE392; font-size: 34px;
        `
      }
      else {
        result = shuffled[(index-1) % shuffled.length]
        resultWindow.textContent = result
        resultWindow.style.cssText = `
        background-color : #FAE392; font-size: 34px;
      `
      }
    }, 1000)
  }
}

spinBtn.addEventListener('click', function(){

  resultWindow.style.backgroundColor = 'white'
  count(shuffled.length + 100 + Math.random() * 200) /* 0 ~ 배열length 중에 랜덤한 값 */
})



// console.log(Math.random() * 2)

