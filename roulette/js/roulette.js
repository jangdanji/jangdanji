const _ = require('lodash');

const yourMission = document.querySelector('.full-modal .custom .mission-list textarea')
yourMission.value = `디바 4인궁 이상 성공하기
겐지 용검 4검 이상 성공하기
정크랫 똥에 10번 맞아죽기
메르시로 딜금먹기
마이크쓰는 친구 만들어오기
송하나 메카탑승에 깔려 죽기`

const spinBtn = document.querySelector('.btn-zone button.spin')
const resultWindow = document.querySelector('.roulette p.result')

function count(shuffledList, endpoint, index=0, delay=20) {

  let result

  console.log(endpoint)

  if (index < endpoint) {

    setTimeout(() => {

      result = shuffledList[index % shuffledList.length]
      resultWindow.textContent = result

      count(shuffledList, endpoint, index + 1, index < endpoint - 30 ? 20 : delay + 16) /* index가 70 이상 넘어가면 delay가 10씩 누적으로 증가 */
    }, delay)
  } 
  else if (index > endpoint) {
    setTimeout(() => {
      if (Math.random() < 0.5) result = shuffledList[index % shuffledList.length]
      else result = shuffledList[(index-1) % shuffledList.length]

      resultWindow.textContent = result
      resultWindow.style.cssText = `background-color : #FAE392; font-size: 34px;`
      const btnZone = document.querySelector('.roulette .btn-zone')
      btnZone.style.display = 'flex'
    }, 1500)
  }
}


spinBtn.addEventListener('click', function(){

  const btnZone = document.querySelector('.roulette .btn-zone')
  btnZone.style.display = 'none'

  let missions = document.querySelector('.full-modal .custom textarea').value
  let shuffledList = _.shuffle(missions.split('\n'))

  resultWindow.style.backgroundColor = 'white'
  const end = shuffledList.length + 100 + Math.random() * 200
  count(shuffledList, endpoint=end) /* 0 ~ 배열length 중에 랜덤한 값 */
})


