regex = "!@#$%^&*()_-+={[}]|\?/><.,"

def phone_number_decorator(level, message):
    def phone_number_decorator_inner(func):
        def phone_number_decorator_innermost(self, *args, **kwargs):
            if not any(response in regex for response in self.user_response):
                if self.user_response.isnumeric() and self.user_response.startswith('0'):
                    return func(self, *args, **kwargs)
                else:
                    menu_text = f"{self.user_response} is an invalid entry for phone number\n"
                    menu_text += f"{message}\n"
                    self.session['level'] = level
                    return self.ussd_continue(menu_text)
            else:
                    menu_text = f"{self.user_response} is an invalid entry for phone number\n"
                    menu_text += f"{message}\n"
                    self.session['level'] = level
                    return self.ussd_continue(menu_text)
        return phone_number_decorator_innermost
    return phone_number_decorator_inner

                   
