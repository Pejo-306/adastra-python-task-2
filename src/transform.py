from fractions import Fraction


def to_fahrenheit(temperature: str) -> str:
    temperature = temperature.strip()
    degrees = temperature[:3] if temperature[0] in ('+', '-') else temperature[:2]
    sign = temperature[-1]
    degrees = int(Fraction('9/5') * int(degrees) + 32) if sign == 'C' else degrees
    return f'{degrees} F'
