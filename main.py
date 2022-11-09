import core.drivers.driver_instance as driver_instance


def main():
    driver_instance.DRIVER = driver_instance.get_new_default_chrome_driver()

    #ENTER CODE HERE

    driver_instance.DRIVER.quit()
    driver_instance.DRIVER = None
    
if __name__ == '__main__':
    main()