#!/usr/bin/env python

import pywapi

def getCurrentWTC(postal):
	result = getCurrentConditions(postal)
	# postal = str(postal)
	# result = pywapi.get_weather_from_weather_com(postal)['current_conditions']
	wind = result['wind']['speed']
	temp =  result['temperature']
	clouds = result['text']
	return (wind, temp, clouds)

def getCurrentConditions(postal):
	postal = str(postal)
	return pywapi.get_weather_from_weather_com(postal)['current_conditions']

def celToF(celcius):
	pass
