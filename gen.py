import numpy as np
import pandas as pd
import random
import math

random.seed("Spooks")

def roll_dX(X):
 return random.choice(list(range(X)))+1

#

def p_roll_dX(X):
 op = {}
 for i in range(X):
  op[i+1] = 1.0/X
 return op

def app(dyct,key,val):
 if key in dyct:
  dyct[key]+=val
 else:
  dyct[key]=val
 return dyct

def p_add(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey+bkey, a[akey]*b[bkey])
 return op

def p_subtract(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey-bkey, a[akey]*b[bkey])
 return op

def p_multiply(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey*bkey, a[akey]*b[bkey])
 return op

def p_divide(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey/bkey, a[akey]*b[bkey])
 return op

def p_min(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, min(akey,bkey), a[akey]*b[bkey])
 return op

def p_max(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, max(akey,bkey), a[akey]*b[bkey])
 return op

def p_ave(a):
 op = 0
 for akey in a:
  op+=a[akey]*akey
 return op

#

def normalize(dyct):
    tot = sum(dyct.values())
    return {k: v / tot for k, v in dyct.items()}

def update(pDist, explDists, value):
 newPDist={}
 for outcome in pDist:
  if outcome in explDists:
   if value in explDists[outcome]:
    newPDist[outcome] = pDist[outcome]*explDists[outcome][value]
 return normalize(newPDist)

###
###
###

def get_inte():
 return roll_dX(80) + min(roll_dX(20),roll_dX(20))

def get_host():
 return roll_dX(80) + min(roll_dX(10), roll_dX(10)) + roll_dX(10)

def get_corp():
 return roll_dX(60) + roll_dX(20) + min(roll_dX(20),roll_dX(20))

def get_slim(corp):
 return round(corp/5) + roll_dX(60) + min(roll_dX(20), roll_dX(20))

def get_grot(host,corp):
 return min(roll_dX(20),round(host/5)) + round(corp/10) + roll_dX(10) + roll_dX(60)

def get_devi(inte):
 return round(inte/10) + roll_dX(10) + roll_dX(80)

def get_perv():
 return roll_dX(60) + min(roll_dX(40), roll_dX(40))

def get_para():
 return roll_dX(100)

def get_unho():
 return roll_dX(60)+roll_dX(40)

#

def get_inte_dist(gt="Spirit"):
 raw = p_add(p_roll_dX(80), p_min(p_roll_dX(20),p_roll_dX(20)))
 op=raw
 if gt=="Horror":
  op = p_max(p_max(raw,raw),raw)
 if gt=="Wisp":
  op = p_min(p_min(raw,raw),raw)
 return op

def get_host_dist(gt="Spirit"):
 raw = p_add(p_roll_dX(80), p_add(p_roll_dX(10),p_min(p_roll_dX(10),p_roll_dX(10))))
 op=raw
 if gt=="Horror":
  op = p_max(p_max(raw,raw),raw)
 if gt=="Wisp":
  op = p_min(p_min(raw,raw),raw)
 return op

def get_corp_dist(gt="Spirit"):
 raw = p_add(p_add(p_roll_dX(60),p_roll_dX(20)), p_min(p_roll_dX(20),p_roll_dX(20)))
 op=raw
 if gt=="Horror":
  op = p_max(p_max(raw,raw),raw)
 if gt=="Wisp":
  op = p_min(p_min(raw,raw),raw)
 return op
 
def get_slim_dist(corp, gt="Spirit"):
 cdist = {round(corp/5):1}
 raw = p_add(cdist, p_add(p_roll_dX(60),p_roll_dX(20)))
 op=raw
 if gt=="Horror":
  op = p_max(p_max(raw,raw),raw)
 if gt=="Wisp":
  op = p_min(p_min(raw,raw),raw)
 return op

def get_grot_dist(host, corp, gt="Spirit"):
 hdist = {round(host/5):1}
 cdist = {round(corp/10):1}
 raw = p_add(p_add(p_min(p_roll_dX(20),hdist),cdist), p_add(p_roll_dX(10),p_roll_dX(60)))
 op=raw
 if gt=="Horror":
  op = p_max(p_max(raw,raw),raw)
 if gt=="Wisp":
  op = p_min(p_min(raw,raw),raw)
 return op

def get_devi_dist(inte, gt="Spirit"):
 idist = {round(inte/10):1}
 raw = p_add(idist, p_add(p_roll_dX(80),p_roll_dX(10)))
 op=raw
 if gt=="Horror":
  op = p_max(p_max(raw,raw),raw)
 if gt=="Wisp":
  op = p_min(p_min(raw,raw),raw)
 return op

def get_perv_dist(gt="Spirit"):
 raw = p_add(p_roll_dX(60),p_min(p_roll_dX(40),p_roll_dX(40)))
 op=raw
 if gt=="Horror":
  op = p_max(p_max(raw,raw),raw)
 if gt=="Wisp":
  op = p_min(p_min(raw,raw),raw)
 return op

def get_para_dist(gt="Spirit"):
 raw = p_roll_dX(100)
 op=raw
 if gt=="Horror":
  op = p_max(p_max(raw,raw),raw)
 if gt=="Wisp":
  op = p_min(p_min(raw,raw),raw)
 return op

def get_unho_dist(gt="Spirit"):
 raw = p_add(p_roll_dX(60),p_roll_dX(40))
 op=raw
 if gt=="Horror":
  op = p_max(p_max(raw,raw),raw)
 if gt=="Wisp":
  op = p_min(p_min(raw,raw),raw)
 return op

#


#fight with fists: use for corporeal slimeless spirits
def mean_pp_price(inte,host,corp,slim,grot,devi,perv,para,unho):
 return 610 - 6*corp + 41*slim + 12*perv + 8*unho

#talks things out: use for smart peaceful spirits
def mean_ww_price(inte,host,corp,slim,grot,devi,perv,para,unho):
 return 521 - 5*inte + 39*host + 15*devi + 17*para

#overwhelming power and compassion: use for ugly dumb aggressive spirits 
def mean_ss_price(inte,host,corp,slim,grot,devi,perv,para,unho):
 return 902 + 53*inte - 5*host + -4*grot + 11*devi

#bad at finishing moves: only useful if you don't know who else to call
def mean_ee_price(inte,host,corp,slim,grot,devi,perv,para,unho):
 return 351 + 7*slim + 26*perv + 17*devi + 13*para

#easily spooked: use for inoffensive sprits
def mean_dd_price(inte,host,corp,slim,grot,devi,perv,para,unho):
 return 505 + 45*grot + 12*host + 5*perv - 5*unho

#ignores scores almost entirely: use for strong ones that don't match any of the specialists
def mean_mm_price(inte,host,corp,slim,grot,devi,perv,para,unho):
 return 4000 - 18*unho

#

def actual_price(price,N=2):
 r = price%N
 p = round((price-r)/N)
 op = r+p*(N-1)+roll_dX(p)+roll_dX(p)-1
 return op

#

def truemean(func, corp, slim, intel,host,grot, espread, pspread,dspread,hspread):
 res = []
 for eloq in espread:
  for perv in pspread:
   for devi in dspread:
    for horr in hspread:
     res.append(func(corp,slim,intel,host,grot,eloq,perv, devi, horr))
 return sum(res)/len(res)

#

def gen_ghosts(N, hi=False):
 
 
 corplist=[]
 slimlist=[]
 intelist=[]
 hostlist=[]
 grotlist=[]
 
 exorcistlist=[]
 costlist=[]
 
 mmlist=[]
 sslist=[]
 pplist=[]
 eelist=[]
 ddlist=[]
 wwlist=[]
 
 pWlist=[]
 pSlist=[]
 pHlist=[]
 
 for i in range(N):
  
  category = random.choice(["Wisp"]*433+["Spirit"]*193+["Horror"]*374)
  
  if category=="Spirit":
   inte=get_inte()
   host=get_host()
   corp=get_corp()
   slim=get_slim(corp)
   grot=get_grot(host,corp)
   devi=get_devi(inte)
   perv=get_perv()
   para=get_para()
   unho=get_unho()
  if category=="Wisp":
   inte=min(get_inte(),get_inte(),get_inte())
   host=min(get_host(),get_host(),get_host())
   corp=min(get_corp(),get_corp(),get_corp())
   slim=min(get_slim(corp),get_slim(corp),get_slim(corp))
   grot=min(get_grot(host,corp),get_grot(host,corp),get_grot(host,corp))
   devi=min(get_devi(inte),get_devi(inte),get_devi(inte))
   perv=min(get_perv(),get_perv(),get_perv())
   para=min(get_para(),get_para(),get_para())
   unho=min(get_unho(),get_unho(),get_unho())
  if category=="Horror":
   inte=max(get_inte(),get_inte(),get_inte())
   host=max(get_host(),get_host(),get_host())
   corp=max(get_corp(),get_corp(),get_corp())
   slim=max(get_slim(corp),get_slim(corp),get_slim(corp))
   grot=max(get_grot(host,corp),get_grot(host,corp),get_grot(host,corp))
   devi=max(get_devi(inte),get_devi(inte),get_devi(inte))
   perv=max(get_perv(),get_perv(),get_perv())
   para=max(get_para(),get_para(),get_para())
   unho=max(get_unho(),get_unho(),get_unho())
  
  corplist.append(corp)
  slimlist.append(slim)
  intelist.append(inte)
  hostlist.append(host)
  grotlist.append(grot)
  
  #
  
  mm = mean_mm_price(inte,host,corp,slim,grot,devi,perv,para,unho)
  ss = mean_ss_price(inte,host,corp,slim,grot,devi,perv,para,unho)
  pp = mean_pp_price(inte,host,corp,slim,grot,devi,perv,para,unho)
  ee = mean_ee_price(inte,host,corp,slim,grot,devi,perv,para,unho)
  dd = mean_dd_price(inte,host,corp,slim,grot,devi,perv,para,unho)
  ww = mean_ww_price(inte,host,corp,slim,grot,devi,perv,para,unho)
  
  exorcist = random.choice(["Mundanifying Mystics"]*237+["Spectre Slayers"]*102+["Phantom Pummelers"]*150+["Entity Eliminators"]*161+["Demon Destroyers"]*221+["Wraith Wranglers"]*129)
  exorcistlist.append(exorcist)
  
  if exorcist.startswith("M"):
   costlist.append(actual_price(mm))
  if exorcist.startswith("S"):
   costlist.append(actual_price(ss))
  if exorcist.startswith("P"):
   costlist.append(actual_price(pp))
  if exorcist.startswith("E"):
   costlist.append(actual_price(ee))
  if exorcist.startswith("D"):
   costlist.append(actual_price(dd))
  if exorcist.startswith("W"):
   costlist.append(actual_price(ww))
  
  
  #
  
  if hi:
   
   prior = {"Wisp":0.433, "Spirit":0.193, "Horror":0.374}
   
   inteUpdater = {"Wisp":get_inte_dist("Wisp"),"Spirit":get_inte_dist("Spirit"),"Horror":get_inte_dist("Horror")}
   prior = update(prior,inteUpdater,inte)
   
   hostUpdater = {"Wisp":get_host_dist("Wisp"),"Spirit":get_host_dist("Spirit"),"Horror":get_host_dist("Horror")}
   prior = update(prior,hostUpdater,host)
   
   corpUpdater = {"Wisp":get_corp_dist("Wisp"),"Spirit":get_corp_dist("Spirit"),"Horror":get_corp_dist("Horror")}
   prior = update(prior,corpUpdater,inte)
   
   slimUpdater = {"Wisp":get_slim_dist(corp,"Wisp"),"Spirit":get_slim_dist(corp,"Spirit"),"Horror":get_slim_dist(corp,"Horror")}
   prior = update(prior,slimUpdater,slim)
   
   grotUpdater = {"Wisp":get_grot_dist(host,corp,"Wisp"),"Spirit":get_grot_dist(host,corp,"Spirit"),"Horror":get_grot_dist(host,corp,"Horror")}
   prior = update(prior,grotUpdater,grot)
   
   #print(prior)
   
   deviMeanW = p_ave(get_devi_dist(inte,"Wisp"))
   pervMeanW = p_ave(get_perv_dist("Wisp"))
   paraMeanW = p_ave(get_para_dist("Wisp"))
   unhoMeanW = p_ave(get_unho_dist("Wisp"))
   
   deviMeanS = p_ave(get_devi_dist(inte,"Spirit"))
   pervMeanS = p_ave(get_perv_dist("Spirit"))
   paraMeanS = p_ave(get_para_dist("Spirit"))
   unhoMeanS = p_ave(get_unho_dist("Spirit"))
   
   deviMeanH = p_ave(get_devi_dist(inte,"Horror"))
   pervMeanH = p_ave(get_perv_dist("Horror"))
   paraMeanH = p_ave(get_para_dist("Horror"))
   unhoMeanH = p_ave(get_unho_dist("Horror"))
   
   #I love how easy lin reg makes the final step: mean(f(x))=f(mean(x))
   
   mm = 0
   if "Wisp" in prior:
    mm += prior["Wisp"]*mean_mm_price(inte,host,corp,slim,grot,deviMeanW,pervMeanW,paraMeanW,unhoMeanW)
   if "Spirit" in prior:
    mm += prior["Spirit"]*mean_mm_price(inte,host,corp,slim,grot,deviMeanS,pervMeanS,paraMeanS,unhoMeanS)
   if "Horror" in prior:
    mm += prior["Horror"]*mean_mm_price(inte,host,corp,slim,grot,deviMeanH,pervMeanH,paraMeanH,unhoMeanH)
   
   ss = 0
   if "Wisp" in prior:
    ss += prior["Wisp"]*mean_ss_price(inte,host,corp,slim,grot,deviMeanW,pervMeanW,paraMeanW,unhoMeanW)
   if "Spirit" in prior:
    ss += prior["Spirit"]*mean_ss_price(inte,host,corp,slim,grot,deviMeanS,pervMeanS,paraMeanS,unhoMeanS)
   if "Horror" in prior:
    ss += prior["Horror"]*mean_ss_price(inte,host,corp,slim,grot,deviMeanH,pervMeanH,paraMeanH,unhoMeanH)
   
   pp = 0
   if "Wisp" in prior:
    pp += prior["Wisp"]*mean_pp_price(inte,host,corp,slim,grot,deviMeanW,pervMeanW,paraMeanW,unhoMeanW)
   if "Spirit" in prior:
    pp += prior["Spirit"]*mean_pp_price(inte,host,corp,slim,grot,deviMeanS,pervMeanS,paraMeanS,unhoMeanS)
   if "Horror" in prior:
    pp += prior["Horror"]*mean_pp_price(inte,host,corp,slim,grot,deviMeanH,pervMeanH,paraMeanH,unhoMeanH)
   
   ee = 0
   if "Wisp" in prior:
    ee += prior["Wisp"]*mean_ee_price(inte,host,corp,slim,grot,deviMeanW,pervMeanW,paraMeanW,unhoMeanW)
   if "Spirit" in prior:
    ee += prior["Spirit"]*mean_ee_price(inte,host,corp,slim,grot,deviMeanS,pervMeanS,paraMeanS,unhoMeanS)
   if "Horror" in prior:
    ee += prior["Horror"]*mean_ee_price(inte,host,corp,slim,grot,deviMeanH,pervMeanH,paraMeanH,unhoMeanH)
   
   dd = 0
   if "Wisp" in prior:
    dd += prior["Wisp"]*mean_dd_price(inte,host,corp,slim,grot,deviMeanW,pervMeanW,paraMeanW,unhoMeanW)
   if "Spirit" in prior:
    dd += prior["Spirit"]*mean_dd_price(inte,host,corp,slim,grot,deviMeanS,pervMeanS,paraMeanS,unhoMeanS)
   if "Horror" in prior:
    dd += prior["Horror"]*mean_dd_price(inte,host,corp,slim,grot,deviMeanH,pervMeanH,paraMeanH,unhoMeanH)
   
   ww = 0
   if "Wisp" in prior:
    ww += prior["Wisp"]*mean_ww_price(inte,host,corp,slim,grot,deviMeanW,pervMeanW,paraMeanW,unhoMeanW)
   if "Spirit" in prior:
    ww += prior["Spirit"]*mean_ww_price(inte,host,corp,slim,grot,deviMeanS,pervMeanS,paraMeanS,unhoMeanS)
   if "Horror" in prior:
    ww += prior["Horror"]*mean_ww_price(inte,host,corp,slim,grot,deviMeanH,pervMeanH,paraMeanH,unhoMeanH)
  
   mmlist.append(mm)
   sslist.append(ss)
   pplist.append(pp)
   eelist.append(ee)
   ddlist.append(dd)
   wwlist.append(ww)
   
   pWlist.append(prior["Wisp"])
   pSlist.append(prior["Spirit"])
   pHlist.append(prior["Horror"])
  
  
 #
 
 if hi: 
  df = pd.DataFrame({"Corporeality":corplist,"Sliminess":slimlist,"Intellect":intelist,"Hostility":hostlist,"Grotesqueness":grotlist,"MM":mmlist, "SS":sslist, "PP":pplist, "EE":eelist, "DD":ddlist, "WW":wwlist, "pWisp":pWlist, "pSpirit":pSlist, "pHorror":pHlist})
 else: 
  df = pd.DataFrame({"Corporeality":corplist,"Sliminess":slimlist,"Intellect":intelist,"Hostility":hostlist,"Grotesqueness":grotlist,"Exorcist Hired":exorcistlist,"Cost of Exorcism (sp)":costlist})
 
 if hi:
  Alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  cpDict = {}
  ktDict = {}
  avDict = {}
  for i in range(len(corplist)):
   cpDict[Alphabet[i]] = {"pWisp":pWlist[i], "pHorror":pHlist[i]}
   ktDict[Alphabet[i]] = {"corp":corplist[i],"slim":slimlist[i],"inte":intelist[i],"host":hostlist[i],"grot":grotlist[i]}
   avDict[Alphabet[i]] = {"MM":mmlist[i], "SS":sslist[i], "PP":pplist[i], "EE":eelist[i], "DD":ddlist[i], "WW":wwlist[i]}
  print(cpDict)
  print(ktDict)
  print(avDict)
 
 return df

trainDf = gen_ghosts(34374)
trainDf.to_csv("pulled_records.csv")

testDf = gen_ghosts(23,True)
testDf.to_csv("ghosts.csv")

if False:
 for DD in [True,False]:
  for FEUD in ["PP","SS"]:
   kept = ["EE", "WW"] + [FEUD]
   if DD:
    kept = kept+["DD"]
   testDf["bestNP"] = testDf[kept].min(axis=1)
   testDf["MMdiff"] = testDf["bestNP"]-testDf["MM"]
   MMbonusRows = testDf[testDf["MMdiff"]>0]["MMdiff"].nlargest(2)
   print(MMbonusRows)
   minc = sum(testDf["bestNP"]) + DD*100 + sum(testDf["MMdiff"].iloc[MMbonusRows.index])
   print(DD,FEUD,minc)
