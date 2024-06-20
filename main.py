import core.drivers.driver_instance as driver_instance
from core.element_type.input_textbox import InputTextBox
from core.element_type.textbox import TextBox

def main():
    driver_instance.DRIVER = driver_instance.get_new_default_chrome_driver()

    #EXAMPLE CODE(IF NEEDED, SURROUND WITH TRY CATCH)
    import time
    item = "Distance to the Mars"
    timeout_amount = 10
    URL = "https://www.bing.com/"

    driver_instance.DRIVER.get(URL)
    time.sleep(2)   #Added delay to help visualize the framework in action

    search_box = InputTextBox(xpath="//input[@id=\"sb_form_q\"]", timeout=timeout_amount)
    search_box.search(item)
    time.sleep(2)   #Added delay to help visualize the framework in action

    result_box = TextBox(xpath="//div[@id=\"d_ans\"]/div/div[1]/div/div[1]", timeout=timeout_amount)
    result = result_box.get_text()

    driver_instance.DRIVER.execute_script("document.evaluate('//div[@id=\"d_ans\"]/div/div[1]/div/div[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.style.borderColor = 'red';")
    driver_instance.DRIVER.execute_script("document.evaluate('//div[@id=\"d_ans\"]/div/div[1]/div/div[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.style.borderStyle = 'solid';")
    driver_instance.DRIVER.execute_script("document.evaluate('//div[@id=\"d_ans\"]/div/div[1]/div/div[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.style.borderWidth = '30px';")
    
    time.sleep(3) #Added delay to help visualize the framework in action
    print(result)

    driver_instance.DRIVER.quit()
    driver_instance.DRIVER = None
    
if __name__ == '__main__':
    main()