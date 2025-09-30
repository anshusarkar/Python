import swisseph as swe
from datetime import datetime
import pytz

# Set path to ephemeris files (download from Swiss Ephemeris)
swe.set_ephe_path('/path/to/ephe')

# Input: Birth date, time, location
birth_date = datetime(1990, 5, 15, 14, 30)  # May 15, 1990, 2:30 PM
timezone = pytz.timezone('America/New_York')
birth_date = timezone.localize(birth_date)
utc_time = birth_date.astimezone(pytz.UTC)

# Convert to Julian Day (required by Swiss Ephemeris)
jd = swe.julday(utc_time.year, utc_time.month, utc_time.day,
                utc_time.hour + utc_time.minute / 60.0)

# Calculate planetary positions (e.g., Sun)
sun_pos = swe.calc_ut(jd, swe.SUN)[0]  # Returns longitude in degrees
sun_sign = int(sun_pos / 30)  # Zodiac sign (0 = Aries, 1 = Taurus, etc.)

print(f"Sun position: {sun_pos:.2f} degrees, Sign: {sun_sign}")