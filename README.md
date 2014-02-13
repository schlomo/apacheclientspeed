apacheclientspeed
=================

Apache Log Analysis to Measure Client Download Speed

Installation & Usage
--------------------

1. Append "%D" to the Apache Access Log, e.g. like this:

  ```
  LogFormat "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\" %D" combined
  ```
1. Make sure that the exact same [Apache Log Format](http://httpd.apache.org/docs/current/mod/mod_log_config.html#formats) defintion is also set in the source code (`__main__.py`).

1. Feed the Python script access log lines. In this example I only care about the download speed of videos:

  ```
  $ grep mp4 /var/log/apache2/access.log | tail -n 20 | python -m apacheclientspeed
  217.111.70.208 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 1409 KiloByte/s
  217.111.70.208 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 119 KiloByte/s
  217.111.70.208 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 1936 KiloByte/s
  217.111.70.208 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 90 KiloByte/s
  217.111.70.208 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 159 KiloByte/s
  217.111.70.208 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 83 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 2067 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 43226 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 4 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 33491 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 28 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 0 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 0 KiloByte/s
  89.204.139.1 GET /c/g2/GANGNAM_320_Rf_28.mp4 HTTP/1.1 0 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 0 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 0 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 0 KiloByte/s
  89.204.139.1 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 0 KiloByte/s
  217.111.70.208 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 507 KiloByte/s
  80.226.1.16 GET /c/g1/GANGNAM_320_Rf_30.mp4 HTTP/1.1 46 KiloByte/s
  ```

TODO
----

* Autodetect log format for given apache log file


License
-------

This code is licensed under the GPL, see included LICENSE.

The included [apachelog module](https://code.google.com/p/apachelog/) is licensed under as "Artistic License/GPL".
