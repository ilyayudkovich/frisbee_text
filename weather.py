#!/usr/bin/env python

import pywapi

def getCurrentWTC(postal):
	result = getCurrentConditions(postal)
	wind = result['wind']['speed']
	temp =  result['temperature']
	clouds = result['text']
	return (wind, temp, clouds)

def getCurrentConditions(postal):
	postal = str(postal)
	return pywapi.get_weather_from_weather_com(postal, units='')['current_conditions']

def getCurrentConditionsMetric(postal):
	postal = str(postal)
	return pywapi.get_weather_from_weather_com(postal, units='')['current_conditions']

def celToF(celcius):
	return celcius * 9/5 + 32

def kiloToMil(km):
	return km / .6
