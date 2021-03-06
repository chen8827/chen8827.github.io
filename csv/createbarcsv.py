import csv
import pandas as pd

#create csv
path='bar.csv'

#write csv
with open(path,'w',newline='',encoding="utf-8") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['name','allmap','map','lat','lon','insof','insplace'])

    writer.writerow(['CÉ LA VI Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.9877158838653!2d121.56377121405262!3d25.034490944427894!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab5b3896b905%3A0x1e74397cfefb7d35!2sC%C3%89%20LA%20VI%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627114073945!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.9877158838567!2d121.5637712140526!3d25.03449094442789!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab5b3896b905%3A0x1e74397cfefb7d35!2sC%C3%89%20LA%20VI%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627051043258!5m2!1szh-TW!2stw',
                     '25.034651339110574',
                     '121.56601354085598',
                     'https://www.instagram.com/celavitaipei/',
                     'https://www.instagram.com/explore/locations/290581664980572/ce-la-vi-taipei/'
                     ])
    
    writer.writerow(['A Train Leads The Way To Jazz',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7229.347678714329!2d121.533829286667!3d25.045140548694906!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc6ce85e759a6b5b6!2sA%20Train%20Leads%20The%20Way%20To%20Jazz!5e0!3m2!1szh-TW!2stw!4v1627106582504!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7229.347678714329!2d121.533829286667!3d25.045140548694906!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc6ce85e759a6b5b6!2sA%20Train%20Leads%20The%20Way%20To%20Jazz!5e0!3m2!1szh-TW!2stw!4v1627106582504!5m2!1szh-TW!2stw',
                     '25.048558967399718',
                     '121.54066185270392',
                     'https://www.instagram.com/atrainjazzbar/',
                     'https://www.instagram.com/explore/locations/193557744001044/a-train-leads-the-way-to-jazz/'
                     ])

    writer.writerow(['B Line by A Train',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d28917.969392318108!2d121.51326835155487!3d25.042686660749276!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xda5ac55b910ed4de!2sB%20Line%20by%20A%20Train!5e0!3m2!1szh-TW!2stw!4v1627124305958!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d28917.969392318108!2d121.51326835155487!3d25.042686660749276!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xda5ac55b910ed4de!2sB%20Line%20by%20A%20Train!5e0!3m2!1szh-TW!2stw!4v1627124305958!5m2!1szh-TW!2stw',
                     '25.0446695750432',
                     '121.53060615124036',
                     'https://www.instagram.com/blinebyatrain/',
                     'https://www.instagram.com/explore/locations/1014042788/b-line-by-a-train/'
                     ])
    
    writer.writerow(['C Park by A Train',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7229.442806681271!2d121.53063209352132!3d25.043527009384974!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xcffae5772f027703!2sC%20Park%20by%20A%20Train!5e0!3m2!1szh-TW!2stw!4v1627124766691!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7229.442806681271!2d121.53063209352132!3d25.043527009384974!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xcffae5772f027703!2sC%20Park%20by%20A%20Train!5e0!3m2!1szh-TW!2stw!4v1627124766691!5m2!1szh-TW!2stw',
                     '25.047172022741126',
                     '121.53378637143439',
                     'https://www.instagram.com/centralparkbyatrain/',
                     'https://www.instagram.com/explore/locations/1621291014853026/c-park-by-a-train/'
                     ])
    
    writer.writerow(['D Town by A Train',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d57013.92317632786!2d121.5112315178983!3d25.027274429718084!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xae6d615d75e7007b!2sD%20Town%20by%20A%20Train!5e0!3m2!1szh-TW!2stw!4v1627124866305!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d57013.92317632786!2d121.5112315178983!3d25.027274429718084!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xae6d615d75e7007b!2sD%20Town%20by%20A%20Train!5e0!3m2!1szh-TW!2stw!4v1627124866305!5m2!1szh-TW!2stw',
                     '25.045287443890714',
                     '121.54574838331926',
                     'https://www.instagram.com/dtownbyatrain/',
                     'https://www.instagram.com/explore/locations/1544536605557926/d-town-by-a-train/'
                     ])
    
    writer.writerow(['F Gallery by A Train',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d57013.92317632786!2d121.5112315178983!3d25.027274429718084!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x39a717bdc5f04307!2sF%20Gallery%20by%20A%20Train!5e0!3m2!1szh-TW!2stw!4v1627124929143!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d57013.92317632786!2d121.5112315178983!3d25.027274429718084!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x39a717bdc5f04307!2sF%20Gallery%20by%20A%20Train!5e0!3m2!1szh-TW!2stw!4v1627124929143!5m2!1szh-TW!2stw',
                     '25.05509767484309',
                     '121.54608678396065',
                     'https://www.instagram.com/flightgallerybyatrain/',
                     'https://www.instagram.com/explore/locations/622438758225425/f-gallery-by-a-train/'
                     ])

    writer.writerow(['jiangwayne.com Sake Bar 清酒吧',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.035227373554!2d121.55396391405247!3d25.03287854449244!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abede8ac4765%3A0x518c4b1b4e18b12e!2zamlhbmd3YXluZS5jb20gU2FrZSBCYXIg5riF6YWS5ZCn!5e0!3m2!1szh-TW!2stw!4v1627125025859!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.035227373554!2d121.55396391405247!3d25.03287854449244!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abede8ac4765%3A0x518c4b1b4e18b12e!2zamlhbmd3YXluZS5jb20gU2FrZSBCYXIg5riF6YWS5ZCn!5e0!3m2!1szh-TW!2stw!4v1627125025859!5m2!1szh-TW!2stw',
                     '25.03311670934868',
                     '121.5561418678496',
                     'https://www.instagram.com/jiangwayne.com.sakebar/',
                     'https://www.instagram.com/explore/locations/127125581110666/jiangwaynecom-sake-bar/'
                     ])
    
    writer.writerow(['jiangwayne.com Sake Bar 清酒吧 大稻埕',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14457.441695842046!2d121.50204591388847!3d25.055770281935214!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9aab08e98bb%3A0xc787bf679290125e!2zamlhbmd3YXluZS5jb20gU2FrZSBCYXIg5riF6YWS5ZCnIOWkp-eou-WflQ!5e0!3m2!1szh-TW!2stw!4v1627125285902!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14457.441695842046!2d121.50204591388847!3d25.055770281935214!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9aab08e98bb%3A0xc787bf679290125e!2zamlhbmd3YXluZS5jb20gU2FrZSBCYXIg5riF6YWS5ZCnIOWkp-eou-WflQ!5e0!3m2!1szh-TW!2stw!4v1627125285902!5m2!1szh-TW!2stw',
                     '25.056256241441428',
                     '121.51084355976849',
                     'https://www.instagram.com/jiangwayne.com.sakebar/',
                     'https://www.instagram.com/explore/locations/551285328653468/jiangwaynecom-sake-bar/'
                     ])
    
    writer.writerow(['SAKEBONO SAKE BAR 曙 日本清酒吧',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14459.872828584093!2d121.49025531388033!3d25.035152985358366!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9fbfae4e971%3A0xb4def5ba2638c320!2zU0FLRUJPTk8gU0FLRSBCQVIg5puZIOaXpeacrOa4hemFkuWQpw!5e0!3m2!1szh-TW!2stw!4v1627125234517!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14459.872828584093!2d121.49025531388033!3d25.035152985358366!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9fbfae4e971%3A0xb4def5ba2638c320!2zU0FLRUJPTk8gU0FLRSBCQVIg5puZIOaXpeacrOa4hemFkuWQpw!5e0!3m2!1szh-TW!2stw!4v1627125234517!5m2!1szh-TW!2stw',
                     '25.03598897507271',
                     '121.49918170579762',
                     'https://www.instagram.com/sakebono.sakebar/',
                     'https://www.instagram.com/explore/locations/347859359332082/sakebono/'
                     ])
    
    writer.writerow(['發琴吧 Ginspiration',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3612049292533!2d121.50989610000002!3d25.055743799999988!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a91472abec8b%3A0x697ad7f473d2e574!2z55m855C05ZCnIEdpbnNwaXJhdGlvbg!5e0!3m2!1szh-TW!2stw!4v1627133772364!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3612049292533!2d121.50989610000002!3d25.055743799999988!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a91472abec8b%3A0x697ad7f473d2e574!2z55m855C05ZCnIEdpbnNwaXJhdGlvbg!5e0!3m2!1szh-TW!2stw!4v1627133772364!5m2!1szh-TW!2stw',
                     '25.05590416688473',
                     '121.50990682883582',
                     'https://www.instagram.com/ginspirationbar/',
                     'https://www.instagram.com/explore/locations/1462824043739218/ginspiration/'
                     ])
    
    writer.writerow(['小城外Bar CityNorth',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3404373705125!2d121.5106366000001!3d25.056448000000017!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9145c60494d%3A0x9d9dd710a7fcec7d!2z5bCP5Z-O5aSWQmFyIENpdHlOb3J0aA!5e0!3m2!1szh-TW!2stw!4v1627134009701!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3404373705125!2d121.5106366000001!3d25.056448000000017!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9145c60494d%3A0x9d9dd710a7fcec7d!2z5bCP5Z-O5aSWQmFyIENpdHlOb3J0aA!5e0!3m2!1szh-TW!2stw!4v1627134009701!5m2!1szh-TW!2stw',
                     '25.056627804247594',
                     '121.51070097301502',
                     'https://www.instagram.com/bar_citynorth/',
                     'https://www.instagram.com/explore/locations/453825028156666/bar-citynorth/'
                     ])
    
    writer.writerow(['Le Zinc 洛 Café & Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3536464504073!2d121.51054599999995!3d25.056000100000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a91468ba8a91%3A0x734b2cdaca2b9cf4!2zTGUgWmluYyDmtJsgQ2Fmw6kgJiBCYXI!5e0!3m2!1szh-TW!2stw!4v1627134115800!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3536464504073!2d121.51054599999995!3d25.056000100000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a91468ba8a91%3A0x734b2cdaca2b9cf4!2zTGUgWmluYyDmtJsgQ2Fmw6kgJiBCYXI!5e0!3m2!1szh-TW!2stw!4v1627134115800!5m2!1szh-TW!2stw',
                     '25.056160466549358',
                     '121.51051381349248',
                     'https://www.instagram.com/lezinc_taipeidadaocheng/',
                     'https://www.instagram.com/explore/locations/400414655/le-zinc-cafe-bar/'
                     ])
    
    writer.writerow(['沃森茶酒館 Watson Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3933077521265!2d121.50999469999998!3d25.0546552!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a99d6f9902cd%3A0x1f242a0ff23f022b!2z5rKD5qOu6Iy26YWS6aSoIFdhdHNvbiBCYXI!5e0!3m2!1szh-TW!2stw!4v1627134221078!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3933077521265!2d121.50999469999998!3d25.0546552!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a99d6f9902cd%3A0x1f242a0ff23f022b!2z5rKD5qOu6Iy26YWS6aSoIFdhdHNvbiBCYXI!5e0!3m2!1szh-TW!2stw!4v1627134221078!5m2!1szh-TW!2stw',
                     '25.054835006877763',
                     '121.50997324232831',
                     'https://www.instagram.com/watsonbar/',
                     'https://www.instagram.com/explore/locations/552651068495975/watson-bar/'
                     ])
    
    writer.writerow(['星夜 Starry night Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.5225463070888!2d121.51934789999999!3d25.050272299999992!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a90d8bd3c551%3A0x4d48a50c23d45855!2z5pif5aScIFN0YXJyeSBuaWdodCBCYXI!5e0!3m2!1szh-TW!2stw!4v1627134326612!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.5225463070888!2d121.51934789999999!3d25.050272299999992!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a90d8bd3c551%3A0x4d48a50c23d45855!2z5pif5aScIFN0YXJyeSBuaWdodCBCYXI!5e0!3m2!1szh-TW!2stw!4v1627134326612!5m2!1szh-TW!2stw',
                     '25.05047155256771',
                     '121.51934789999999',
                     'https://www.instagram.com/starrynight20180101/',
                     'https://www.instagram.com/explore/locations/2110283249195161/starry-night-bar/'
                     ])
    
    writer.writerow(['醜 Sponge',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.5106934156815!2d121.51617570000002!3d25.050674300000008!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9708d7f406d%3A0x6e4fd957dcb0b511!2z6YacIFNwb25nZQ!5e0!3m2!1szh-TW!2stw!4v1627134548630!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.5106934156815!2d121.51617570000002!3d25.050674300000008!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9708d7f406d%3A0x6e4fd957dcb0b511!2z6YacIFNwb25nZQ!5e0!3m2!1szh-TW!2stw!4v1627134548630!5m2!1szh-TW!2stw',
                     '25.050854112717445',
                     '121.51613278465668',
                     'https://www.instagram.com/uuuggglllyyy2018/',
                     'https://www.instagram.com/explore/locations/291601791574682/sponge/'
                     ])
    
    writer.writerow(['Bitter Burro,take the bitter with the sweet',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.5172744460156!2d121.51662979999999!3d25.050451099999993!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a945140ecebb%3A0xecf8b8d553947b8f!2zQml0dGVyIEJ1cnJvLCB0YWtlIHRoZSBiaXR0ZXIgd2l0aCB0aGUgc3dlZXQt5Lqs56uZ5Y-w5YyX6LuK56uZIOeJueiJsuiqv-mFkiDnibnoibLkurrmsKPphZLlkKcg5bCP6YWM5o6o6JamIOe2k-WFuOmFkuWQpyBQb3B1bGFyIENvY2t0YWlsIEJhcg!5e0!3m2!1szh-TW!2stw!4v1627134633126!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.5172744460156!2d121.51662979999999!3d25.050451099999993!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a945140ecebb%3A0xecf8b8d553947b8f!2zQml0dGVyIEJ1cnJvLCB0YWtlIHRoZSBiaXR0ZXIgd2l0aCB0aGUgc3dlZXQt5Lqs56uZ5Y-w5YyX6LuK56uZIOeJueiJsuiqv-mFkiDnibnoibLkurrmsKPphZLlkKcg5bCP6YWM5o6o6JamIOe2k-WFuOmFkuWQpyBQb3B1bGFyIENvY2t0YWlsIEJhcg!5e0!3m2!1szh-TW!2stw!4v1627134633126!5m2!1szh-TW!2stw',
                     '25.050689230732445',
                     '121.51650105397',
                     'https://www.instagram.com/bitter_burro/',
                     'https://www.instagram.com/explore/locations/1261762593987457/bitter-burrotake-the-bitter-with-the-sweet/'
                     ])
    
    writer.writerow(['Hush Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.683105966805!2d121.54532009999998!3d25.0448262!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab6b6de3a2bb%3A0xfa879a1b41780ac2!2zSHVzaCBUYWlwZWkgLUNvY2t0YWlsIEJhciBCaXN0cm8g6aSQ6YWS6aSoIOaymeeZvOWMheW7giDmmZrppJDlrrXlpJwg576p5rOV5paZ55CGIOiBmuacg-WMheWgtA!5e0!3m2!1szh-TW!2stw!4v1627134803133!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.683105966805!2d121.54532009999998!3d25.0448262!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab6b6de3a2bb%3A0xfa879a1b41780ac2!2zSHVzaCBUYWlwZWkgLUNvY2t0YWlsIEJhciBCaXN0cm8g6aSQ6YWS6aSoIOaymeeZvOWMheW7giDmmZrppJDlrrXlpJwg576p5rOV5paZ55CGIOiBmuacg-WMheWgtA!5e0!3m2!1szh-TW!2stw!4v1627134803133!5m2!1szh-TW!2stw',
                     '25.045064341657746',
                     '121.54525572698499',
                     'https://www.instagram.com/hush_taipei/',
                     'https://www.instagram.com/explore/locations/106267134095266/hush-taipei/'
                     ])
    
    writer.writerow(['ROOM by Le Kief',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.703888096751!2d121.54482870000001!3d25.044121200000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab626a2e2cb1%3A0x367d65af17bf0f5e!2sROOM%20by%20Le%20Kief!5e0!3m2!1szh-TW!2stw!4v1627134908127!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.703888096751!2d121.54482870000001!3d25.044121200000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab626a2e2cb1%3A0x367d65af17bf0f5e!2sROOM%20by%20Le%20Kief!5e0!3m2!1szh-TW!2stw!4v1627134908127!5m2!1szh-TW!2stw',
                     '25.044301022328415',
                     '121.54480724232832',
                     'https://www.instagram.com/room_by_le_kief/',
                     'https://www.instagram.com/explore/locations/300781004010595/room-by-le-kief/'
                     ])
    
    writer.writerow(['房間餐酒 The Room Bistro',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.722340990293!2d121.54673839999998!3d25.04349519999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab6c46a2af7b%3A0x58f057d1cc976aea!2z5oi_6ZaT6aSQ6YWSIFRoZSBSb29tIEJpc3Rybw!5e0!3m2!1szh-TW!2stw!4v1627135034803!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.722340990293!2d121.54673839999998!3d25.04349519999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab6c46a2af7b%3A0x58f057d1cc976aea!2z5oi_6ZaT6aSQ6YWSIFRoZSBSb29tIEJpc3Rybw!5e0!3m2!1szh-TW!2stw!4v1627135034803!5m2!1szh-TW!2stw',
                     '25.04367502324639',
                     '121.54673839999998',
                     'https://www.instagram.com/theroombistro/',
                     'https://www.instagram.com/explore/locations/115279783265799/the-room/'
                     ])
    
    writer.writerow(['EAST END',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.737102994449!2d121.54602990000005!3d25.042994399999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdaf06c78c7%3A0x1d57f2497cfee0e4!2sEAST%20END!5e0!3m2!1szh-TW!2stw!4v1627135152347!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.737102994449!2d121.54602990000005!3d25.042994399999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdaf06c78c7%3A0x1d57f2497cfee0e4!2sEAST%20END!5e0!3m2!1szh-TW!2stw!4v1627135152347!5m2!1szh-TW!2stw',
                     '25.04321310480678',
                     '121.54615864602998',
                     'https://www.instagram.com/eastendbar/',
                     'https://www.instagram.com/explore/locations/978140842/east-end/'
                     ])
    
    writer.writerow(['花生俱樂部 Peanut Club',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.6983344577366!2d121.5469604!3d25.0443096!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab2d4a87cb4d%3A0xc03fa4deda78c51f!2z6Iqx55Sf5L-x5qiC6YOoIFBlYW51dCBDbHViLea3seWknOWSluWVoeW7syDnibnoibLlibXmhI_mlpnnkIYg5o6o6Jam54m56Imy57aT5YW46Kq_6YWS5ZCnIOmkkOmFkumkqOaWmeeQhg!5e0!3m2!1szh-TW!2stw!4v1627135235913!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.6983344577366!2d121.5469604!3d25.0443096!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab2d4a87cb4d%3A0xc03fa4deda78c51f!2z6Iqx55Sf5L-x5qiC6YOoIFBlYW51dCBDbHViLea3seWknOWSluWVoeW7syDnibnoibLlibXmhI_mlpnnkIYg5o6o6Jam54m56Imy57aT5YW46Kq_6YWS5ZCnIOmkkOmFkumkqOaWmeeQhg!5e0!3m2!1szh-TW!2stw!4v1627135235913!5m2!1szh-TW!2stw',
                     '25.044664383795663',
                     '121.54698185767168',
                     'https://www.instagram.com/peanutclubtaiwan/',
                     'https://www.instagram.com/explore/locations/2643331862558941/peanut-club/'
                     ])
    
    writer.writerow(['Bar Mood Taipei 吧沐',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7162657322533!2d121.54663049999996!3d25.04370129999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdae220bb81%3A0xf0391805045a3335!2zQmFyIE1vb2QgVGFpcGVpIOWQp-aykC1Db2NrdGFpbCBCYXIg5aC05Zyw56ef5YCfQmlzdHJvIOaZmumkkOWuteWknCBHcmlsbCDogZrmnIPljIXloLQgQmFyIEZvb2Qg5o6o6JamIFdoaXNreQ!5e0!3m2!1szh-TW!2stw!4v1627135520256!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7162657322533!2d121.54663049999996!3d25.04370129999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdae220bb81%3A0xf0391805045a3335!2zQmFyIE1vb2QgVGFpcGVpIOWQp-aykC1Db2NrdGFpbCBCYXIg5aC05Zyw56ef5YCfQmlzdHJvIOaZmumkkOWuteWknCBHcmlsbCDogZrmnIPljIXloLQgQmFyIEZvb2Qg5o6o6JamIFdoaXNreQ!5e0!3m2!1szh-TW!2stw!4v1627135520256!5m2!1szh-TW!2stw',
                     '25.043910283396745',
                     '121.54669487301499',
                     'https://www.instagram.com/barmood_taipei/',
                     'https://www.instagram.com/explore/locations/1961335540751839/bar-mood-taipei/'
                     ])
    
    writer.writerow(['OAK',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7354051422103!2d121.54742999999998!3d25.043052!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc54b7a6bbb%3A0xa6355d635206d8f5!2sOAK!5e0!3m2!1szh-TW!2stw!4v1627135596775!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7354051422103!2d121.54742999999998!3d25.043052!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc54b7a6bbb%3A0xa6355d635206d8f5!2sOAK!5e0!3m2!1szh-TW!2stw!4v1627135596775!5m2!1szh-TW!2stw',
                     '25.04329986530182',
                     '121.54741927116417',
                     'https://www.instagram.com/oak_bar/',
                     'https://www.instagram.com/explore/locations/305258113425935/oak-bar/'
                     ])
    
    writer.writerow(['Arpia Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.743858995287!2d121.5467668!3d25.04276520000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abfd7b932749%3A0xd00e7b2e1f28739d!2sArpia%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627135777044!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.743858995287!2d121.5467668!3d25.04276520000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abfd7b932749%3A0xd00e7b2e1f28739d!2sArpia%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627135777044!5m2!1szh-TW!2stw',
                     '25.04293530409026',
                     '121.54682044417913',
                     'https://www.instagram.com/arpia_taipei/',
                     'https://www.instagram.com/explore/locations/103436151676694/arpia-taipei/'
                     ])
    
    writer.writerow(['P.s. I Love You Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7431545109907!2d121.54739970000003!3d25.042789100000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abab1e7b0b39%3A0x6cc57c92a1f24d05!2zUC5zLiBJIExvdmUgWW91IEJhciAmIEJpc3RybyB8IFAuUy4gSGVhbHRoeSBCb3gg5b6u5YGl5bq36aSQ55uSIC0g5pqr5YGc5YWn55SofOWPsOWMl-adseWNgOmFkuWQp3zppJDphZLppKh86Kq_6aOy5aSW5bi2fOWBpeW6t-mkkOebknzkvr_nlbblpJbpgIF85b-g5a2d5pWm5YyWfOW_oOWtneW-qeiIiA!5e0!3m2!1szh-TW!2stw!4v1627135862907!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7431545109907!2d121.54739970000003!3d25.042789100000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abab1e7b0b39%3A0x6cc57c92a1f24d05!2zUC5zLiBJIExvdmUgWW91IEJhciAmIEJpc3RybyB8IFAuUy4gSGVhbHRoeSBCb3gg5b6u5YGl5bq36aSQ55uSIC0g5pqr5YGc5YWn55SofOWPsOWMl-adseWNgOmFkuWQp3zppJDphZLppKh86Kq_6aOy5aSW5bi2fOWBpeW6t-mkkOebknzkvr_nlbblpJbpgIF85b-g5a2d5pWm5YyWfOW_oOWtneW-qeiIiA!5e0!3m2!1szh-TW!2stw!4v1627135862907!5m2!1szh-TW!2stw',
                     '25.042930043378366',
                     '121.54735678465669',
                     'https://www.instagram.com/p.s.iloveyoubar/',
                     'https://www.instagram.com/explore/locations/106802804512982/ps-i-love-you-bar/'
                     ])
    
    writer.writerow(['昨天 Bistro & Flavor',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.69702563266!2d121.54756390000001!3d25.04435400000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdb3ae5bec5%3A0xb6f1f2e866d3ef7d!2z5pio5aSpIEJpc3RybyAmIEZsYXZvcg!5e0!3m2!1szh-TW!2stw!4v1627135998032!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.69702563266!2d121.54756390000001!3d25.04435400000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdb3ae5bec5%3A0xb6f1f2e866d3ef7d!2z5pio5aSpIEJpc3RybyAmIEZsYXZvcg!5e0!3m2!1szh-TW!2stw!4v1627135998032!5m2!1szh-TW!2stw',
                     '25.04459214257481',
                     '121.5475209846567',
                     'https://www.instagram.com/thedaybefore0730/',
                     'https://www.instagram.com/explore/locations/1689438374693887/bistro-flavor/'
                     ])
    
    writer.writerow(['To Infinity & Beyond',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7172119545576!2d121.54787049999999!3d25.043669199999993!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab6699e2c0db%3A0x786c3722dc013964!2zVG8gSW5maW5pdHkgJiBCZXlvbmQgLSBDb2NrdGFpbCBCYXIgLyBXaGlza3kgLyBCaXN0cm8gLyDmnbHljYAgLyDphZLlkKc!5e0!3m2!1szh-TW!2stw!4v1627136069799!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7172119545576!2d121.54787049999999!3d25.043669199999993!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab6699e2c0db%3A0x786c3722dc013964!2zVG8gSW5maW5pdHkgJiBCZXlvbmQgLSBDb2NrdGFpbCBCYXIgLyBXaGlza3kgLyBCaXN0cm8gLyDmnbHljYAgLyDphZLlkKc!5e0!3m2!1szh-TW!2stw!4v1627136069799!5m2!1szh-TW!2stw',
                     '25.04378098189044',
                     '121.54802070370165',
                     'https://www.instagram.com/infinity_beyond_tpe/',
                     'https://www.instagram.com/explore/locations/114037283333854/to-infinity-and-beyond/'
                     ])
    
    writer.writerow(['WA-SHU 和酒',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.731696973058!2d121.5481579!3d25.0431778!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdad45dcb5b%3A0x6295e8865ee364e8!2zV0EtU0hVIOWSjOmFkg!5e0!3m2!1szh-TW!2stw!4v1627136231699!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.731696973058!2d121.5481579!3d25.0431778!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdad45dcb5b%3A0x6295e8865ee364e8!2zV0EtU0hVIOWSjOmFkg!5e0!3m2!1szh-TW!2stw!4v1627136231699!5m2!1szh-TW!2stw',
                     '25.043357623711824',
                     '121.54815789999999',
                     'https://www.instagram.com/washu.taipei/',
                     'https://www.instagram.com/explore/locations/589365934407046/wa-shu/'
                     ])
    
    writer.writerow(['Herban Kitchen & Bar 二本餐廳',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7381759408536!2d121.54826100000004!3d25.042958000000013!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdad2ee4777%3A0x53120d6df3d63300!2zSGVyYmFuIEtpdGNoZW4gJiBCYXIg5LqM5pys6aSQ5buz!5e0!3m2!1szh-TW!2stw!4v1627136302398!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7381759408536!2d121.54826100000004!3d25.042958000000013!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdad2ee4777%3A0x53120d6df3d63300!2zSGVyYmFuIEtpdGNoZW4gJiBCYXIg5LqM5pys6aSQ5buz!5e0!3m2!1szh-TW!2stw!4v1627136302398!5m2!1szh-TW!2stw',
                     '25.043128103822816',
                     '121.54828245767169',
                     'https://www.instagram.com/herban_kitchen/',
                     'https://www.instagram.com/explore/locations/239203331/herban-kitchen-bar/'
                     ])
    
    writer.writerow(['Closet Restaurant & Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7512693066515!2d121.5481451!3d25.042513800000016!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdad5d12413%3A0x9d0ecbfd2b7ffa80!2zQ2xvc2V0IOiho-arpemkkOmFki3lpKflronppJDphZLppKjmjqjolqYv5aSn5a6J576O6aOf5o6o6JamL-adseWNgOmkkOmFkumkqOaOqOiWpi_mnbHljYDnvo7po5_mjqjolqYv5Y-w5YyX576O6aOf5o6o6JamL-Wkp-WuiemFkuWQpy_mnbHljYDphZLlkKcv5Y-w5YyX6aSQ6YWS6aSo5o6o6JamL-WPsOWMl-mFkuWQp-aOqOiWpg!5e0!3m2!1szh-TW!2stw!4v1627136378647!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7512693066515!2d121.5481451!3d25.042513800000016!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abdad5d12413%3A0x9d0ecbfd2b7ffa80!2zQ2xvc2V0IOiho-arpemkkOmFki3lpKflronppJDphZLppKjmjqjolqYv5aSn5a6J576O6aOf5o6o6JamL-adseWNgOmkkOmFkumkqOaOqOiWpi_mnbHljYDnvo7po5_mjqjolqYv5Y-w5YyX576O6aOf5o6o6JamL-Wkp-WuiemFkuWQpy_mnbHljYDphZLlkKcv5Y-w5YyX6aSQ6YWS6aSo5o6o6JamL-WPsOWMl-mFkuWQp-aOqOiWpg!5e0!3m2!1szh-TW!2stw!4v1627136378647!5m2!1szh-TW!2stw',
                     '25.042683904438984',
                     '121.54797343862668',
                     'https://www.instagram.com/closet_taipei/',
                     'https://www.instagram.com/explore/locations/1025293385/closet-restaurant-bar/'
                     ])
    
    writer.writerow(['AQUA Lounge',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8319794199288!2d121.55221470000001!3d25.039775499999987!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab1c0d695c35%3A0xffa0a33dd29c9348!2sAQUA%20Lounge!5e0!3m2!1szh-TW!2stw!4v1627136747573!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8319794199288!2d121.55221470000001!3d25.039775499999987!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab1c0d695c35%3A0xffa0a33dd29c9348!2sAQUA%20Lounge!5e0!3m2!1szh-TW!2stw!4v1627136747573!5m2!1szh-TW!2stw',
                     '25.040013651465838',
                     '121.55232198835836',
                     'https://www.instagram.com/_aqua_lounge_/',
                     'https://www.instagram.com/explore/locations/100454771625538/aqua-lounge-featlpg/'
                     ])
    
    writer.writerow(['MOD Public Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8581097713104!2d121.55138889999999!3d25.038888900000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcf75a6e721%3A0xbdc12dd99e985a2a!2z5pGp5b6X6aSQ5Z2K!5e0!3m2!1szh-TW!2stw!4v1627136827436!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8581097713104!2d121.55138889999999!3d25.038888900000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcf75a6e721%3A0xbdc12dd99e985a2a!2z5pGp5b6X6aSQ5Z2K!5e0!3m2!1szh-TW!2stw!4v1627136827436!5m2!1szh-TW!2stw',
                     '25.03902984786064',
                     '121.55147473068665',
                     'https://www.instagram.com/modpublicbar/',
                     'https://www.instagram.com/explore/locations/100486866682266/mod-public-bar/'
                     ])
    
    writer.writerow(['花酒蔵 餐酒館 Aplus Dining Sake Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8609685548777!2d121.5508154!3d25.038791900000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcfa1e96f79%3A0x5b160770c433ee4a!2z6Iqx6YWS6JS1IOmkkOmFkumkqCBBcGx1cyBEaW5pbmcgU2FrZSBCYXI!5e0!3m2!1szh-TW!2stw!4v1627136894371!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8609685548777!2d121.5508154!3d25.038791900000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcfa1e96f79%3A0x5b160770c433ee4a!2z6Iqx6YWS6JS1IOmkkOmFkumkqCBBcGx1cyBEaW5pbmcgU2FrZSBCYXI!5e0!3m2!1szh-TW!2stw!4v1627136894371!5m2!1szh-TW!2stw',
                     '25.038952289058987',
                     '121.55087977301501',
                     'https://www.instagram.com/aplusdiningsakebar/',
                     'https://www.instagram.com/explore/locations/216563802/aplus-dining-sake-bar/'
                     ])
    
    writer.writerow(['Draft Land',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7965461532744!2d121.55404480000001!3d25.040977700000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc5df1d0ba5%3A0xf89017c20c5d3c86!2sDraft%20Land!5e0!3m2!1szh-TW!2stw!4v1627136984888!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7965461532744!2d121.55404480000001!3d25.040977700000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc5df1d0ba5%3A0xf89017c20c5d3c86!2sDraft%20Land!5e0!3m2!1szh-TW!2stw!4v1627136984888!5m2!1szh-TW!2stw',
                     '25.041254730578363',
                     '121.55404479999999',
                     'https://www.instagram.com/draftland/',
                     'https://www.instagram.com/explore/locations/1596995943682073/draft-land/'
                     ])
    
    writer.writerow(['墨子 | Mozi & Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8319705780204!2d121.5524022!3d25.039775800000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab45242a9ce9%3A0x72e7317624d8a31b!2z5aKo5a2QIEkgTU9aSQ!5e0!3m2!1szh-TW!2stw!4v1627137061537!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8319705780204!2d121.5524022!3d25.039775800000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab45242a9ce9%3A0x72e7317624d8a31b!2z5aKo5a2QIEkgTU9aSQ!5e0!3m2!1szh-TW!2stw!4v1627137061537!5m2!1szh-TW!2stw',
                     '25.039994510546656',
                     '121.55247730185081',
                     'https://www.instagram.com/mozisalon/',
                     'https://www.instagram.com/explore/locations/769565746555553/i-mozi/'
                     ])
    
    writer.writerow(['John Sakamoto坂本ジョン',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.840532445482!2d121.55393540000003!3d25.03948529999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab5515ec5253%3A0x174e0ee8e0463edf!2sJohn%20Sakamoto!5e0!3m2!1szh-TW!2stw!4v1627137289465!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.840532445482!2d121.55393540000003!3d25.03948529999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab5515ec5253%3A0x174e0ee8e0463edf!2sJohn%20Sakamoto!5e0!3m2!1szh-TW!2stw!4v1627137289465!5m2!1szh-TW!2stw',
                     '25.039713731547376',
                     '121.553999773015',
                     'https://www.instagram.com/john.sakamoto/',
                     'https://www.instagram.com/explore/locations/103692167917875/john-sakamoto/'
                     ])
    
    writer.writerow(['Book ing Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.861210224766!2d121.55447489999999!3d25.038783700000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab687fee0a75%3A0xbbbc211da00eb2e4!2zQm9vayBpbmcv5p2x5Y2A5o6o6JamL-WkluW4ti_ppJDphZIv6YWS5ZCnL-mkkOW7sy_mmZrppJA!5e0!3m2!1szh-TW!2stw!4v1627137370065!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.861210224766!2d121.55447489999999!3d25.038783700000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab687fee0a75%3A0xbbbc211da00eb2e4!2zQm9vayBpbmcv5p2x5Y2A5o6o6JamL-WkluW4ti_ppJDphZIv6YWS5ZCnL-mkkOW7sy_mmZrppJA!5e0!3m2!1szh-TW!2stw!4v1627137370065!5m2!1szh-TW!2stw',
                     '25.03901213285409',
                     '121.5545178153433',
                     'https://www.instagram.com/booking_taipei/',
                     'https://www.instagram.com/explore/locations/2363007833714575/book-ing-taipei/'
                     ])
    
    writer.writerow(['B612 Restaurant & Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.820387593942!2d121.5551725!3d25.040168800000007!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc613fa18f1%3A0x60e82c97c1569a2c!2zQjYxMiBSZXN0YXVyYW50ICYgQmFyIC0gQjYxMumkkOmFkumkqA!5e0!3m2!1szh-TW!2stw!4v1627137488110!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.820387593942!2d121.5551725!3d25.040168800000007!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc613fa18f1%3A0x60e82c97c1569a2c!2zQjYxMiBSZXN0YXVyYW50ICYgQmFyIC0gQjYxMumkkOmFkumkqA!5e0!3m2!1szh-TW!2stw!4v1627137488110!5m2!1szh-TW!2stw',
                     '25.040338907691588',
                     '121.55519395767169',
                     'https://www.instagram.com/b612_restaurant_bar/',
                     'https://www.instagram.com/explore/locations/387725725015415/b612-restaurant-bar/'
                     ])
    
    writer.writerow(['Oopsy Daisy Garden',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.846297285647!2d121.5545759!3d25.039289699999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc1bb49e739%3A0x1bce16dfa0c4f28e!2sOopsy%20Daisy%20Garden!5e0!3m2!1szh-TW!2stw!4v1627137579704!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.846297285647!2d121.5545759!3d25.039289699999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc1bb49e739%3A0x1bce16dfa0c4f28e!2sOopsy%20Daisy%20Garden!5e0!3m2!1szh-TW!2stw!4v1627137579704!5m2!1szh-TW!2stw',
                     '25.039450088408003',
                     '121.5545759',
                     'https://www.instagram.com/oopsydaisygarden/',
                     'https://www.instagram.com/explore/locations/2101498623503368/oopsy-daisy-garden/'
                     ])
    
    writer.writerow(['Le Kief 菱玖洋服',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8561881913784!2d121.55582219999998!3d25.038954100000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc89e1880d9%3A0x57bdfeffd9034d90!2zTGUgS2llZiDoj7HnjpbmtIvmnI0!5e0!3m2!1szh-TW!2stw!4v1627137656807!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8561881913784!2d121.55582219999998!3d25.038954100000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc89e1880d9%3A0x57bdfeffd9034d90!2zTGUgS2llZiDoj7HnjpbmtIvmnI0!5e0!3m2!1szh-TW!2stw!4v1627137656807!5m2!1szh-TW!2stw',
                     '25.03907560672144',
                     '121.5558329288358',
                     'https://www.instagram.com/le.kief.09/',
                     'https://www.instagram.com/explore/locations/1779269992350949/le-kief/'
                     ])
    
    writer.writerow(['JokeR Bistro & Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.6838871489645!2d121.55141259999999!3d25.0447997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc47d05a115%3A0x3fc398ab8af40f5a!2sJokeR%20Bistro%20%26%20Bar!5e0!3m2!1szh-TW!2stw!4v1627137775375!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.6838871489645!2d121.55141259999999!3d25.0447997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc47d05a115%3A0x3fc398ab8af40f5a!2sJokeR%20Bistro%20%26%20Bar!5e0!3m2!1szh-TW!2stw!4v1627137775375!5m2!1szh-TW!2stw',
                     '25.044794839960314',
                     '121.55142332883582',
                     'https://www.instagram.com/jokertaipei/',
                     'https://www.instagram.com/explore/locations/272750266468683/joker-bistro-bar/'
                     ])
    
    writer.writerow(['THE BED SHISHA LOUNGE',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.70604586952!2d121.55185599999997!3d25.044047999999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc467b26c13%3A0xbdf95ca5d44201e0!2sTHE%20BED%20Shisha%20Lounge!5e0!3m2!1szh-TW!2stw!4v1627137849220!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.70604586952!2d121.55185599999997!3d25.044047999999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc467b26c13%3A0xbdf95ca5d44201e0!2sTHE%20BED%20Shisha%20Lounge!5e0!3m2!1szh-TW!2stw!4v1627137849220!5m2!1szh-TW!2stw',
                     '25.044101460751694',
                     '121.55187745767167',
                     'https://www.instagram.com/thebedshishalounge/',
                     'https://www.instagram.com/explore/locations/217477395/the-bed-shisha-lounge/'
                     ])
    
    writer.writerow(['紙醉金迷Relax Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7214655193116!2d121.55326079999996!3d25.04352489999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab53f5636bc5%3A0xd416055d0349881!2z57SZ6YaJ6YeR6L-3IFJFTEFYIFRBSVBFSQ!5e0!3m2!1szh-TW!2stw!4v1627137950273!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7214655193116!2d121.55326079999996!3d25.04352489999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab53f5636bc5%3A0xd416055d0349881!2z57SZ6YaJ6YeR6L-3IFJFTEFYIFRBSVBFSQ!5e0!3m2!1szh-TW!2stw!4v1627137950273!5m2!1szh-TW!2stw',
                     '25.043568640803326',
                     '121.55327152883582',
                     'https://www.instagram.com/relaxtaipei/',
                     'https://www.instagram.com/explore/locations/1105101152979334/relax-taipei/'
                     ])
    
    writer.writerow(['Everland Shisha Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.732805298891!2d121.55039490000003!3d25.043140200000014!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc43d7fd287%3A0xf25dcb2df6c1461d!2sEverland%20Shisha%20Bar!5e0!3m2!1szh-TW!2stw!4v1627138033195!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.732805298891!2d121.55039490000003!3d25.043140200000014!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc43d7fd287%3A0xf25dcb2df6c1461d!2sEverland%20Shisha%20Bar!5e0!3m2!1szh-TW!2stw!4v1627138033195!5m2!1szh-TW!2stw',
                     '25.043222821763514',
                     '121.55041635767168',
                     'https://www.instagram.com/everland.taipei/',
                     'https://www.instagram.com/explore/locations/1839102902996273/everland-shisha-bar/'
                     ])
    
    writer.writerow(['Q9 lounge bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7325105315344!2d121.55273550000001!3d25.043150200000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc437e4cfe3%3A0x40319a85e89b3158!2sQ9%20LOUNGE%20BAR!5e0!3m2!1szh-TW!2stw!4v1627138122426!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7325105315344!2d121.55273550000001!3d25.043150200000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc437e4cfe3%3A0x40319a85e89b3158!2sQ9%20LOUNGE%20BAR!5e0!3m2!1szh-TW!2stw!4v1627138122426!5m2!1szh-TW!2stw',
                     '25.043164780314065',
                     '121.55273550000001',
                     'https://www.instagram.com/q9loungebar/',
                     'https://www.instagram.com/explore/locations/178301705584868/q9-lounge-bar/'
                     ])
    
    writer.writerow(['島Dau',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7343027153634!2d121.55311929999996!3d25.04308940000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab551dfedb1b%3A0x2b60b3c6c8a45f16!2z5bO2RGF1!5e0!3m2!1szh-TW!2stw!4v1627138191287!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7343027153634!2d121.55311929999996!3d25.04308940000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab551dfedb1b%3A0x2b60b3c6c8a45f16!2z5bO2RGF1!5e0!3m2!1szh-TW!2stw!4v1627138191287!5m2!1szh-TW!2stw',
                     '25.04315258137976',
                     '121.55311929999998',
                     'https://www.instagram.com/daubar2020/',
                     'https://www.instagram.com/explore/locations/113802880183372/dau/'
                     ])
    
    writer.writerow(['Unknown Lounge',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7375746194216!2d121.54976519999997!3d25.042978400000006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc52023b94f%3A0xdc4b186d39e7c38a!2sUnknown%20Lounge%20bar!5e0!3m2!1szh-TW!2stw!4v1627138263368!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7375746194216!2d121.54976519999997!3d25.042978400000006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc52023b94f%3A0xdc4b186d39e7c38a!2sUnknown%20Lounge%20bar!5e0!3m2!1szh-TW!2stw!4v1627138263368!5m2!1szh-TW!2stw',
                     '25.043119343160793',
                     '121.54975447116418',
                     'https://www.instagram.com/unknown_lounge/',
                     'https://www.instagram.com/explore/locations/242068295/unknown-lounge/'
                     ])
    
    writer.writerow(['狗毛 Hair of the Dog',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7573148193874!2d121.553797!3d25.042308699999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abaec77918a7%3A0x4fc119ba8c3e3e1c!2z54uX5q-bIEhhaXIgb2YgdGhlIERvZw!5e0!3m2!1szh-TW!2stw!4v1627138496027!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7573148193874!2d121.553797!3d25.042308699999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abaec77918a7%3A0x4fc119ba8c3e3e1c!2z54uX5q-bIEhhaXIgb2YgdGhlIERvZw!5e0!3m2!1szh-TW!2stw!4v1627138496027!5m2!1szh-TW!2stw',
                     '25.04237188178197',
                     '121.55377554232831',
                     'https://www.instagram.com/hairofthedogtaipei/',
                     'https://www.instagram.com/explore/locations/2180104895541474/hair-of-the-dog/'
                     ])
    
    writer.writerow(['酒窖子winebar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7661427764765!2d121.55328069999995!3d25.042009199999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc5cdba05cd%3A0xa8786bf2b266c29c!2z6YWS56qW5a2QV2luZSBiYXIgJiBXaW5lIHNob3A!5e0!3m2!1szh-TW!2stw!4v1627138567612!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7661427764765!2d121.55328069999995!3d25.042009199999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc5cdba05cd%3A0xa8786bf2b266c29c!2z6YWS56qW5a2QV2luZSBiYXIgJiBXaW5lIHNob3A!5e0!3m2!1szh-TW!2stw!4v1627138567612!5m2!1szh-TW!2stw',
                     '25.042101542818962',
                     '121.55330215767168',
                     'https://www.instagram.com/winebar_tw/',
                     'https://www.instagram.com/explore/locations/1032348068/wine-bar/'
                     ])
    
    writer.writerow(['Inges Bar&grill 台北萬豪酒店',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3613.6319138705167!2d121.55903!3d25.080461999999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ac0d594f13fd%3A0x46dbd27edf98de64!2zSU5HRSdTIEJhciAmIEdyaWxsIOWPsOWMl-iQrOixqumFkuW6lw!5e0!3m2!1szh-TW!2stw!4v1627138764469!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3613.6319138705167!2d121.55903!3d25.080461999999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ac0d594f13fd%3A0x46dbd27edf98de64!2zSU5HRSdTIEJhciAmIEdyaWxsIOWPsOWMl-iQrOixqumFkuW6lw!5e0!3m2!1szh-TW!2stw!4v1627138764469!5m2!1szh-TW!2stw',
                     '25.080505727618934',
                     '121.55904072883583',
                     'https://www.instagram.com/explore/locations/1355151937833349/inges-bargrill/',
                     'https://www.instagram.com/inges_taipei/'
                     ])
    
    writer.writerow(['YEN Bar-W Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.803575754196!2d121.56573429999999!3d25.040739199999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abd8d4d836a9%3A0xae9b50f18bf9eeeb!2sYen%20Bar!5e0!3m2!1szh-TW!2stw!4v1627139018980!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.803575754196!2d121.56573429999999!3d25.040739199999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abd8d4d836a9%3A0xae9b50f18bf9eeeb!2sYen%20Bar!5e0!3m2!1szh-TW!2stw!4v1627139018980!5m2!1szh-TW!2stw',
                     '25.040792662194125',
                     '121.56571284232832',
                     'https://www.instagram.com/wtaipei/',
                     'https://www.instagram.com/explore/locations/719021843/yen-bar-w-taipei/'
                     ])
    
    writer.writerow(['馬可波羅酒廊Marco Polo Lounge-香格里拉台北遠東國際大飯店',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.2250384941703!2d121.54713471405242!3d25.026435944750734!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aa32657c4a79%3A0xbad7b8c4fb2eafe!2z6aas5Y-v5rOi576F6YWS5buK77yITWFyY28gUG9sbyBMb3VuZ2XvvIktIOmmmeagvOmHjOaLieWPsOWMl-mBoOadseWci-mam-Wkp-mjr-W6lw!5e0!3m2!1szh-TW!2stw!4v1627139329604!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.2250384941703!2d121.54713471405242!3d25.026435944750734!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aa32657c4a79%3A0xbad7b8c4fb2eafe!2z6aas5Y-v5rOi576F6YWS5buK77yITWFyY28gUG9sbyBMb3VuZ2XvvIktIOmmmeagvOmHjOaLieWPsOWMl-mBoOadseWci-mam-Wkp-mjr-W6lw!5e0!3m2!1szh-TW!2stw!4v1627139329604!5m2!1szh-TW!2stw',
                     '25.0266741221121',
                     '121.54922683714645',
                     'https://www.instagram.com/marcopolo.tpe/',
                     'https://www.instagram.com/explore/locations/308122586314988/'
                     ])
    
    writer.writerow(['FRANK Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.9619683280266!2d121.56581909999998!3d25.035364700000017!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abb0b102ad23%3A0x3dafa20fb23d499c!2sFRANK%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627139090397!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.9619683280266!2d121.56581909999998!3d25.035364700000017!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abb0b102ad23%3A0x3dafa20fb23d499c!2sFRANK%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627139090397!5m2!1szh-TW!2stw',
                     '25.035447327001485',
                     '121.56580837116418',
                     'https://www.instagram.com/ethan_hung/',
                     'https://www.instagram.com/explore/locations/879311873/frank-taipei/'
                     ])
    
    writer.writerow(['Asia 49亞洲料理及酒廊',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.6184358376568!2d121.46472041405212!3d25.0130782452859!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a818c0afa7b9%3A0x14d08730d5211d7a!2zQXNpYSA0OSDkup7mtLLmlpnnkIblj4rphZLlu4o!5e0!3m2!1szh-TW!2stw!4v1627139575034!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.6184358376568!2d121.46472041405212!3d25.0130782452859!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a818c0afa7b9%3A0x14d08730d5211d7a!2zQXNpYSA0OSDkup7mtLLmlpnnkIblj4rphZLlu4o!5e0!3m2!1szh-TW!2stw!4v1627139575034!5m2!1szh-TW!2stw',
                     '25.013131719531653',
                     '121.46691982550995',
                     'https://www.instagram.com/asia49_lounge/',
                     'https://www.instagram.com/explore/locations/1148462368630433/asia-49/'
                     ])
    
    writer.writerow(['GREY ME瑰秘',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.2233358005974!2d121.55298181405244!3d25.026493744748365!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aa33a2e9aa99%3A0x1495bebb301f7219!2zR1JFWSBNReeRsOenmOOAguS_oee-qeWNgOmkkOmFkumkqC7mmZrppJDlrrXlpJznvo7po58u54m56Imy5rWu6KqH6Kq_6YWSLuiBmumkkOWMheWgtC7lj6_liLfljaEu5L-h576p5Y2A6aSQ5buz5o6o6JamLuWkp-WuieWNgOmkkOW7s-aOqOiWpi5Db2NrdGFpbCBCYXIuQmlzdHJv!5e0!3m2!1szh-TW!2stw!4v1627139730054!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.2233358005974!2d121.55298181405244!3d25.026493744748365!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aa33a2e9aa99%3A0x1495bebb301f7219!2zR1JFWSBNReeRsOenmOOAguS_oee-qeWNgOmkkOmFkumkqC7mmZrppJDlrrXlpJznvo7po58u54m56Imy5rWu6KqH6Kq_6YWSLuiBmumkkOWMheWgtC7lj6_liLfljaEu5L-h576p5Y2A6aSQ5buz5o6o6JamLuWkp-WuieWNgOmkkOW7s-aOqOiWpi5Db2NrdGFpbCBCYXIuQmlzdHJv!5e0!3m2!1szh-TW!2stw!4v1627139730054!5m2!1szh-TW!2stw',
                     '25.02654721315068',
                     '121.55519195434664',
                     'https://www.instagram.com/greyme/',
                     'https://www.instagram.com/explore/locations/1980122735646305/'
                     ])
    
    writer.writerow(['Geography Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.6785620062524!2d121.50309421405282!3d25.0449803440072!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a908d7489fa5%3A0x46f44ff566485c88!2zR2VvZ3JhcGh5IEJhcu-8j2NvY2t0YWls77yPd2hpc2t577yP6KW_6ZaA55S66YWS5ZCn77yPVGFpcGVpYmFy77yPeGltZW5iYXI!5e0!3m2!1szh-TW!2stw!4v1627139810576!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.6785620062524!2d121.50309421405282!3d25.0449803440072!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a908d7489fa5%3A0x46f44ff566485c88!2zR2VvZ3JhcGh5IEJhcu-8j2NvY2t0YWls77yPd2hpc2t577yP6KW_6ZaA55S66YWS5ZCn77yPVGFpcGVpYmFy77yPeGltZW5iYXI!5e0!3m2!1szh-TW!2stw!4v1627139810576!5m2!1szh-TW!2stw',
                     '25.045033804352403',
                     '121.50530435434703',
                     'https://www.instagram.com/geographybar/',
                     'https://www.instagram.com/explore/locations/1843567775974053/geography-bar/'
                     ])
    
    writer.writerow(['Bar THY',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.6508485419326!2d121.50139941405288!3d25.0459204439696!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9973fb0d69b%3A0xc8f4c432060659d5!2sBar%20THY!5e0!3m2!1szh-TW!2stw!4v1627139965638!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.6508485419326!2d121.50139941405288!3d25.0459204439696!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9973fb0d69b%3A0xc8f4c432060659d5!2sBar%20THY!5e0!3m2!1szh-TW!2stw!4v1627139965638!5m2!1szh-TW!2stw',
                     '25.04595446393115',
                     '121.50368465620177',
                     'https://www.instagram.com/thy_taipei/',
                     'https://www.instagram.com/explore/locations/112178280621907/thy/'
                     ])
    
    writer.writerow(['HANKO 60 如醉如夢',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.650011315444!2d121.5030253140529!3d25.045948843968457!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a90f2eaea327%3A0x7f821b508bbfa0d!2zSEFOS08gNjAg5aaC6YaJ5aaC5aSi!5e0!3m2!1szh-TW!2stw!4v1627140048290!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.650011315444!2d121.5030253140529!3d25.045948843968457!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a90f2eaea327%3A0x7f821b508bbfa0d!2zSEFOS08gNjAg5aaC6YaJ5aaC5aSi!5e0!3m2!1szh-TW!2stw!4v1627140048290!5m2!1szh-TW!2stw',
                     '25.046012023874898',
                     '121.5052354543471',
                     'https://www.instagram.com/barhanko60/?hl=zh-tw',
                     'https://www.instagram.com/explore/locations/353192685424022/'
                     ])
    
    writer.writerow(['THE KEY COMPANY 鑰匙行',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.72799043499!2d121.55074281405285!3d25.043303544074547!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc438c17e37%3A0xf71b1501f1d5b7d8!2zVEhFIEtFWSBDT01QQU5ZIOmRsOWMmeihjA!5e0!3m2!1szh-TW!2stw!4v1627140430538!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.72799043499!2d121.55074281405285!3d25.043303544074547!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc438c17e37%3A0xf71b1501f1d5b7d8!2zVEhFIEtFWSBDT01QQU5ZIOmRsOWMmeihjA!5e0!3m2!1szh-TW!2stw!4v1627140430538!5m2!1szh-TW!2stw',
                     '25.043347284956834',
                     '121.55296368307023',
                     'https://www.instagram.com/thekeycompany.taipei/',
                     'https://www.instagram.com/explore/locations/372358969851098/the-key-company/?utm_source=ig_embed&ig_rid=358ee082-d112-43ef-b670-377db51229e5'
                     ])
    
    writer.writerow(['BAR PUN',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.0426215263806!2d121.5558771!3d25.032627599999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcbc14e34bd%3A0xfaa10e154b46672a!2sBAR%20PUN!5e0!3m2!1szh-TW!2stw!4v1627140522896!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.0426215263806!2d121.5558771!3d25.032627599999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcbc14e34bd%3A0xfaa10e154b46672a!2sBAR%20PUN!5e0!3m2!1szh-TW!2stw!4v1627140522896!5m2!1szh-TW!2stw',
                     '25.03271022884498',
                     '121.55592001534332',
                     'https://www.instagram.com/bar_pun/',
                     'https://www.instagram.com/explore/locations/125431401484672/pun/?utm_source=ig_embed&ig_rid=5f780206-44a5-4922-9570-dd862d5192dd'
                     ])
    
    writer.writerow(['MUD Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3590154381654!2d121.52093741405317!3d25.055818043572582!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a968157bf3a9%3A0xb0e76091633e3915!2sMUD%20Bar!5e0!3m2!1szh-TW!2stw!4v1627140650841!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3590154381654!2d121.52093741405317!3d25.055818043572582!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a968157bf3a9%3A0xb0e76091633e3915!2sMUD%20Bar!5e0!3m2!1szh-TW!2stw!4v1627140650841!5m2!1szh-TW!2stw',
                     '25.055861779990007',
                     '121.52314755423471',
                     'https://www.instagram.com/mud.taipei/',
                     'https://www.instagram.com/explore/locations/973964538/mud-at-amba-taipei-zhongshan/?utm_source=ig_embed&ig_rid=adca32b4-68cc-4579-84ba-1546878b1825'
                     ])
    
    writer.writerow(['桂公子',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.288759597256!2d121.52382651405314!3d25.05820024347708!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9fa8ce9b5bf%3A0xa84d50bf52f9c20d!2z5qGC5YWs5a2Q6YWS6aSoIEhpZ2hiYWxsZXIncyBCYXI!5e0!3m2!1szh-TW!2stw!4v1627140834061!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.288759597256!2d121.52382651405314!3d25.05820024347708!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9fa8ce9b5bf%3A0xa84d50bf52f9c20d!2z5qGC5YWs5a2Q6YWS6aSoIEhpZ2hiYWxsZXIncyBCYXI!5e0!3m2!1szh-TW!2stw!4v1627140834061!5m2!1szh-TW!2stw',
                     '25.058195383968627',
                     '121.52600446783823',
                     'https://www.instagram.com/w29556412/',
                     'https://www.instagram.com/explore/locations/423846264791279/?utm_source=ig_embed&ig_rid=1175d19a-f7d0-4b35-9be7-d56967ef1134'
                     ])
    
    writer.writerow(['Ounce Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.023441113732!2d121.55367171405257!3d25.03327854447646!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcd1fbd2c2f%3A0xeb1fe4b16f0cf9ac!2sOunce!5e0!3m2!1szh-TW!2stw!4v1627140973886!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.023441113732!2d121.55367171405257!3d25.03327854447646!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcd1fbd2c2f%3A0xeb1fe4b16f0cf9ac!2sOunce!5e0!3m2!1szh-TW!2stw!4v1627140973886!5m2!1szh-TW!2stw',
                     '25.033293125964025',
                     '121.55588185423413',
                     'https://www.instagram.com/ouncetaipei/',
                     'https://www.instagram.com/explore/locations/46630093/ounce-taipei/?utm_source=ig_embed&ig_rid=784040e2-d278-46cd-b028-788a3f247a7d'
                     ])
    
    writer.writerow(['R SQUARED Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.91756902956!2d121.55694041405263!3d25.03687134433246!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abb2ec733ad7%3A0x713db996ceb4e8df!2sR%20SQUARED%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627141114751!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.91756902956!2d121.55694041405263!3d25.03687134433246!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abb2ec733ad7%3A0x713db996ceb4e8df!2sR%20SQUARED%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627141114751!5m2!1szh-TW!2stw',
                     '25.03690536680428',
                     '121.55911836783774',
                     'https://www.instagram.com/rsquared_taipei/',
                     'https://www.instagram.com/explore/locations/300844860708207/r-squared-taipei/'
                     ])
    
    writer.writerow(['Intention',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.794290060624!2d121.54711031405279!3d25.04105424416471!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc6936939e9%3A0xb745daae8ef9ecb9!2sIntention!5e0!3m2!1szh-TW!2stw!4v1627141236900!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.794290060624!2d121.54711031405279!3d25.04105424416471!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc6936939e9%3A0xb745daae8ef9ecb9!2sIntention!5e0!3m2!1szh-TW!2stw!4v1627141236900!5m2!1szh-TW!2stw',
                     '25.0411077062215',
                     '121.54932045434701',
                     'https://www.instagram.com/intention.__/',
                     'https://www.instagram.com/explore/locations/294856158/intention/'
                     ])
    
    writer.writerow(['洞香春',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.2705915089496!2d121.54452421405321!3d25.058816243452245!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab53c57f9427%3A0x4976160f100fed4b!2z5rSe6aaZ5pilLemFkuWQp-aOqOiWpiDlupfkuK3lupfphZLlkKcgc3BlYWtlYXN5IOeEoemFkuWWruiqv-mFkiDmt7HlpJzpo5_loIIg6YWS5ZCn5bCP6YWM6IGa5pyDIOeJueiJsumFkuWQpw!5e0!3m2!1szh-TW!2stw!4v1627141347079!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.2705915089496!2d121.54452421405321!3d25.058816243452245!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab53c57f9427%3A0x4976160f100fed4b!2z5rSe6aaZ5pilLemFkuWQp-aOqOiWpiDlupfkuK3lupfphZLlkKcgc3BlYWtlYXN5IOeEoemFkuWWruiqv-mFkiDmt7HlpJzpo5_loIIg6YWS5ZCn5bCP6YWM6IGa5pyDIOeJueiJsumFkuWQpw!5e0!3m2!1szh-TW!2stw!4v1627141347079!5m2!1szh-TW!2stw',
                     '25.058869697763647',
                     '121.54670216783829',
                     'https://www.instagram.com/dong.taipei/',
                     'https://www.instagram.com/explore/locations/813282772213180/'
                     ])
    
    writer.writerow(['父母-FuMu',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.349298196705!2d121.54150091405316!3d25.056147543559415!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab1ad7091bd7%3A0xd260d6c087881674!2z54i25q-NIC0gRnVNdQ!5e0!3m2!1szh-TW!2stw!4v1627141489975!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.349298196705!2d121.54150091405316!3d25.056147543559415!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab1ad7091bd7%3A0xd260d6c087881674!2z54i25q-NIC0gRnVNdQ!5e0!3m2!1szh-TW!2stw!4v1627141489975!5m2!1szh-TW!2stw',
                     '25.056162122327752',
                     '121.54366813900185',
                     'https://www.instagram.com/fumu_taipei/',
                     'https://www.instagram.com/explore/locations/448159845753064/-fumu/'
                     ])
    
    writer.writerow(['ABV Bar & Kitchen 閣樓餐酒館',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.7322521049587!2d121.45800649999998!3d25.0092124!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a93fabbf8ab3%3A0x50fb47b8d84e5d01!2zQUJWIEJhciAmIEtpdGNoZW4g6Zaj5qiT6aSQ6YWS6aSoLemgguaok-aZr-ingOmkkOW7sy3nvqnlpKfliKnpurUg5q2Q6Zm45paZ55CGKOadv-api-W6nOS4reW6lyk!5e0!3m2!1szh-TW!2stw!4v1627175106490!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.7322521049587!2d121.45800649999998!3d25.0092124!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a93fabbf8ab3%3A0x50fb47b8d84e5d01!2zQUJWIEJhciAmIEtpdGNoZW4g6Zaj5qiT6aSQ6YWS6aSoLemgguaok-aZr-ingOmkkOW7sy3nvqnlpKfliKnpurUg5q2Q6Zm45paZ55CGKOadv-api-W6nOS4reW6lyk!5e0!3m2!1szh-TW!2stw!4v1627175106490!5m2!1szh-TW!2stw',
                     '25.00924643013938',
                     '121.45798504232833',
                     'https://www.instagram.com/abv_penthouse/',
                     'https://www.instagram.com/explore/locations/175713386650351/abv/'
                     ])
    
    writer.writerow(['ABV Bar & Kitchen 日式居酒館',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.4173972828708!2d121.52431829999999!3d25.0538383!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9ee283f9b1b%3A0xff1cc963f0e15a06!2zQUJWIEJhciAmIEtpdGNoZW4g5pel5byP5bGF6YWS6aSoICjlj7DljJfkuK3lsbHlupcpIOWuteWknC_lsYXphZLlsYs!5e0!3m2!1szh-TW!2stw!4v1627175326274!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.4173972828708!2d121.52431829999999!3d25.0538383!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9ee283f9b1b%3A0xff1cc963f0e15a06!2zQUJWIEJhciAmIEtpdGNoZW4g5pel5byP5bGF6YWS6aSoICjlj7DljJfkuK3lsbHlupcpIOWuteWknC_lsYXphZLlsYs!5e0!3m2!1szh-TW!2stw!4v1627175326274!5m2!1szh-TW!2stw',
                     '25.053882037123866',
                     '121.52432902883581',
                     'https://www.instagram.com/abv_japanese/',
                     'https://www.instagram.com/explore/locations/684840528645013/abv-/'
                     ])
    
    writer.writerow(['ABV Bar & Kitchen 地中海餐酒館',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8211332720853!2d121.55568079999999!3d25.040143499999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc63e49ca85%3A0x78ccfabf9901bdfe!2zQUJWIEJhciAmIEtpdGNoZW4g5Zyw5Lit5rW36aSQ6YWS6aSoLeeyvumHgEJlZXLppJDlu7M!5e0!3m2!1szh-TW!2stw!4v1627175410977!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8211332720853!2d121.55568079999999!3d25.040143499999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc63e49ca85%3A0x78ccfabf9901bdfe!2zQUJWIEJhciAmIEtpdGNoZW4g5Zyw5Lit5rW36aSQ6YWS6aSoLeeyvumHgEJlZXLppJDlu7M!5e0!3m2!1szh-TW!2stw!4v1627175410977!5m2!1szh-TW!2stw',
                     '25.04020668289745',
                     '121.55565934232833',
                     'https://www.instagram.com/abv_mediterranean/',
                     'https://www.instagram.com/explore/locations/500953733448743/abv-/'
                     ])
    
    writer.writerow(['ABV Bar & Kitchen 美式餐酒館',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8133109848645!2d121.54767919999998!3d25.04040890000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab978c8cd485%3A0xc07ee88bac917338!2zQUJWIEJhciAmIEtpdGNoZW7nvo7lvI_ppJDphZLppKgg576O5byP54Ok6IKJIOa8ouWgoSDniZvmjpIg6YSJ5p2R6I-cIOe-juW8j-mkkOW7sw!5e0!3m2!1szh-TW!2stw!4v1627175482962!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8133109848645!2d121.54767919999998!3d25.04040890000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab978c8cd485%3A0xc07ee88bac917338!2zQUJWIEJhciAmIEtpdGNoZW7nvo7lvI_ppJDphZLppKgg576O5byP54Ok6IKJIOa8ouWgoSDniZvmjpIg6YSJ5p2R6I-cIOe-juW8j-mkkOW7sw!5e0!3m2!1szh-TW!2stw!4v1627175482962!5m2!1szh-TW!2stw',
                     '25.040549846113855',
                     '121.54770065767168',
                     'https://www.instagram.com/abv_americano/',
                     'https://www.instagram.com/explore/locations/110159867432029/abv-/'
                     ])
    
    writer.writerow(['ABV Bar & Kitchen 加勒比海餐酒館',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8111328737527!2d121.55242229999996!3d25.04048279999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc5e5cc8e03%3A0xa58081d43316cce4!2zQUJWIEJhciAmIEtpdGNoZW4g5Yqg5YuS5q-U5rW36aSQ6YWS6aSo!5e0!3m2!1szh-TW!2stw!4v1627175561079!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8111328737527!2d121.55242229999996!3d25.04048279999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc5e5cc8e03%3A0xa58081d43316cce4!2zQUJWIEJhciAmIEtpdGNoZW4g5Yqg5YuS5q-U5rW36aSQ6YWS6aSo!5e0!3m2!1szh-TW!2stw!4v1627175561079!5m2!1szh-TW!2stw',
                     '25.040429337670776',
                     '121.5524544865075',
                     'https://www.instagram.com/abv_caribbean/',
                     'https://www.instagram.com/explore/locations/119203283245120/abv/'
                     ])
    
    writer.writerow(['當吧 PAWN BAR',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.5608871281015!2d121.52573939999999!3d25.048971899999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a96e5f837b7b%3A0x8a40214ca3b017a!2z55W25ZCnUEFXTiBCQVI!5e0!3m2!1szh-TW!2stw!4v1627175625436!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.5608871281015!2d121.52573939999999!3d25.048971899999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a96e5f837b7b%3A0x8a40214ca3b017a!2z55W25ZCnUEFXTiBCQVI!5e0!3m2!1szh-TW!2stw!4v1627175625436!5m2!1szh-TW!2stw',
                     '25.04900591911486',
                     '121.52575012883581',
                     'https://www.instagram.com/pawn_bar/',
                     'https://www.instagram.com/explore/locations/103520627782731/pawn-bar/'
                     ])
    
    writer.writerow(['純愛小吃部 Pure Love Diner Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.5966691984286!2d121.53346139999998!3d25.013817499999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a94b8f511db1%3A0xcb82d23c7932000a!2z57SU5oSb5bCP5ZCD6YOoIFB1cmUgTG92ZSBEaW5lciBCYXI!5e0!3m2!1szh-TW!2stw!4v1627175698440!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.5966691984286!2d121.53346139999998!3d25.013817499999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a94b8f511db1%3A0xcb82d23c7932000a!2z57SU5oSb5bCP5ZCD6YOoIFB1cmUgTG92ZSBEaW5lciBCYXI!5e0!3m2!1szh-TW!2stw!4v1627175698440!5m2!1szh-TW!2stw',
                     '25.013861251393966',
                     '121.5334292134925',
                     'https://www.instagram.com/purelovetw/',
                     'https://www.instagram.com/explore/locations/100531845329695/'
                     ])
    
    writer.writerow(['89 LOOP Sports Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.622255999877!2d121.53582269999997!3d25.012948500000014!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9903cded679%3A0x311d66c8382317ad!2zODkgTE9PUCBTcG9ydHMgQmFy576O5byP6aSQ6YWS6aSo!5e0!3m2!1szh-TW!2stw!4v1627175781817!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.622255999877!2d121.53582269999997!3d25.012948500000014!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9903cded679%3A0x311d66c8382317ad!2zODkgTE9PUCBTcG9ydHMgQmFy576O5byP6aSQ6YWS6aSo!5e0!3m2!1szh-TW!2stw!4v1627175781817!5m2!1szh-TW!2stw',
                     '25.013011696900183',
                     '121.53580124232832',
                     'https://www.instagram.com/89_loop/',
                     'https://www.instagram.com/explore/locations/548405882207570/89-loop/'
                     ])
    
    writer.writerow(['Vine Bar 藤蔓老屋',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.9581875529802!2d121.55717670000001!3d25.035493000000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc9a8f94619%3A0x1fb5ef08e4952e46!2zVmluZSBCYXIg6Jek6JST6ICB5bGL!5e0!3m2!1szh-TW!2stw!4v1627175993633!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.9581875529802!2d121.55717670000001!3d25.035493000000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abc9a8f94619%3A0x1fb5ef08e4952e46!2zVmluZSBCYXIg6Jek6JST6ICB5bGL!5e0!3m2!1szh-TW!2stw!4v1627175993633!5m2!1szh-TW!2stw',
                     '25.035517302039622',
                     '121.5571767',
                     'https://www.instagram.com/vinebar.taipei/',
                     'https://www.instagram.com/explore/locations/1470774846345770/vine-bar/'
                     ])
    
    writer.writerow(['Babylon Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.963580235182!2d121.56606650000002!3d25.035309999999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab15a57dd415%3A0xd309ac1f8d22331!2sBabylon%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627176054257!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.963580235182!2d121.56606650000002!3d25.035309999999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab15a57dd415%3A0xd309ac1f8d22331!2sBabylon%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627176054257!5m2!1szh-TW!2stw',
                     '25.035353743733115',
                     '121.56605577116417',
                     'https://www.instagram.com/babylon_taipei/',
                     'https://www.instagram.com/explore/locations/111360120743196/babylon-taipei/'
                     ])
    
    writer.writerow(['COYA 克亞',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.9869775658135!2d121.57611099999998!3d25.03451599999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aba5f73201c5%3A0x8d7e78f9e32ba098!2zQ09ZQSDlhYvkup4!5e0!3m2!1szh-TW!2stw!4v1627176127286!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.9869775658135!2d121.57611099999998!3d25.03451599999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aba5f73201c5%3A0x8d7e78f9e32ba098!2zQ09ZQSDlhYvkup4!5e0!3m2!1szh-TW!2stw!4v1627176127286!5m2!1szh-TW!2stw',
                     '25.03453058134048',
                     '121.57612172883583',
                     'https://www.instagram.com/coya_taipei/',
                     'https://www.instagram.com/explore/locations/108696931279578/coya-taipei/'
                     ])
    
    writer.writerow(['Costa Blanca Taipei',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.963580235182!2d121.56606649999998!3d25.035309999999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab55edaf75e5%3A0x14b1bbad55d7f289!2sCosta%20Blanca%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627176186018!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.963580235182!2d121.56606649999998!3d25.035309999999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab55edaf75e5%3A0x14b1bbad55d7f289!2sCosta%20Blanca%20Taipei!5e0!3m2!1szh-TW!2stw!4v1627176186018!5m2!1szh-TW!2stw',
                     '25.035344022904887',
                     '121.56608795767167',
                     'https://www.instagram.com/costablanca.att/',
                     'https://www.instagram.com/explore/locations/100892178498577/costa-blanca-taipei/'
                     ])
    
    writer.writerow(['Wonder.land 仙境',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3612.9565298523835!2d121.54097240000002!3d25.1033328!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442adf14c141453%3A0x85cb9d464a5d707!2zV29uZGVyLmxhbmQg5LuZ5aKD!5e0!3m2!1szh-TW!2stw!4v1627176261699!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3612.9565298523835!2d121.54097240000002!3d25.1033328!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442adf14c141453%3A0x85cb9d464a5d707!2zV29uZGVyLmxhbmQg5LuZ5aKD!5e0!3m2!1szh-TW!2stw!4v1627176261699!5m2!1szh-TW!2stw',
                     '25.103318226847755',
                     '121.54101531534333',
                     'https://www.instagram.com/drunk_land/',
                     'https://www.instagram.com/explore/locations/106692377877214/wonderland/'
                     ])
    
    writer.writerow(['INDULGE Bistro',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8509332947456!2d121.54477679999998!3d25.039132400000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abd0e2e035e5%3A0x819af3bd78283034!2zSU5EVUxHRSBCaXN0cm8gKOWvpumpl-WJteaWsOmkkOmFkumkqCk!5e0!3m2!1szh-TW!2stw!4v1627176332622!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8509332947456!2d121.54477679999998!3d25.039132400000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abd0e2e035e5%3A0x819af3bd78283034!2zSU5EVUxHRSBCaXN0cm8gKOWvpumpl-WJteaWsOmkkOmFkumkqCk!5e0!3m2!1szh-TW!2stw!4v1627176332622!5m2!1szh-TW!2stw',
                     '25.039127539735706',
                     '121.54475534232832',
                     'https://www.instagram.com/indulgebistro/',
                     'https://www.instagram.com/explore/locations/146378112089210/indulge-bistro/'
                     ])
    
    writer.writerow(['Staff Only Club',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.6317838528853!2d121.52789680000001!3d25.0126249!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9b7965fe7ef%3A0x6b0b7a5af651b8bd!2sStaff%20Only%20Club!5e0!3m2!1szh-TW!2stw!4v1627176518606!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.6317838528853!2d121.52789680000001!3d25.0126249!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9b7965fe7ef%3A0x6b0b7a5af651b8bd!2sStaff%20Only%20Club!5e0!3m2!1szh-TW!2stw!4v1627176518606!5m2!1szh-TW!2stw',
                     '25.012639483941367',
                     '121.52788607116418',
                     'https://www.instagram.com/staffonlyclub_taipei/',
                     'https://www.instagram.com/explore/locations/202853286975074/staff-only-club/'
                     ])
    
    writer.writerow(['Café The Misanthrope Society 厭世會社',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.5583757744107!2d121.53328700000002!3d25.015118000000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a983e08d732d%3A0x95a886bb2a989a48!2zQ2Fmw6kgVGhlIE1pc2FudGhyb3BlIFNvY2lldHkg5Y6t5LiW5pyD56S-!5e0!3m2!1szh-TW!2stw!4v1627176583518!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.5583757744107!2d121.53328700000002!3d25.015118000000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a983e08d732d%3A0x95a886bb2a989a48!2zQ2Fmw6kgVGhlIE1pc2FudGhyb3BlIFNvY2lldHkg5Y6t5LiW5pyD56S-!5e0!3m2!1szh-TW!2stw!4v1627176583518!5m2!1szh-TW!2stw',
                     '25.01513258364525',
                     '121.5333191865075',
                     'https://www.instagram.com/mis.society/',
                     'https://www.instagram.com/explore/locations/341963129939698/the-misanthrope-society/'
                     ])
    
    writer.writerow(['軍火庫精釀啤酒專門店 BeerAmmo Craft Beer',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.4156574588965!2d121.5156252!3d25.0538973!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a96b60972abf%3A0x4851704120d44a7e!2z6LuN54Gr5bqr57K-6YeA5ZWk6YWS5bCI6ZaA5bqXIEJlZXJBbW1vIENyYWZ0IEJlZXI!5e0!3m2!1szh-TW!2stw!4v1627176751841!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.4156574588965!2d121.5156252!3d25.0538973!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a96b60972abf%3A0x4851704120d44a7e!2z6LuN54Gr5bqr57K-6YeA5ZWk6YWS5bCI6ZaA5bqXIEJlZXJBbW1vIENyYWZ0IEJlZXI!5e0!3m2!1szh-TW!2stw!4v1627176751841!5m2!1szh-TW!2stw',
                     '25.053941037102827',
                     '121.51563592883582',
                     'https://www.instagram.com/beerammo_anno2016/',
                     'https://www.instagram.com/explore/locations/313861018982234/beerammo/'
                     ])

    writer.writerow(['OriginBAR 源',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.469714063466!2d121.5563713!3d25.0520641!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abea4d5bcac7%3A0x8f49dcd3272fe20!2zT3JpZ2luQkFSIOa6kA!5e0!3m2!1szh-TW!2stw!4v1627176812374!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.469714063466!2d121.5563713!3d25.0520641!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abea4d5bcac7%3A0x8f49dcd3272fe20!2zT3JpZ2luQkFSIOa6kA!5e0!3m2!1szh-TW!2stw!4v1627176812374!5m2!1szh-TW!2stw',
                     '25.05213699625292',
                     '121.5563713',
                     'https://www.instagram.com/originbar_yuan/',
                     'https://www.instagram.com/explore/locations/226646467758293/originbar/'
                     ])             
    
    writer.writerow(['Nite Nite 酒鈅酒',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.216258233665!2d121.54368579999999!3d25.026733999999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab1f8bed705d%3A0x52308050a61f324e!2zTml0ZSBOaXRlIOmFkumIhemFkiBCaXN0cm8gQmFyLeWkp-WuiemFkuWQp-aOqOiWpiDnp5HmioDlpKfmqJPphZLlkKcg5o6o6Jam6aSQ6YWS6aSoIOWgtOWcsOenn-WAnyDlk4HphZLphZLlkKcg6IGa5pyD5YyF5buC!5e0!3m2!1szh-TW!2stw!4v1627177093174!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.216258233665!2d121.54368579999999!3d25.026733999999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab1f8bed705d%3A0x52308050a61f324e!2zTml0ZSBOaXRlIOmFkumIhemFkiBCaXN0cm8gQmFyLeWkp-WuiemFkuWQp-aOqOiWpiDnp5HmioDlpKfmqJPphZLlkKcg5o6o6Jam6aSQ6YWS6aSoIOWgtOWcsOenn-WAnyDlk4HphZLphZLlkKcg6IGa5pyD5YyF5buC!5e0!3m2!1szh-TW!2stw!4v1627177093174!5m2!1szh-TW!2stw',
                     '25.026758303774525',
                     '121.54362142698501',
                     'https://www.instagram.com/nitenite_bar/',
                     'https://www.instagram.com/explore/locations/102691961105537/nite-nite-bar/'
                     ])
    
    writer.writerow(['Circle Gallery Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.114208446927!2d121.55974551405255!3d25.030197944599866!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abb5a5390499%3A0xb4408822e09a5d03!2zMTEw5Y-w5YyX5biC5L-h576p5Y2A6I6K5pWs6LevMjIz6Jmf!5e0!3m2!1szh-TW!2stw!4v1627177309223!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.114208446927!2d121.55974551405255!3d25.030197944599866!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abb5a5390499%3A0xb4408822e09a5d03!2zMTEw5Y-w5YyX5biC5L-h576p5Y2A6I6K5pWs6LevMjIz6Jmf!5e0!3m2!1szh-TW!2stw!4v1627177309223!5m2!1szh-TW!2stw',
                     '25.030280575081086',
                     '121.56194492539825',
                     'https://www.instagram.com/circle_gallery_bar_/',
                     'https://www.instagram.com/explore/locations/102397141893806/circle-gallery-bar/'
                     ])
    
    writer.writerow(['北緯二十五',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.876423489921!2d121.56817670000002!3d25.0382675!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abba545c9cc7%3A0x9a691d982bf6f879!2z5YyX57ev5LqM5Y2B5LqU!5e0!3m2!1szh-TW!2stw!4v1627177378352!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.876423489921!2d121.56817670000002!3d25.0382675!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abba545c9cc7%3A0x9a691d982bf6f879!2z5YyX57ev5LqM5Y2B5LqU!5e0!3m2!1szh-TW!2stw!4v1627177378352!5m2!1szh-TW!2stw',
                     '25.038311242678443',
                     '121.56829471719415',
                     'https://www.instagram.com/lemeridientaipei/',
                     'https://www.instagram.com/explore/locations/2072400786377724/'
                     ])
    
    writer.writerow(['AHA Saloon',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.151508376263!2d121.5432764!3d25.0289319!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aa2c86670c71%3A0x726d400c28de3aa5!2sAHA%20Saloon!5e0!3m2!1szh-TW!2stw!4v1627177492172!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.151508376263!2d121.5432764!3d25.0289319!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aa2c86670c71%3A0x726d400c28de3aa5!2sAHA%20Saloon!5e0!3m2!1szh-TW!2stw!4v1627177492172!5m2!1szh-TW!2stw',
                     '25.028975646007183',
                     '121.54334077301499',
                     'https://www.instagram.com/ahasaloon/',
                     'https://www.instagram.com/explore/locations/158767408019259/aha-saloon/'
                     ])
    
    writer.writerow(['Tickle My Fantasy',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.0439314133237!2d121.55006211405257!3d25.032583144504382!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcc44cf26c9%3A0xad9c63c93e339691!2sTickle%20my%20fantasy!5e0!3m2!1szh-TW!2stw!4v1627177633239!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.0439314133237!2d121.55006211405257!3d25.032583144504382!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcc44cf26c9%3A0xad9c63c93e339691!2sTickle%20my%20fantasy!5e0!3m2!1szh-TW!2stw!4v1627177633239!5m2!1szh-TW!2stw',
                     '25.03258800502797',
                     '121.55226152539828',
                     'https://www.instagram.com/explore/locations/761433003/tickle-my-fantasy/',
                     'https://www.instagram.com/explore/locations/761433003/tickle-my-fantasy/'
                     ])
    
    writer.writerow(['Bittersweet Bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.649308205964!2d121.53572650000001!3d25.0120297!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcd1f6baaf5%3A0x5f3107cfcd9e00d2!2sBittersweet%20Bar!5e0!3m2!1szh-TW!2stw!4v1627177694523!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.649308205964!2d121.53572650000001!3d25.0120297!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abcd1f6baaf5%3A0x5f3107cfcd9e00d2!2sBittersweet%20Bar!5e0!3m2!1szh-TW!2stw!4v1627177694523!5m2!1szh-TW!2stw',
                     '25.01207345203094',
                     '121.53569431349251',
                     'https://www.instagram.com/bittersweettaipei/',
                     'https://www.instagram.com/explore/locations/514989512296961/bittersweet-bar/'
                     ])
    
    writer.writerow(['渣男 Taiwan Bistro 信義一渣',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.2096139592613!2d121.56657621405245!3d25.026959544729657!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abb2e680ed73%3A0xd97a03e137aee0d0!2z5rij55S3IFRhaXdhbiBCaXN0cm8g5L-h576p5LiA5rij!5e0!3m2!1szh-TW!2stw!4v1627179539630!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.2096139592613!2d121.56657621405245!3d25.026959544729657!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abb2e680ed73%3A0xd97a03e137aee0d0!2z5rij55S3IFRhaXdhbiBCaXN0cm8g5L-h576p5LiA5rij!5e0!3m2!1szh-TW!2stw!4v1627179539630!5m2!1szh-TW!2stw',
                     '25.026896355009477',
                     '121.56880781201941',
                     'https://www.instagram.com/zhananbistro/',
                     'https://www.instagram.com/explore/locations/1027861995/taiwan-bistro/'
                     ])
    
    writer.writerow(['渣男 Taiwan Bistro 木柵二渣',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3616.0479805286045!2d121.56830281405178!3d24.998485545870334!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aa68b2adc2ef%3A0x994c821502530140!2z5rij55S3IFRhaXdhbiBCaXN0cm8g5pyo5p-15LqM5rij!5e0!3m2!1szh-TW!2stw!4v1627179601002!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3616.0479805286045!2d121.56830281405178!3d24.998485545870334!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aa68b2adc2ef%3A0x994c821502530140!2z5rij55S3IFRhaXdhbiBCaXN0cm8g5pyo5p-15LqM5rij!5e0!3m2!1szh-TW!2stw!4v1627179601002!5m2!1szh-TW!2stw',
                     '24.99850985523625',
                     '121.57048076783686',
                     'https://www.instagram.com/zhananbistro/',
                     'https://www.instagram.com/explore/locations/1728395554090734/taiwan-bistro/'
                     ])
    
    writer.writerow(['渣男 Taiwan Bistro 南京三渣',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.464885810432!2d121.55456131405305!3d25.052227843716622!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abebab7cb0e9%3A0x18f2787d3a6c29d7!2z5rij55S3IFRhaXdhbiBCaXN0cm8g5Y2X5Lqs5LiJ5rij!5e0!3m2!1szh-TW!2stw!4v1627179651502!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.464885810432!2d121.55456131405305!3d25.052227843716622!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abebab7cb0e9%3A0x18f2787d3a6c29d7!2z5rij55S3IFRhaXdhbiBCaXN0cm8g5Y2X5Lqs5LiJ5rij!5e0!3m2!1szh-TW!2stw!4v1627179651502!5m2!1szh-TW!2stw',
                     '25.05227158141516',
                     '121.55678218318364',
                     'https://www.instagram.com/zhananbistro/',
                     'https://www.instagram.com/explore/locations/125304464740611/taiwan-bistro/'
                     ])
    
    writer.writerow(['渣男 Taiwan Bistro 古亭四渣',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.2283083625193!2d121.51719301405245!3d25.02632494475512!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9fca5cf5f71%3A0xdf4bd899d6f82a91!2z5rij55S3VGFpd2FuIEJpc3Ryb-OAiuWPpOS6reWbm-a4o-OAiw!5e0!3m2!1szh-TW!2stw!4v1627179713771!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.2283083625193!2d121.51719301405245!3d25.02632494475512!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9fca5cf5f71%3A0xdf4bd899d6f82a91!2z5rij55S3VGFpd2FuIEJpc3Ryb-OAiuWPpOS6reWbm-a4o-OAiw!5e0!3m2!1szh-TW!2stw!4v1627179713771!5m2!1szh-TW!2stw',
                     '25.0263298055266',
                     '121.5193924255103',
                     'https://www.instagram.com/zhananbistro/',
                     'https://www.instagram.com/explore/locations/677756669242898/taiwan-bistro/'
                     ])
    
    writer.writerow(['渣男 Taiwan Bistro 中山五渣',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3710328021075!2d121.51578271405322!3d25.055410543588863!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a90175ad2017%3A0xfb40cf5a5fccd8e1!2z5rij55S3VGFpd2FuIEJpc3RybyDkuK3lsbHlupc!5e0!3m2!1szh-TW!2stw!4v1627179780985!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.3710328021075!2d121.51578271405322!3d25.055410543588863!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a90175ad2017%3A0xfb40cf5a5fccd8e1!2z5rij55S3VGFpd2FuIEJpc3RybyDkuK3lsbHlupc!5e0!3m2!1szh-TW!2stw!4v1627179780985!5m2!1szh-TW!2stw',
                     '25.055434841681258',
                     '121.51800358318378',
                     'https://www.instagram.com/zhananbistro/',
                     'https://www.instagram.com/explore/locations/2250651798585062/taiwan-bistro/'
                     ])

    writer.writerow(['渣男 Taiwan Bistro 天母八渣',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3612.9877549486646!2d121.52186231405426!3d25.10227584170707!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442af53b8decf63%3A0x70504bdbb2e07959!2z5rij55S3VGFpd2FuIEJpc3Ryb-OAiuWkqeavjeWFq-a4o-OAiw!5e0!3m2!1szh-TW!2stw!4v1627179842411!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3612.9877549486646!2d121.52186231405426!3d25.10227584170707!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442af53b8decf63%3A0x70504bdbb2e07959!2z5rij55S3VGFpd2FuIEJpc3Ryb-OAiuWkqeavjeWFq-a4o-OAiw!5e0!3m2!1szh-TW!2stw!4v1627179842411!5m2!1szh-TW!2stw',
                     '25.102300130500197',
                     '121.52408318318486',
                     'https://www.instagram.com/zhananbistro/',
                     'https://www.instagram.com/explore/locations/104307428420761/taiwan-bistro/'
                     ])

    writer.writerow(['童裏心柑仔店ÖMAR放感情',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.749226614405!2d121.55317760000004!3d25.0425831!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a99454e0a469%3A0xb9f377b1fbfe7b4c!2z56ul6KOP5b-D5p-R5LuU5bqXw5ZNQVLmlL7mhJ_mg4Ut54m56Imy6YWS5ZCnIOmkkOmFkumkqCDlubPlg7nphZLlkKcg57ay576O6YWS5ZCnIOS6uuawoyDmnIvlj4vogZrmnIMg55Sf5pel5oW255SfIGJhciDnibnoibLoqr_phZIg5Ym15oSP5paZ55CG!5e0!3m2!1szh-TW!2stw!4v1627138351791!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.749226614405!2d121.55317760000004!3d25.0425831!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a99454e0a469%3A0xb9f377b1fbfe7b4c!2z56ul6KOP5b-D5p-R5LuU5bqXw5ZNQVLmlL7mhJ_mg4Ut54m56Imy6YWS5ZCnIOmkkOmFkumkqCDlubPlg7nphZLlkKcg57ay576O6YWS5ZCnIOS6uuawoyDmnIvlj4vogZrmnIMg55Sf5pel5oW255SfIGJhciDnibnoibLoqr_phZIg5Ym15oSP5paZ55CG!5e0!3m2!1szh-TW!2stw!4v1627138351791!5m2!1szh-TW!2stw',
                     '25.04262684113926',
                     '121.55318832883586',
                     'https://www.instagram.com/tonglixin_omar/',
                     'https://www.instagram.com/explore/locations/111321643795012/omar/'
                     ])
    
    writer.writerow(['離城放感情',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.3478273165265!2d121.55254939999999!3d25.0222674!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab9f59485707%3A0x88744d5584602e8c!2z6Zui5Z-O5pS-5oSf5oOFLemkkOmFkumkqOaOqOiWpiDlubPlg7noqr_phZLphZLlkKcgYmFyIGJpc3RybyDkurrmsKPnibnoibLppJDphZLnvo7po5_mjqjolqYg57ay576O6YWS5ZCn!5e0!3m2!1szh-TW!2stw!4v1627470861991!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.3478273165265!2d121.55254939999999!3d25.0222674!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab9f59485707%3A0x88744d5584602e8c!2z6Zui5Z-O5pS-5oSf5oOFLemkkOmFkumkqOaOqOiWpiDlubPlg7noqr_phZLphZLlkKcgYmFyIGJpc3RybyDkurrmsKPnibnoibLppJDphZLnvo7po5_mjqjolqYg57ay576O6YWS5ZCn!5e0!3m2!1szh-TW!2stw!4v1627470861991!5m2!1szh-TW!2stw',
                     '25.022350035821063',
                     '121.55253867116332',
                     'https://www.instagram.com/leaving_city/',
                     'https://www.instagram.com/explore/locations/106488987369054/_/'])
    
    writer.writerow(['Odin信義放感情',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.1468888646964!2d121.55771460000004!3d25.02908869999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab355499b629%3A0xb41bde4da53b8c0!2zT2RpbuS_oee-qeaUvuaEn-aDhS3ppJDphZLppKjmjqjolqYg5bmz5YO56Kq_6YWS6YWS5ZCnIGJhciBiaXN0cm8g5Lq65rCj54m56Imy6aSQ6YWS576O6aOf5o6o6JamIOe2sue-jumFkuWQpw!5e0!3m2!1szh-TW!2stw!4v1627470940589!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.1468888646964!2d121.55771460000004!3d25.02908869999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab355499b629%3A0xb41bde4da53b8c0!2zT2RpbuS_oee-qeaUvuaEn-aDhS3ppJDphZLppKjmjqjolqYg5bmz5YO56Kq_6YWS6YWS5ZCnIGJhciBiaXN0cm8g5Lq65rCj54m56Imy6aSQ6YWS576O6aOf5o6o6JamIOe2sue-jumFkuWQpw!5e0!3m2!1szh-TW!2stw!4v1627470940589!5m2!1szh-TW!2stw',
                     '25.029074118012776',
                     '121.55776824418335',
                     'https://www.instagram.com/odin_xinyi/',
                     'https://www.instagram.com/explore/locations/2128688550724773/odin-bistro/'])
    
    writer.writerow(['Odin士林放感情',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3613.2819588811744!2d121.52541040000001!3d25.092315100000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aebb34f53bb9%3A0x512b60f5da825a80!2zT2RpbiDlo6vmnpfmlL7mhJ_mg4Ut6aSQ6YWS6aSo5o6o6JamIOW5s-WDueiqv-mFkumFkuWQpyBiYXIgYmlzdHJvIOS6uuawo-eJueiJsumkkOmFkue-jumjn-aOqOiWpiDntrLnvo7phZLlkKc!5e0!3m2!1szh-TW!2stw!4v1627471008094!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3613.2819588811744!2d121.52541040000001!3d25.092315100000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aebb34f53bb9%3A0x512b60f5da825a80!2zT2RpbiDlo6vmnpfmlL7mhJ_mg4Ut6aSQ6YWS6aSo5o6o6JamIOW5s-WDueiqv-mFkumFkuWQpyBiYXIgYmlzdHJvIOS6uuawo-eJueiJsumkkOmFkue-jumjn-aOqOiWpiDntrLnvo7phZLlkKc!5e0!3m2!1szh-TW!2stw!4v1627471008094!5m2!1szh-TW!2stw',
                     '25.092329674463148',
                     '121.52537821349',
                     'https://www.instagram.com/odin_shilin/',
                     'https://www.instagram.com/explore/locations/338918639782555/odin-bistro/'])
    
    writer.writerow(['Driftwood',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.6261100094357!2d121.50558149999999!3d25.046759599999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a90f275a74bb%3A0x29954039ef1af9de!2zRHJpZnR3b29kIOilv-mWgOeUug!5e0!3m2!1szh-TW!2stw!4v1627471079079!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.6261100094357!2d121.50558149999999!3d25.046759599999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a90f275a74bb%3A0x29954039ef1af9de!2zRHJpZnR3b29kIOilv-mWgOeUug!5e0!3m2!1szh-TW!2stw!4v1627471079079!5m2!1szh-TW!2stw',
                     '25.04686165915782',
                     '121.50562441534665',
                     'https://www.instagram.com/driftwoodxmd/',
                     'https://www.instagram.com/explore/locations/1264051633677830/driftwood/'])
    
    writer.writerow(['啜飲室 Landmark',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8180827661367!2d121.56677300000001!3d25.040246999999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abbbc0632e07%3A0x5836c1f514fd0ff4!2z5ZWc6aOy5a6kIExhbmRtYXJrIChDcmFmdCBCZWVyIFRhcHJvb20g57K-6YeA5ZWk6YWS5bCI6LOj5bqXKQ!5e0!3m2!1szh-TW!2stw!4v1627471143791!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.8180827661367!2d121.56677300000001!3d25.040246999999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abbbc0632e07%3A0x5836c1f514fd0ff4!2z5ZWc6aOy5a6kIExhbmRtYXJrIChDcmFmdCBCZWVyIFRhcHJvb20g57K-6YeA5ZWk6YWS5bCI6LOj5bqXKQ!5e0!3m2!1szh-TW!2stw!4v1627471143791!5m2!1szh-TW!2stw',
                     '25.04026158065922',
                     '121.56679445767334',
                     'https://www.instagram.com/cyslandmark/',
                     'https://www.instagram.com/explore/locations/1019630993/landmark/'])
    
    writer.writerow(['啜飲室大安 CYSDAAN',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.792764585234!2d121.54509900000001!3d25.041106!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abda52db9ac9%3A0xc9968e10e8f89c05!2z5ZWc6aOy5a6kIOWkp-WuiQ!5e0!3m2!1szh-TW!2stw!4v1627471235928!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.792764585234!2d121.54509900000001!3d25.041106!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abda52db9ac9%3A0xc9968e10e8f89c05!2z5ZWc6aOy5a6kIOWkp-WuiQ!5e0!3m2!1szh-TW!2stw!4v1627471235928!5m2!1szh-TW!2stw',
                     '25.041149741666125',
                     '121.54513118651002',
                     'https://www.instagram.com/cysdaan/',
                     'https://www.instagram.com/explore/locations/531516936/'])
    
    writer.writerow(['tei by OBOND',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.081623586171!2d121.5576814!3d25.031303899999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab997c16d655%3A0xfb7a47d5307c473d!2stei%20by%20OBOND!5e0!3m2!1szh-TW!2stw!4v1627471300823!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.081623586171!2d121.5576814!3d25.031303899999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab997c16d655%3A0xfb7a47d5307c473d!2stei%20by%20OBOND!5e0!3m2!1szh-TW!2stw!4v1627471300823!5m2!1szh-TW!2stw',
                     '25.031347645161503',
                     '121.55767067116334',
                     'https://www.instagram.com/tei_by_obond/',
                     'https://www.instagram.com/explore/locations/110075720824677/tei-by-obond/'])
    
    writer.writerow(['Mu:',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7541992196325!2d121.5465557!3d25.042414399999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab2a076faddd%3A0x2de10c0bbff06e84!2zTXU6!5e0!3m2!1szh-TW!2stw!4v1627471371944!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7541992196325!2d121.5465557!3d25.042414399999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab2a076faddd%3A0x2de10c0bbff06e84!2zTXU6!5e0!3m2!1szh-TW!2stw!4v1627471371944!5m2!1szh-TW!2stw',
                     '25.04253590329325',
                     '121.54658788651003',
                     'https://www.instagram.com/mu_taipei/',
                     'https://www.instagram.com/explore/locations/109379077209228/mu/'])
    
    writer.writerow(['Another Brick',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.432013402052!2d121.52833129999998!3d25.019409!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a98e7da16639%3A0xdf712be17d248f1a!2sAnother%20Brick!5e0!3m2!1szh-TW!2stw!4v1627471430830!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.432013402052!2d121.52833129999998!3d25.019409!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a98e7da16639%3A0xdf712be17d248f1a!2sAnother%20Brick!5e0!3m2!1szh-TW!2stw!4v1627471430830!5m2!1szh-TW!2stw',
                     '25.019433305224975',
                     '121.52834202883666',
                     'https://www.instagram.com/anotherbrick_taipei/',
                     'https://www.instagram.com/explore/locations/1706434736313396/another-brick/'])
    
    writer.writerow(['She_Design tapas soju bar',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.692544953801!2d121.566848!3d25.044506000000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab3fef4e4505%3A0x3526fc3925f58b3!2sShe_Design%20tapas%20soju%20bar!5e0!3m2!1szh-TW!2stw!4v1627471568827!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.692544953801!2d121.566848!3d25.044506000000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442ab3fef4e4505%3A0x3526fc3925f58b3!2sShe_Design%20tapas%20soju%20bar!5e0!3m2!1szh-TW!2stw!4v1627471568827!5m2!1szh-TW!2stw',
                     '25.044588620843278',
                     '121.56681581349',
                     'https://www.instagram.com/she_designbar/',
                     'https://www.instagram.com/explore/locations/339596970275482/she_design-tapas-soju-bar/'])

    writer.writerow(['Fourplay Cuisine',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.9382372550936!2d121.54693300000001!3d25.036170000000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abd1fa93a035%3A0x542a6f8ec84205e3!2sFourplay%20Cuisine!5e0!3m2!1szh-TW!2stw!4v1627471656338!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.9382372550936!2d121.54693300000001!3d25.036170000000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abd1fa93a035%3A0x542a6f8ec84205e3!2sFourplay%20Cuisine!5e0!3m2!1szh-TW!2stw!4v1627471656338!5m2!1szh-TW!2stw',
                     '25.03612625655799',
                     '121.54691154232668',
                     'https://www.instagram.com/fourplaytaipei/',
                     'https://www.instagram.com/explore/locations/959907725/fourplay/'])
    
    writer.writerow(['榕 RON',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3613.307328442255!2d121.52713299999998!3d25.091455999999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aea4e7dae6cd%3A0x96b286ba2ec98dcd!2z5qaVIFJPTg!5e0!3m2!1szh-TW!2stw!4v1627471753338!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3613.307328442255!2d121.52713299999998!3d25.091455999999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aea4e7dae6cd%3A0x96b286ba2ec98dcd!2z5qaVIFJPTg!5e0!3m2!1szh-TW!2stw!4v1627471753338!5m2!1szh-TW!2stw',
                     '25.091499723691214',
                     '121.52713299999999',
                     'https://www.instagram.com/roncafebar/',
                     'https://www.instagram.com/explore/locations/236229885/ron/'])
    
    writer.writerow(['溫柔鄉 (The Tender Land)',
                     '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.1889551076865!2d121.530676!3d25.061584000000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a95be5148383%3A0x8b8858c840e8eab0!2z5rqr5p-U6YSJIChUaGUgVGVuZGVyIExhbmQp!5e0!3m2!1szh-TW!2stw!4v1627471821239!5m2!1szh-TW!2stw" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
                     'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.1889551076865!2d121.530676!3d25.061584000000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a95be5148383%3A0x8b8858c840e8eab0!2z5rqr5p-U6YSJIChUaGUgVGVuZGVyIExhbmQp!5e0!3m2!1szh-TW!2stw!4v1627471821239!5m2!1szh-TW!2stw',
                     '25.06161801561434',
                     '121.53064381348997',
                     'https://www.instagram.com/thetenderland_taipei/',
                     'https://www.instagram.com/explore/locations/1029800321/'])
    
    # close csv
    csvfile.close()
    
    # add index column
    bar=pd.read_csv('bar.csv',header=0)
    bar=bar.rename_axis('index').reset_index()
    store=pd.DataFrame(bar)
    store.to_csv(path,encoding='utf-8')
