import json
from app.location import location


regex = "[0-9]~!@#$%^&*()_-+={[}]|\?/><.,"
counties = json.loads(location)

def location_decorator(level, message):
    def validate_location_inner(func):
        def validate_location_innermost(self, *args, **kwargs):
            if not any(response in regex for response in self.user_response):
                if self.user_response.title() in counties.__str__():
                    return func(self, *args, **kwargs)
                else:
                    menu_text = f"{self.user_response} Does not exist\n"
                    menu_text += f"{message}"
                    self.session['level'] = level
                    return self.ussd_continue(menu_text)
            else:
                menu_text = f"{self.user_response} Invalid input!!\n"
                menu_text += "Names may not contain special characters\n"
                menu_text += f"{message}"
                self.session['level'] = level
                return self.ussd_continue(menu_text)
        return validate_location_innermost
    return validate_location_inner
