# GNU Makefile

RM=rm -rf 
CURL=curl -O
GUNZIP=gunzip -f
GEOIP_DAT=GeoIP.dat
GEOLITECITY_DAT=GeoLiteCity.dat
GEOIP_DAT_GZ=GeoIP.dat.gz
GEOLITECITY_DAT_GZ=GeoLiteCity.dat.gz
MKDIR=mkdir -p

.PHONY: all clean distclean init fetch_data

all: fetch_data

init:
	-$(MKDIR) data/

fetch_data: init data/$(GEOLITECITY_DAT_GZ) data/$(GEOIP_DAT_GZ)
	cp data/*.gz geoservice/geo/
	$(GUNZIP) geoservice/geo/*.gz

data/$(GEOIP_DAT_GZ):
	$(CURL) http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
	mv *.gz data/

data/$(GEOLITECITY_DAT_GZ):
	$(CURL) http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
	mv *.gz data/

clean:
	-$(RM) geoservice/*.pyc

distclean: clean
	-$(RM) data/ geoservice/geo/*.dat
