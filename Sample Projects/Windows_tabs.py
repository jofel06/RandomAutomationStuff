from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')

browser.execute_script('window.open("https://techstepacademy.com/training-ground","_blank");')
browser.execute_script('window.open("https://techstepacademy.com/training-ground","_blank");')





#In terminal
#browser.window_handles         --------- to show how many windows currently
#len(browser.window_handles)         ------- how many windows open (int)
#handles = browser.window_handles    ----- assign to variable handles
#browser.switch_to.window(handles[0])     -------- to open and highlight it ([0] index)
