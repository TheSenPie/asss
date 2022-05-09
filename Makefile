NAME = assss
WHATWEB = whatweb
PREFIX ?= /usr
BINPATH = $(PREFIX)/bin
LIBPATH = $(PREFIX)/share

ifeq "$(PLATFORM)" ""
PLATFORM := $(shell uname)
endif

ifeq "$(PLATFORM)" "Darwin"
INSTALLD =
PREFIX ?= /usr/local
else
INSTALLD = -D
endif

install:
	# upgrade/installation will leave the my-plugins folder
	rm -Rf $(DESTDIR)$(BINPATH)/$(NAME)
	rm -Rf $(WHATWEB)

	cd src && python3 setup.py install
	git clone https://github.com/urbanadventurer/WhatWeb.git $(WHATWEB) && cd $(WHATWEB) && $(MAKE) install

clean:
	# clean will remove your my-plugins folder. be warned
	cd src && python3 setup.py install --record files.txt && xargs rm -rf < files.txt && rm -f files.txt
	cd whatweb && $(MAKE) clean
