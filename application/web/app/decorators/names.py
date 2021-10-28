regex = "[0-9]~!@#$%^&*()_-+={[}]|\?/><.,"


def names_decorator(level, message):
    def names_decorator_inner(func):
        def names_decorator_innnermost(self, *args, **kwargs):
            if (
                not any(response in regex for response in self.user_response)
                and self.user_response is not None
            ):
                return func(self, *args, **kwargs)
            else:
                menu_text = f"{self.user_response} is an invalid name !!\n"
                menu_text += f"{message}\n"
                self.session["level"] = level
                return self.ussd_continue(menu_text)

        return names_decorator_innnermost

    return names_decorator_inner
