#Import Packages
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 


class Test_Shopping_Website(unittest.TestCase):  

    def setUp(self):
        self.driver = webdriver.Edge()
        Url="https://www.saucedemo.com/" 
        self.driver.get(Url)  
        self.driver.maximize_window()

    def test_Login_Screen(self):

        #TS_Login_011
        Login_text_username=self.driver.find_element(By.CLASS_NAME,"login_credentials")
        Expected_username="Accepted usernames are:\nstandard_user\nlocked_out_user\nproblem_user\nperformance_glitch_user\nerror_user\nvisual_user"
        assert Expected_username==Login_text_username.text
        Login_text_password=self.driver.find_element(By.CLASS_NAME,"login_password")
        Expected_password="Password for all users:\nsecret_sauce"
        assert Login_text_password.text==Expected_password


        color_validation_section= self.driver.find_element(By.CLASS_NAME, 'login_credentials_wrap-inner') 
        background_color = color_validation_section.value_of_css_property("#132322")
        if "rgb(0, 0, 0)" in background_color:
            print("Login button has a black background color!")
        else:
            print("Login button does not have a black background color!")



        
        #TS_Login_001 & TS_Login_002
        Input_Box=self.driver.find_elements(By.CLASS_NAME,"form_input")
        placeholder_text = Input_Box[1] .get_attribute("placeholder")
        assert placeholder_text=="Password"
        Input_Box[1].send_keys("secret_sauce")  #Password

        placeholder_text = Input_Box[0].get_attribute("placeholder")
        assert placeholder_text=="Username"        
        Input_Box[0].send_keys("standard_user") #Username

        self.driver.find_element(By.CLASS_NAME,"btn_action").click()  #Submit Button
        self.driver.find_element(By.CLASS_NAME,"app_logo").is_displayed()
        hamberg=self.driver.find_element(By.ID,"react-burger-menu-btn").click() #Hamberg icon click
        time.sleep(1)
        logout=self.driver.find_elements(By.CLASS_NAME,"menu-item") #logout

        logout[2].click()
        

        #TS_Login_003
        Submit= self.driver.find_element(By.CLASS_NAME,"btn_action").click()
        Error_message= self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text
        assert Error_message=="Epic sadface: Username is required"
        Cross_Button= self.driver.find_element(By.CLASS_NAME,"error-button")
        Cross_Button.is_displayed()
        Cross_Button.click()


        #TS_Login_005
        Input_Box=self.driver.find_elements(By.CLASS_NAME,"form_input")
        Input_Box[1].send_keys("secret_sauce")
        submit=self.driver.find_element(By.CLASS_NAME,"btn_action") #Submit
        print(submit.is_displayed())
        submit.click()
        error_message_locator = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        expected_error_message = "Epic sadface: Username is required"
        error_message_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(error_message_locator))
        actual_error_message = error_message_element.text
        Input_Box[1].send_keys(Keys.BACK_SPACE * 12)


        #TS_Login_004
        Input_Box[1].send_keys("secret_sauce")
        submit=self.driver.find_element(By.CLASS_NAME,"btn_action")
        print(submit.is_displayed())
        submit.click()
        expected_error_message = "Epic sadface: Password is required"
        error_message_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(error_message_locator))
        actual_error_message = error_message_element.text
        Input_Box[0].send_keys(Keys.BACK_SPACE * 12)

        Input_Box[1].send_keys("zdvr11.dvsauce") 
        Input_Box[0].send_keys("standard_user")
        submit=self.driver.find_element(By.CLASS_NAME,"btn_action").click()
        error_message_path = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        assert error_message_path.text=="Epic sadface: Username and password do not match any user in this service"
        Input_Box[1].send_keys(Keys.BACK_SPACE * 12)

        Input_Box[1].send_keys("secret_sauce")
        Input_Box[0].send_keys("er33#rd_user")
        submit=self.driver.find_element(By.CLASS_NAME,"btn_action").click()
        assert error_message_path.text=="Epic sadface: Username and password do not match any user in this service"
        Cross_Button= self.driver.find_element(By.CLASS_NAME,"error-button")
        Cross_Button.click()
        try:
                error_message = self.driver.find_element(By.ID,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
                Cross_Button= self.driver.find_element(By.CLASS_NAME,"error-button")
                assert not error_message.is_displayed(), "Error message is still present after clicking the button"
                assert not Cross_Button.is_displayed()
        except NoSuchElementException:
                pass  
        


    def test_HomePage(self):   

        Login_TextBox = self.driver.find_elements(By.XPATH, '//*[@class="input_error form_input"]')
        Login_TextBox [0].send_keys("standard_user")
        Login_TextBox [1].send_keys("secret_sauce")

        login_button = self.driver.find_element(By.XPATH, '//*[@class="submit-button btn_action"]') 
        #  CSS value of the background-color property
        background_color = login_button.value_of_css_property("#3ddc91")
        if "rgb(19, 35, 34)" in background_color:
            print("Login button has a green background color!")
        else:
            print("Login button does not have a green background color!")

        
        #TS_Login_009
        submit=self.driver.find_element(By.XPATH, '//*[@class="submit-button btn_action"]').click()
        element = self.driver.find_element(By.XPATH,"//*[@class='app_logo']")
        actual_text = element.text
        expected_text = "Swag Labs"
        if actual_text == expected_text:
            print("Text validation passed. Actual text:", actual_text)
        else:
            print("Text validation failed. Actual text:", actual_text)


        text_element = self.driver.find_element(By.XPATH,"//*[@class='app_logo']")
        location = text_element.location
        expected_position = {"x": 575.2, "y": 48}  # Example expected position
        actual_position = location

        if actual_position == expected_position:
            print("Text is displayed in the proper position.")
        else:
            print("Text is not displayed in the proper position.")
        self.driver.execute_script("arguments[0].scrollIntoView();", text_element)



        Product_Name = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        assert Product_Name[0].text=="Sauce Labs Backpack"
        assert Product_Name[1].text=="Sauce Labs Bike Light"
        assert Product_Name[2].text=="Sauce Labs Bolt T-Shirt"
        assert Product_Name[3].text=="Sauce Labs Fleece Jacket"
        assert Product_Name[4].text=="Sauce Labs Onesie"
        assert Product_Name[5].text=="Test.allTheThings() T-Shirt (Red)"



        font_weight = Product_Name[0].value_of_css_property("font-weight")
        # Check if the font-weight is bold
        if font_weight == "bold" or font_weight >= "700":  # "bold" or numerical value >= 700 indicates bold
                print("The text is displayed in bold.")
        else:
                print("The text is not displayed in bold.")


        Product_Desc = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_desc')
        assert Product_Desc[0].text=="carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
        assert Product_Desc[1].text=="A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included."
        assert Product_Desc[2].text=="Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt."
        assert Product_Desc[3].text=="It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office."
        assert Product_Desc[4].text=="Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel."
        assert Product_Desc[5].text=="This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton."

        Product_Price = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
        assert Product_Price[0].text=="$29.99"
        assert Product_Price[1].text=="$9.99"
        assert Product_Price[2].text=="$15.99"
        assert Product_Price[3].text=="$49.99"
        assert Product_Price[4].text=="$7.99"
        assert Product_Price[5].text=="$15.99"


        image_element = self.driver.find_elements(By.CLASS_NAME,"inventory_item_img")
        #  src attribute value of the image
        actual_src_attribute_1 = image_element[1].get_attribute("alt")
        actual_src_attribute_2 = image_element[2].get_attribute("alt")
        actual_src_attribute_3 = image_element[3].get_attribute("alt")
        actual_src_attribute_4 = image_element[4].get_attribute("alt")
        actual_src_attribute_5 = image_element[5].get_attribute("alt")
        actual_src_attribute_6 = image_element[6].get_attribute("alt")
        # Expected src attribute value
        expected_src_attribute_1 = "Sauce Labs Backpack"
        expected_src_attribute_2 = "Sauce Labs Bike Light"
        expected_src_attribute_3 = "Sauce Labs Bolt T-Shirt"
        expected_src_attribute_4 = "Sauce Labs Fleece Jacket"
        expected_src_attribute_5 = "Sauce Labs Onesie"
        expected_src_attribute_6 = "Test.allTheThings() T-Shirt (Red)"

       
        if actual_src_attribute_1 == expected_src_attribute_1 and actual_src_attribute_2 == expected_src_attribute_2 and actual_src_attribute_3 == expected_src_attribute_3 and actual_src_attribute_4 == expected_src_attribute_4 and actual_src_attribute_5 == expected_src_attribute_5:
                print("Image src matches the expected value.")
        else:
                print("Image src does not match the expected value.")


         #Comparing if product description , rate, header text is same in home page and product details page, then comparing if "add to cart" add and remove clicks
        for n in range(0,6):

                product_click=self.driver.find_elements(By.CLASS_NAME,'inventory_item_img')
                product_click[n*2].click() # 0,2,4,6,8,10
                inventory_details_desc=self.driver.find_elements(By.CLASS_NAME,"large_size")
                inventory_details_desc_text= inventory_details_desc[1].text # 1     
                inventory_item_name=self.driver.find_elements(By.CLASS_NAME,"large_size") #large_size inventory_item_name
                inventory_item_name_text= inventory_item_name[0].text #0     
                inventory_details_price=self.driver.find_element(By.CLASS_NAME,"inventory_details_price").text
                count_of_items_in_Cart = self.driver.find_element(By.CLASS_NAME, 'btn_inventory')
                count_of_items_in_Cart.is_displayed()
                count_of_items_in_Cart.click()

                border_color_check= self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div[2]/button")  
                border_color = border_color_check.value_of_css_property("border")
                if border_color == "1px solid #e2231a;":
                        print("pass")
                else:
                      print("fail")

                count_of_items_in_Cart_After_click = self.driver.find_element(By.CLASS_NAME, 'btn_inventory')  
                #TS_Product_026a,TS_Cart_028
                if count_of_items_in_Cart_After_click.text == "Remove":
                        count =1   #1
                Actual_items_added_in_Cart = int(self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)
                assert count==Actual_items_added_in_Cart
                count_of_items_in_Cart_After_click.click()
                #TS_Cart_027
                add_btn=self.driver.find_element(By.CLASS_NAME, 'btn_inventory')
                assert add_btn.text=="Add to cart"
                #TS_Cart_029
                assert EC.invisibility_of_element_located((By.CLASS_NAME, 'btn_inventory'))

                Back_to_product_text=self.driver.find_element(By.CLASS_NAME,"inventory_details_back_button")  #TS_Product_036
                Back_to_product_text.is_displayed() 
                Back_to_product_text.click()
                Product_Desc = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_desc')
                Product_Desc_text=Product_Desc[n].text # 0,1,2,3,4,5
                Product_Name = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
                Product_Name_text=Product_Name[n].text #+1,
                Product_Price = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
                Product_Price_text=Product_Price[n].text #+1
                print(inventory_details_desc_text)
                print(Product_Desc_text)
                assert inventory_details_desc_text == Product_Desc_text
                assert inventory_item_name_text == Product_Name_text
                assert inventory_details_price== Product_Price_text


        #TS_Cart_031 - TS_Cart_035
        for i in range(0,6):
                AddToCart_btn = self.driver.find_elements(By.CLASS_NAME, 'btn_inventory')
                AddToCart_btn[i].is_displayed()
                AddToCart_btn[i].click()
                AddToCart_btn = self.driver.find_elements(By.CLASS_NAME, 'btn_inventory')  
                if AddToCart_btn[i].text == "Remove":
                    count =1
                Expected_AddToCart_btn = int(self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)
                assert count==Expected_AddToCart_btn
                AddToCart_btn[i].click()
                add_btn=self.driver.find_element(By.CLASS_NAME, 'btn_inventory')
                assert add_btn.text=="Add to cart"
                assert EC.invisibility_of_element_located((By.CLASS_NAME, 'btn_inventory'))
                    

        #TS_Cart_037, TS_Cart_038
        Filter=self.driver.find_element(By.CLASS_NAME,"product_sort_container")
        print(Filter.is_displayed())
        Drop_Down_Option=Filter.text
        Expected_text=("Name (A to Z)\nName (Z to A)\nPrice (low to high)\nPrice (high to low)")
        assert Drop_Down_Option==Expected_text
        Default_text=self.driver.find_element(By.CLASS_NAME,"active_option")
        Expected_Default_selection ="Name (A to Z)"
        assert Expected_Default_selection==Default_text.text


        products = self.driver.find_elements(By.CLASS_NAME,"inventory_item_name") 
        for sort in products:
                a=sort.text
                print(a)
        expected_order=("Sauce Labs Backpack\nSauce Labs Bike Light\nSauce Labs Bolt T-Shirt\nSauce Labs Fleece Jacket\nSauce Labs Onesie\nTest.allTheThings() T-Shirt (Red)")
        print(expected_order)



        for j in range(0,6):
                AddToCart_btn = self.driver.find_elements(By.CLASS_NAME, 'btn_inventory')
                AddToCart_btn[j].is_displayed()
                AddToCart_btn[j].click()


        #TS_Cart_044, TS_Cart_045
        cart=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        cart.is_displayed()
        cart.click()
        title_text=self.driver.find_element(By.CLASS_NAME,"title")
        title_text.is_displayed()
        assert title_text.text=="Your Cart"
        sub_text1=self.driver.find_element(By.CLASS_NAME,"cart_quantity_label")
        sub_text1.is_displayed()
        assert sub_text1.text=="QTY"
        sub_text2=self.driver.find_element(By.CLASS_NAME,"cart_desc_label")
        sub_text2.is_displayed()
        assert sub_text2.text=="Description"

        for k in range(0,6):
            cart_item=self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
            expected_order=("Sauce Labs Backpack\nSauce Labs Bike Light\nSauce Labs Bolt T-Shirt\nSauce Labs Fleece Jacket\nSauce Labs Onesie\nTest.allTheThings() T-Shirt (Red)")
            print(cart_item[k].text)

        Continue_shopping_btn=self.driver.find_element(By.CLASS_NAME,"btn_medium")
        Continue_shopping_btn.is_displayed()
        Image_in_continue_btn=self.driver.find_element(By.CLASS_NAME,"back-image")
        Image_in_continue_btn.is_displayed()
        assert Continue_shopping_btn.text=="Continue Shopping"
        Image_in_continue_btn.click()
        Home_page=self.driver.find_element(By.CLASS_NAME,"title").is_displayed()
        cart=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()



        #TS_Cart_048
        check_out_button=self.driver.find_element(By.CLASS_NAME,"checkout_button ")
        check_out_button.click()
        #TS_Checkout_050
        check_out_title_text=self.driver.find_element(By.CLASS_NAME,"title").is_displayed()
        #TS_Checkout_052,TS_Checkout_054 -TS_Checkout_057
        Check_out_details=self.driver.find_elements(By.CLASS_NAME,"form_input")
        Check_out_details[0].click()

        continue_button_click=self.driver.find_element(By.CLASS_NAME,"btn_action")
        continue_button_click.click()
        Error_message= self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3").text
        assert Error_message=="Error: First Name is required"
        Check_out_details[0].send_keys("#john1")

        continue_button_click.click()
        submit=self.driver.find_element(By.CLASS_NAME,"btn_action")
        Error_message= self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3").text
        assert Error_message=="Error: Last Name is required"
        Check_out_details[1].click()
        Check_out_details[1].send_keys("#ore1")

        continue_button_click.click()
        submit=self.driver.find_element(By.CLASS_NAME,"btn_action")
        Error_message= self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3").text
        assert Error_message=="Error: Postal Code is required"
        Check_out_details[2].click()
        Check_out_details[2].send_keys("#street10")



        #TS_Checkout_053
        placeholder_path_Fist_Name = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input")  
        placeholder_text = placeholder_path_Fist_Name.get_attribute("placeholder")
        assert placeholder_text=="First Name"

        placeholder_path_Last_Name  = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input")  
        placeholder_text = placeholder_path_Last_Name .get_attribute("placeholder")
        assert placeholder_text=="Last Name"

        placeholder_path_Last_Name  = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input")  
        placeholder_text = placeholder_path_Last_Name .get_attribute("placeholder")
        assert placeholder_text=="Zip/Postal Code"
        
        #TS_Checkout_059
        cancel_btn=self.driver.find_element(By.CLASS_NAME,"cart_cancel_link").click()
        your_cart_txt=self.driver.find_element(By.CLASS_NAME,"title").text
        assert your_cart_txt=="Your Cart"
        checkout_btn=self.driver.find_element(By.CLASS_NAME,"checkout_button").click()
        
        #TS_Checkout_060
        assert EC.invisibility_of_element_located((By.CLASS_NAME, Check_out_details[0]))
        assert EC.invisibility_of_element_located((By.CLASS_NAME, Check_out_details[1]))
        assert EC.invisibility_of_element_located((By.CLASS_NAME, Check_out_details[2]))


        #TS_Checkout_051,TS_Checkout_058
        continue_button_click=self.driver.find_element(By.CLASS_NAME,"btn_action").click()
        error_message=self.driver.find_element(By.CLASS_NAME,"error").is_displayed() 
        Cross_symbol=self.driver.find_elements(By.CLASS_NAME,"error_icon") 
        Cross_symbol1=Cross_symbol[0].is_displayed()
        Cross_symbol1=Cross_symbol[1].is_displayed()
        Cross_symbol1=Cross_symbol[2].is_displayed()
        cross_button=self.driver.find_element(By.CLASS_NAME,"error-button").click()
        WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "error")))
        WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "error_icon"))) 


        #TS_Checkout_063
        Check_out_details=self.driver.find_elements(By.CLASS_NAME,"form_input")
        Check_out_details[0].click()
        Check_out_details[0].send_keys("john")
        Check_out_details[1].click()
        Check_out_details[1].send_keys("ore1")
        Check_out_details[2].click()
        Check_out_details[2].send_keys("#10")
        continue_button_click=self.driver.find_element(By.CLASS_NAME,"btn_action").click()
        Checkout_text=self.driver.find_element(By.CLASS_NAME,"title")
        assert Checkout_text.text=="Checkout: Overview"
        Checkout_sub_tile1=self.driver.find_element(By.CLASS_NAME,"cart_quantity_label")
        assert Checkout_sub_tile1.text=="QTY"
        Checkout_sub_tile2=self.driver.find_element(By.CLASS_NAME,"cart_desc_label")
        assert Checkout_sub_tile2.text=="Description" 

        summary_info=self.driver.find_elements(By.CLASS_NAME,"summary_info_label")
        summary_info[0].is_displayed()
        assert summary_info[0].text=="Payment Information:"
        summary_value=self.driver.find_elements(By.CLASS_NAME,"summary_value_label")
        summary_value[0].is_displayed()
        assert summary_value[0].text=="SauceCard #31337" 

        summary_info[1].is_displayed()
        assert summary_info[1].text=="Shipping Information:"
        summary_value[1].is_displayed()
        assert summary_value[1].text=="Free Pony Express Delivery!"

       
        summary_info[2].is_displayed()
        assert summary_info[2].text=="Price Total"
        summary_subtotal=self.driver.find_element(By.CLASS_NAME,"summary_subtotal_label")
        summary_subtotal.is_displayed()
       
        tax=self.driver.find_element(By.CLASS_NAME,"summary_tax_label")
        tax.is_displayed()
       
        total=self.driver.find_element(By.CLASS_NAME,"summary_total_label")
        total.is_displayed()
       



        self.driver.back()
        self.driver.back()

        text1 = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        previouse_text= text1[0].text
        text1[0].click()
        text2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[1]"))) 
        new_text = text2.text
        if previouse_text == new_text:
                print("Text on the first screen matches the text on the new screen.")
        else:
                print("Text on the first screen does not match the text on the new screen.")
 
        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.driver.back()


        try:
                WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))
                WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))
                WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))
                WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))
                WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))
                WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))
                print("Text changed to 'Remove'. Validation successful!")
        except TimeoutException:
                print("Text did not change to 'Remove'. Validation failed.")


        product_btn=self.driver.find_elements(By.CLASS_NAME,"btn_inventory") 
        product_btn[0].click()
        product_btn[1].click()
        product_btn[2].click()
        product_btn[3].click()
        product_btn[4].click()
        product_btn[5].click()

        try:
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
            print("Text changed to 'Add to cart'. Validation successful!")
        except TimeoutException:
            print("Text did not change to 'Add to cart'. Validation failed.")

        item1 = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        item1[0].click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
        add=self.driver.find_element(By.CLASS_NAME, 'btn_inventory')
        add.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))

        #Verifing "Back to product" text in product details screen
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/button"), "Back to products"))
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/button").click()

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"title"), "Products"))
        item2 = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        item2[1].click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
        add=self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/button')
        add.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/button").click()

        item3 = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        item3[2].click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
        add=self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/button')
        add.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/button").click()
        
        item4 = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        item4[3].click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
        add=self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/button')
        add.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/button").click()   

        item5 = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        item5[4].click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
        add=self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/button')
        add.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))   
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/button").click()

        item6 = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        item6[5].click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Add to cart"))
        add=self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/button')
        add.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"btn_inventory "), "Remove"))      
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/button").click()  

        count_of_items_in_Cart = self.driver.find_elements(By.CLASS_NAME, 'btn_inventory')
        count = 0
        for n in range(6):
                if count_of_items_in_Cart[n].text == "Remove":
                        count += 1
        print(count)

        Actual_items_added_in_Cart = int(self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)
        print(Actual_items_added_in_Cart)
        assert count==Actual_items_added_in_Cart

            
        count_of_items_in_Cart = self.driver.find_elements(By.CLASS_NAME, 'btn_inventory')
        count=6
        for n in range(6):
                if count_of_items_in_Cart[n].text == "Remove":
                        count_of_items_in_Cart[n].click()
                        count -= 1
                        print(count)
        assert EC.invisibility_of_element_located((By.CLASS_NAME, 'btn_inventory'))

        
        cart = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        # List to store the texts found
        texts = []
        # Iterate over the elements to get their text content
        for element in elements:
                texts.append(element.text)
        # List of expected texts
        expected_texts = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
        # Verifying each expected text
        for expected_text in expected_texts:
                if expected_text in texts:
                        print(f"Text '{expected_text}' is present.")
                else:
                        print(f"Text '{expected_text}' is not present.")


        button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[1]")
        # Verifying button presence
        if button.is_displayed() and button.is_enabled():
                print("Button is present and enabled.")
        else:
                print("Button is not present or not enabled.")

                
        # Get text from the button
        button_text = button.text

        # Verify text inside the button
        expected_text = "Continue Shopping"
        if button_text == expected_text:
                print(f"Button text '{button_text}' matches the expected text '{expected_text}'.")
        else:
                print(f"Button text '{button_text}' does not match the expected text '{expected_text}'.")

        button.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"title"), "Products"))  


        cart_btn=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
        check_out_btn=self.driver.find_element(By.CLASS_NAME,"checkout_button").click()
        User_detail_TextBox = self.driver.find_elements(By.CLASS_NAME,"form_input")
        User_detail_TextBox [0].send_keys("charitha")
        User_detail_TextBox [1].send_keys("raj")
        User_detail_TextBox [2].send_keys("570001")
        continue_btn=self.driver.find_element(By.CLASS_NAME,"btn_action").click()
      

        header= (By.CLASS_NAME, "summary_total_label")
        expected_error_message = "Total: $"
        error_message_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(header))
        actual_error_message = error_message_element.text

       
        # Finding and adding items to the cart
        item_prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")  # Locate all item prices
        total_price = 0
        # Adding each item price to the total
        for item_price in item_prices:
                price = float(item_price.text.strip().replace("$", ""))  
                total_price += price
        # Finding the total price displayed in the cart
        cart_total = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label") 
        # Check if the total displayed in the cart matches the calculated total
        '''if float(cart_total.text.strip().replace("$", "")) == total_price:
                print("Total price in cart matches the calculated total: $", total_price)
        else:
                print("Total price in cart does not match the calculated total.")'''

        


        cart_total_text = cart_total.text.strip().replace("Item total: ", "").replace("$", "").strip()
        # Converting the extracted numerical part to a float
        cart_total_value = float(cart_total_text)
        # Checking if the total displayed in the cart matches the calculated total
        if cart_total_value == total_price:
                print("Total price in cart matches the calculated total: $", total_price)
        else:
                print("Total price in cart does not match the calculated total.")



        
   
        cancel=self.driver.find_element(By.CLASS_NAME,"cart_cancel_link")
        print(cancel.is_displayed())
        cancel.click()
        cancel=self.driver.find_element(By.CLASS_NAME,"title").text
        text="Products"
        if text==cancel:
                print("match")
        check_out=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
        check_out=self.driver.find_element(By.CLASS_NAME,"checkout_button").click()
        User_detail_TextBox = self.driver.find_elements(By.CLASS_NAME,"form_input")
        User_detail_TextBox [0].send_keys("charitha")
        User_detail_TextBox [1].send_keys("raj")
        User_detail_TextBox [2].send_keys("570001")
        continue_btn=self.driver.find_element(By.CLASS_NAME,"btn_action").click()
    
        finish=self.driver.find_element(By.CLASS_NAME,"cart_button").click()

        #TS_Checkout_067
        text2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))) 
        new_text = "Thank you for your order!"
        if text2== new_text:
                print("Text match")
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-text"))) 
        new_text1 = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        if text== new_text1:
                print("Text match")

        back=self.driver.find_element(By.CLASS_NAME,"btn_small")
        print(back.is_displayed())


        button_color = back.value_of_css_property("background-color")   #TS_Checkout_068
        print("Button color:", button_color)
        expected_color = "rgba(61, 220, 145, 1)"  # Replace with the expected color in RGBA format
        if button_color == expected_color:
                print("Button color is  green")
        else:
                print("Button color is not  green")


        back.click() 
        self.driver.back()

        '''hamberg=self.driver.find_element(By.ID,"react-burger-menu-btn")
        print(hamberg.is_displayed())
        hamberg.click()
        Left_Panel=self.driver.find_elements(By.CLASS_NAME,"menu-item")
        assert Left_Panel[0].text=="All Items"
        assert Left_Panel[1].text=="About"
        assert Left_Panel[2].text=="Logout"
        assert Left_Panel[3].text=="Reset App State"

        
        Left_Panel[1].click()
        screen= self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div/div[1]/div[1]/a/div[1]/span/img")
        image_src = screen.get_attribute("src")
        print("image_src")
        assert image_src =="/images/logo.svg"
        self.driver.back()
        
        
        hamberg.click()
        cross_symbol=self.driver.find_element(By.ID,"react-burger-cross-btn")
        print(cross_symbol.is_displayed())
        cross_symbol.click()'''

        
        scroll_height = self.driver.execute_script("return document.body.scrollHeight;")
        # Getting the height of the viewport
        viewport_height = self.driver.execute_script("return window.innerHeight;")
        # Comparing scroll height with viewport height
        is_scrollable = scroll_height > viewport_height
        if is_scrollable:
                print("The page is scrollable.")
        else:
                print("The page is not scrollable or fully loaded.")






    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()