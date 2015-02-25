# -*- coding: utf-8 -*-
import os, urllib, xbmc, zipfile

def ExtractAll(_in, _out):
	try:
		zin = zipfile.ZipFile(_in, 'r')
		zin.extractall(_out)
	except Exception, e:
		print str(e)
		return False

	return True
	
def DocRepo():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.docshadrach')):
		return
		
	url = "https://github.com/XBMCSpot/docshadrach.repository/raw/master/zips/repository.docshadrach-1.0.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")


def Anon():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.anonymous')):
		return
		
	url = "http://anonymous-repo.googlecode.com/svn/trunk/repository.anonymous.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	
	
def Bromix():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.bromix')):
		return
		
	url = "https://github.com/bromix/repository.bromix.storage/blob/master/repository.bromix/repository.bromix-1.2.2.zip?raw=true"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")


def Kinkin():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.Kinkin')):
		return
		
	url = "http://fusion.tvaddons.ag/xbmc-repos/repository.Kinkin-1.2.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")


def Lambda():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.lambda')):
		return
		
	url = "http://fusion.tvaddons.ag/xbmc-repos/repository.lambda-1.0.9.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")


def Metal():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.metalkettle')):
		return
		
	url = "https://github.com/metalkettle/MetalKettles-Addon-Repository/blob/master/zips/repository.metalkettle/repository.metalkettle-1.4.3.zip?raw=true"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")


def Enen():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.p2p-streams.xbmc')):
		return
		
	url = "http://fusion.tvaddons.ag/xbmc-repos/repository.p2p-streams.xbmc-1.0.3.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	

def Pulsar():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.pulsarunofficialmirror')):
		return
		
	url = "https://github.com/iCanuck/Unofficial-Pulsar-Repo-Mirror/blob/master/repository.pulsarunofficialmirror/repository.pulsarunofficialmirror-1.0.0.zip?raw=true"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")


def Shani():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.shani')):
		return
		
	url = "http://fusion.tvaddons.ag/xbmc-repos/repository.shani-2.5.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	

def Highway():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.thehighway')):
		return
		
	url = "http://fusion.tvaddons.ag/xbmc-repos/repository.thehighway-0.0.4.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	
	
def Theyid():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.TheYid')):
		return
		
	url = "http://fusion.tvaddons.ag/xbmc-repos/repository.TheYid-1.7.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	
	
def Tknorris():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.tknorris.release')):
		return
		
	url = "http://fusion.tvaddons.ag/xbmc-repos/repository.tknorris.release-1.0.1.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	

def Tknorrisb():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.tknorris.beta')):
		return
		
	url = "https://github.com/tknorris/tknorris-beta-repo/blob/master/zips/repository.tknorris.beta/repository.tknorris.beta-1.0.1.zip?raw=true"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	

def Total():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.totalinstaller')):
		return
		
	url = "http://i.totalxbmc.tv/repository.totalinstaller.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")


def Tvaddons():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.xbmchub')):
		return
		
	url = "http://fusion.tvaddons.ag/xbmc-repos/repository.xbmchub-1.0.5.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")


def Israeli():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.xbmc-israel')):
		return
		
	url = "https://github.com/cubicle-vdo/xbmc-israel/raw/master/repo/repository.xbmc-israel/repository.xbmc-israel-1.0.4.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")


def Xunity():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.xunitytalk')):
		return
		
	url = "http://xunitytalk.com/xfinity/XunityTalk_Repository.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
