

def us_epa_index_description(US_EPA_Index):

  if US_EPA_Index == 1:
    EPA_description="Good: Air quality is satisfactory, and air pollution poses little or no risk." 
  elif US_EPA_Index ==2:
    EPA_description="Moderate: Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
  elif US_EPA_Index ==3:
    EPA_description="Unhealthy for Sensitive Groups: Members of sensitive groups may experience health effects. The general public is less likely to be affected."
  elif US_EPA_Index ==4:
    EPA_description="Unhealthy: Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
  elif US_EPA_Index ==5:
    EPA_description="Very Unhealthy: Health alert: The risk of health effects is increased for everyone."
  elif US_EPA_Index ==6:
    EPA_description="Hazardous: Health warning of emergency conditions: everyone is more likely to be affected."

  return EPA_description
