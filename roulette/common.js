const fullModal = document.querySelector('.full-modal')

const modifyBtn = document.querySelector('.btn-zone .custom')
modifyBtn.addEventListener('click', () => fullModal.style.zIndex = 1)

const save = fullModal.querySelector('button.save')
save.addEventListener('click', () => {
  const missionData = fullModal.querySelector('.mission-list textarea')
  let cleanedData = missionData.value.replace(/\n{2,}/g, '\n')
      cleanedData = cleanedData.trimEnd()
  missionData.value = cleanedData
  fullModal.style.zIndex = -1
})