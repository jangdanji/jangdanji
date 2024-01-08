
const checkBtn = document.querySelector('.input-word .input-btn')

checkBtn.addEventListener('click', function(){

  let word = document.querySelector('.input-word .your-words').value
      word = word.trim()
      console.log(word)

  /* 입력한 텍스트 유효성 검사 */

  const wordCheck = document.querySelector('.data-check p')

  if (word == '') wordCheck.textContent = '단어를 입력해 주세요.'
  else if (/[a-zA-Z]/.test(word)) wordCheck.textContent = '영어없이 한글 문자열로 구성해 주세요.'
  else if (/[0-9]/.test(word)) wordCheck.textContent = '숫자를 제외한 한글 문자열로 구성해 주세요.'
  else if (/[ㄱ-ㅎㅏ-ㅣ]/.test(word)) wordCheck.textContent = '올바른 한글 문자열로 구성해 주세요.'
  else {
    wordCheck.textContent = ''


  }


})

// const { normalize } = require("hangul-util");

// console.log(
//   normalize("별다를 것 없이 늙어간다")
// )