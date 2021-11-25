from sqlalchemy.sql import func

from app.decorators.location import location_decorator
from app.decorators.payment_decorators import charge_users_decorator
from app.houses.data import houses
from app.houses.houses_query_menu import HousesQueryMenu
from app.houses.utils import get_type_of_house
from app.models import Houses


class WardResults(HousesQueryMenu):
    @charge_users_decorator
    @location_decorator(level=22, message="Enter Ward")
    def houses_ward_query_results(self):
        rent = bool
        hse_id = self.session.get("hse_type")
        ward = self.user_response
        if self.session.get("rent_house"):
            rent = True
            # service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            # service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_house(houses, hse_id))
        if (
            Houses.query.filter_by(
                ward=ward, for_rent=rent, get_type_of_house=hse_id
            ).count()
            > 2
        ):
            menu_text = f"{get_type_of_house(hse_id, houses)} in {ward}\n"
            menu_text += f"{str(Houses.query.filter_by(ward=ward, for_rent=rent, type_of_house=hse_id).order_by(func.random()).limit(2).all())[1:-1]}"
            menu_text += "Re-enter ward  to see more results\n"
            menu_text += f"{ward.title()} >> (next)\n"
            return self.ussd_continue(menu_text)

        if (
            0
            < Houses.query.filter_by(
                ward=ward, for_rent=rent, get_type_of_house=hse_id
            ).count()
            <= 2
        ):
            menu_text = f"{get_type_of_house(hse_id, houses)} in {ward}\n"
            menu_text += f"{str(Houses.query.filter_by(ward=ward, for_rent=rent, type_of_house=hse_id).all())[1:-1]}"
            return self.ussd_end(menu_text)

        else:
            menu_text = "No records\nKindly try again later\n"
            return self.ussd_end(menu_text)

    def execute(self):
        level = self.session.get("level")
        menu = {
            21: self.houses_ward_query_results,
        }
        return menu.get(level, self.house_services_menu)()
