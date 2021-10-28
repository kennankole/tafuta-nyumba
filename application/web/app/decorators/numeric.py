regex = "!@#$%^&*()_-+={[}]|\?/><.,"


def numeric_decorator(level, message):
    def numeric_decorator_inner(func):
        def numeric_decorator_innermost(self, *args, **kwargs):
            if not any(response in regex for response in self.user_response):
                if self.user_response.isnumeric():
                    return func(self, *args, **kwargs)
                else:
                    menu_text = f"{self.user_response} is an invalid selection\n"
                    menu_text += f"{message}\n"
                    self.session["level"] = level
                    return self.ussd_continue(menu_text)
            else:
                menu_text = f"{self.user_response} is an invalid entry\n"
                menu_text += f"{message}\n"
                self.session["level"] = level
                return self.ussd_continue(menu_text)

        return numeric_decorator_innermost

    return numeric_decorator_inner
