from sqlalchemy.sql import func

from app.decorators.names import names_decorator
from app.decorators.payment_decorators import charge_users_decorator
from app.houses.data import houses
from app.houses.houses_query_menu import HousesQueryMenu
from app.houses.utils import get_type_of_house
from app.models import Houses


class EstateResults(HousesQueryMenu):
    @charge_users_decorator
    @names_decorator(level=23, message="Enter Estate or village name")
    def houses_village_estate_query_results(self):
        rent = bool
        hse_id = self.session.get("hse_type")
        estate = self.user_response
        if self.session.get("rent_house"):
            rent = True
            # service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            # service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_house(houses, hse_id))
        if (
            Houses.query.filter_by(
                name_of_estate_or_village=estate,
                for_rent=rent,
                get_type_of_house=hse_id,
            ).count()
            > 2
        ):
            menu_text = f"{get_type_of_house(hse_id, houses)} in {estate}\n"
            menu_text += f"{str(Houses.query.filter_by(name_of_estate_or_village=estate, for_rent=rent, type_of_house=hse_id).order_by(func.random()).limit(2).all())[1:-1]}"
            menu_text += "Re-enter estate  to see more results\n"
            menu_text += f"{estate.title()} >> (next)\n"
            return self.ussd_continue(menu_text)

        if (
            0
            < Houses.query.filter_by(
                name_of_estate_or_village=estate,
                for_rent=rent,
                get_type_of_house=hse_id,
            ).count()
            <= 2
        ):
            menu_text = f"{get_type_of_house(hse_id, houses)} in {estate}\n"
            menu_text += f"{str(Houses.query.filter_by(name_of_estate_or_village=estate, for_rent=rent, type_of_house=hse_id).all())[1:-1]}"
            return self.ussd_end(menu_text)

        else:
            menu_text = "No records\nKindly try again later\n"
            return self.ussd_end(menu_text)

    def execute(self):
        level = self.session.get("level")
        menu = {
            22: self.houses_village_estate_query_results,
        }
        return menu.get(level, self.house_services_menu)()
