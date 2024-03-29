# RANs

## Open Air Interface 
[OpenAirInteface](oai/README.md)
For our testing it was used the tag 2023.w50.
### How to Build

+ [UHD - Build Instructions](https://files.ettus.com/manual/page_build_guide.html)
+ [OAI - Build Instructions(No E2Agent)](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/BUILD.md)
+ [OAI - Build Instructions(Flexric)](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/openair2/E2AP/README.md)

#### Build with Flexric
In this setup we have used oai built with the _--build-e2_ flag.
```shell

## 0.1 Building Swig

$ git clone https://github.com/swig/swig.git && cd swig
$ git checkout release-4.1
$ ./autogen.sh
$ ./configure --prefix=/usr/
$ make -j12
$ sudo make install

## 0.2 Required dependencies

$ sudo apt install libsctp-dev python3 cmake-curses-gui libpcre2-dev

## 1. Building OAI

$ git clone https://gitlab.eurecom.fr/oai/openairinterface5g oai
$ cd oai
$ git checkout 2023.w50
$ ./build_oai -w USRP --gNB --nrUE --build-e2 --ninja

## 2. Building Flexric

$ cd oai/openair2/E2AP/flexric
$ mkdir build && cd build 
$ cmake -D CMAKE_C_COMPILER=gcc-10 -D CMAKE_CXX_COMPILER=g++-10 ..
$ make -j8
$ sudo make install 

```
