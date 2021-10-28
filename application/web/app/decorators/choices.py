def validate_choices(level, message, choices):
    def validate_choices_inner(func):
        def validate_choices_innermost(self, *args, **kwargs):
            if self.user_response in choices:
                return func(self, *args, **kwargs)
            else:
                menu_text = f"{self.user_response} is an invalid choice\n"
                menu_text += f"{message}\n"
                self.session["level"] = level
                return self.ussd_continue(menu_text)

        return validate_choices_innermost

    return validate_choices_inner
