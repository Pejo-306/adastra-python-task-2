from fractions import Fraction


def to_fahrenheit(temperature: str) -> str:
    """Convert Celsius temperature value to Fahrenheit

    If the input temperature value is already in Fahrenheit, it is only formatted
    and returned as is.

    :param temperature: input temperature, either in Celsius or Fahrenheit
    :type temperature: str
    :return: formatted temperature value in Fahrenheit
    :rtype: str
    """
    temperature = temperature.strip()
    degrees = temperature[:3] if temperature[0] in ('+', '-') else temperature[:2]
    sign = temperature[-1]
    degrees = int(Fraction('9/5') * int(degrees) + 32) if sign == 'C' else degrees
    return f'{degrees} F'
