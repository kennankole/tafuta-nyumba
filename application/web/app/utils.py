from app import db
from app.models import CapturingUserData


def storing_user_records(phone, service_type, property_type):
    if not CapturingUserData.query.filter_by(
        contacts=phone, property_type=property_type
    ).first():
        save_to_db = CapturingUserData(
            contacts=phone, service_type=service_type, property_type=property_type
        )
        db.session.add(save_to_db)
        db.session.commit()
        return save_to_db
    else:
        return None