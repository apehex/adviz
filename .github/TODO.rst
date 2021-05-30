####
TODO
####

******
GLOBAL
******

- [x] use poetry for dep management, instead of pipenv
- [x] keep only the modules in adviz
- [ ] save all the data in mongodb
- [ ] create a dashboard in dash / bokeh

*******
WORFLOW
*******

- [ ] collect / update referentials
- [ ] rate & rank ads
- [ ] view the ads : select the relevant offers, refine project
- [ ] complete the data (call the sellers, correct the data errors)

*******************
STEPS TO VANLIFE :)
*******************

- [x] data collection
- [x] data cleaning & merging
- [x] ad scraping & alerts
- [ ] filtering & ranking tools
- [ ] project dashboard
- [ ] sharing datasets : kaggle, open datasets => loop back on gh
- [ ] contact, verification of ads
- [ ] & finally buying ! and begining a new chapter !..
- [ ] diy conversion : electricity, internet, solar, water, bedding, furniture, insulation

***************
DATA COLLECTION
***************

- [ ] car (especially van) size (volume)
- [ ] car lifespan
- [ ] fuel costs per region (country most likely)
- [x] van mpg & emissions
- [ ] insurance prices database / scraping
- [x] van / utility list
- [ ] repairs costs
- [ ] conversion costs
- [ ] parking costs

*******
DATAVIZ
*******

- [ ] plot the ad price vs most characteristics
- [ ] plot the averages / stds
- [ ] locate the ads on a map

******
MINING
******

- [x] plot consumption vs emission (by fuel type)
- [x] linear regression :
  - [x] mpg vs emission vs fuel type
  - [ ] mpg vs (gross) weight
- [x] estimation from combustion chemistry

*************
CAR VALUATION
*************

- [ ] age & mileage
- [ ] fuel efficiency / current models
- [ ] reparation cost
- [ ] conversion cost
- [ ] equipment cost
- [ ] actual cost (price_new + all)
- [ ] fuel & electricity price
- [ ] cost at 0 & 100 000 km

*******
RANKING
*******

- [ ] normalize each column used for rating
- [ ] metric for fuel consumption
- [ ] metric for co2, co, nox, pm emissions
- [ ] metric for habitable space
- [ ] metric for mileage
- [ ] metric for the cost
- [ ] overall priority for each metric
- [ ] global rating
- [ ] rank all the potential vehicles
- [ ] rank all the ads

*******
HONESTY
*******

- [ ] compare the informations from the seller to the ref
- [ ] détails et contenu de l'annonce (déjà la taille...)
- [ ] ratio estimated value / price

*********
DASHBOARD
*********

- [ ] Project :
  - [ ] habitable space : min x, y, z, V
  - [ ] budget : fuel, diy, van, insurance
  - [ ] miles / months, year, total
  - [ ] priorities (relative weights) : price, space, (mile)age,
  - [ ] ranges : consumption (from budget vs miles)
- [ ] Reparation costs :
  - [ ] MOT
  - [ ] paint
  - [ ] tyres
  - [ ] mech ?
- [ ] Conversion costs :
  - [ ] materials
  - [ ] insulation
  - [ ] water tank
  - [ ] batteries
  - [ ] solar panels ?
  - [ ] tools
  - [ ] garage
- [ ] Living costs :
  - [ ] electricity : kW/h
  - [ ] diesel
  - [ ] petrol
  - [ ] lpg
  - [ ] insurance
  - [ ] parking (% time idle)
  - [ ] total (over a period / distance)
- [ ] rank & highlight ads

************
VERIFICATION
************

- [ ] mileage
- [ ] technical checkup
- [ ] papers

**************
DIY CONVERSION
**************

- [ ] cost of diy materials / tools / etc
- [ ] planning & tracking of the conversion
- [ ] satellite dish => internet connection

****
TEST
****

- [ ] find model & make
- [ ] find closest make
