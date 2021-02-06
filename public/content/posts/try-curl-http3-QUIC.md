---
title: "Try Http3 QUIC By using CURL"
author: "linna.li"
tags: ["HTTP", "QUIC"]
categories: ["note"]
date: 2020-01-18
---

## Use ngtcp2

>"Call it TCP/2. One More Time."

ngtcp2 project is an effort to implement QUIC protocol which is now being discussed in IETF QUICWG for its standardization.

### Build

Build OpenSSL

```md
git clone --depth 1 -b openssl-quic-draft-23 https://github.com/tatsuhiro-t/openssl
cd openssl
./config enable-tls1_3 --prefix=/usr/local/include/openssl
make
make install_sw
```

Build nghttp3

Make sure you have installed automake and autoconf

```md
git clone https://github.com/ngtcp2/nghttp3
cd nghttp3
autoreconf -i
./configure --prefix=/usr/local/include/nghttp3 --enable-lib-only
make
make install
```

Build ngtcp2

```md
cd ..
git clone https://github.com/ngtcp2/ngtcp2
cd ngtcp2
autoreconf -i
./configure PKG_CONFIG_PATH=/usr/local/include/openssl/lib/pkgconfig:/usr/local/include/nghttp3/lib/pkgconfig LDFLAGS="-Wl,-rpath,/usr/local/include/openssl/lib" --prefix=/usr/local/include/ngtcp2/
make
make install
```

Build curl

```md
cd ..
git clone https://github.com/curl/curl
cd curl
./buildconf
LDFLAGS="-Wl,-rpath,/usr/local/include/openssl/lib" ./configure --with-ssl=/usr/local/include/openssl --with-nghttp3=/usr/local/include/nghttp3 --with-ngtcp2=/usr/local/include/ngtcp2
make
```

### Run

```md
curl --http3 https://www.facebook.com/ -v -o /dev/null
```

### Compare

http3 is faster in connecting than http2

(QUIC is fatster than TLS1.3)

```md
/**
 * time_appconnect The time, in seconds, it took from the start until the SSL/SSH/etc       connect/handshake to the remote host was completed. (Added in 7.19.0)
* time_connect The time, in seconds, it took from the start until the TCP connect to the remote host (or proxy) was completed.
**/

curl --http3 -i https://www.facebook.com/ -v -s -o output -w 'connect: %{time_connect} sec\ntime_appconnect: %{time_appconnect} sec\ntotal: %{time_total} sec\n'

10 times average: 
Connection #0 to host www.facebook.com left intact
connect: 0.000000 sec
time_appconnect: 0.000000 sec
total: 0.239049 sec

curl --http2 -i https://www.facebook.com/ -v -s -o output -w 'connect: %{time_connect} sec\ntime_appconnect: %{time_appconnect} sec\ntotal: %{time_total} sec\n'

10 times average: 
connect: 0.009577 sec
time_appconnect: 0.027397 sec
total: 0.333672 sec
```

### Problem i had

* i refered to this for doing install, https://github.com/curl/curl/blob/master/docs/HTTP3.md

Need to memo <somewhere1>, <somewhere2>, <somewhere3>

* sudo mkdir in /usr/, Operation not permitted.

Refer to: https://qiita.com/iwaseasahi/items/9d2e29b02df5cce7285d

### What i learned 

* autoreconf = aclocal + automake -a + autoconf, used for making source directory have valid format.

* --prefix : install path

* enable-lib-only: only build 
* make, make install: make=read command from Makefile, then compile, make install = install



# 























