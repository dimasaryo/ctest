# ctest
Page Object Pattern &amp; Appium POC


### Requirements:
1. Python 2.6 or above
2. Nodejs
3. Appium
4. Android Emulator
5. nose2


### Project Structure:
```
sources\
   android_app\                     # Application abstraction layer
       app\
           <domain>\
               ..._page.py
               ..._page_element.py
           ...
       tests\                       # Test layer
            <domain>\
                ..._input.py
                ..._test.py
            ...
   libs\                           # Webdriver abstraction layer

```

### USAGE
```
$virtualenv ctest
$source ctest/bin/activate

$cd ctest/android_app
$pip install -r requirements.txt
$nose -t ../
```

### References
- https://martinfowler.com/bliki/PageObject.html


### Future Development:
1. Test config plugin.
2. Better logging system and screenshot capturing.
3. Reporting system integration.
4. Web and iOs handler.
