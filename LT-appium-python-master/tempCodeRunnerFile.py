 btn3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.handycloset.android.jpegpng:id/loadButton")))
        btn3.click()