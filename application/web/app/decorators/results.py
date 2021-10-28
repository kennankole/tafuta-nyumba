def results_decorator(message, model):
    def results_decorator_inner(func):
        def results_decorator_innermost(self, *args, **kwargs):
            if "no" in model:
                menu_text = f"{model}\n"
                return self.ussd_end(menu_text)
            else:
                menu_text = f"{message} in {self.user_response}\n"
                menu_text += f"{model}"
                menu_text += f"{self.user_response.title()} >> (next)"
                return self.ussd_continue(menu_text)

        return results_decorator_innermost

    return results_decorator_inner
