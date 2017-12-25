# ctest
Page Object Pattern &amp; Appium POC

### Requirements:
1. Python 2.6 or above
2. Nodejs
3. Appium
3. Android Emulator

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

### Future Development:
1. Test config plugin.
2. Better logging system and screenshot capturing.
3. Reporting system integration.
4. Web and iOs handler.
