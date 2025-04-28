from datetime import datetime, timedelta


def round_time_to_nearest_hour(dt: datetime) -> datetime:
    "Rounds time object to nearest time"

    discard = timedelta(minutes = dt.minute % 60,
                        seconds = dt.second,
                        microseconds = dt.microsecond)
    dt -= discard
    if discard >= timedelta(minutes=30):
        dt += timedelta(hours=1)
    return dt
