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
	$(CURL) http://dl.dropbox.com/u/12470785/maxmind/GeoIP.dat.gz
	mv $(GEOIP_DAT_GZ) data/

data/$(GEOLITECITY_DAT_GZ):
	$(CURL) http://dl.dropbox.com/u/12470785/maxmind/GeoLiteCity.dat.gz
	mv $(GEOLITE_DAT_GZ) data/

clean:
	-$(RM) geoservice/*.pyc

distclean: clean
	-$(RM) data/ geoservice/geo/*.dat
