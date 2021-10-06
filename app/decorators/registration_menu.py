def registration_menu_decorator(level, message):
    def registration_menu_decorator_inner(func):
        def registration_menu_decorator_innermost(self, *args, **kwargs):
            if self.user_response == "00":
                return func(self, *args, **kwargs)
            if self.session.get("name_of_city") != "00":
                return func(self, *args, **kwargs)
            else:
                menu_text = f"{self.user_response} is an invalid selection\n"
                menu_text += f"{message}\n"
                self.session['level'] = level
                return self.ussd_continue(menu_text)
        return registration_menu_decorator_innermost
    return registration_menu_decorator_inner