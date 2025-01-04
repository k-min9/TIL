# realease의 tag(0.7.1)에 등록된 source code 다운로드
wget --no-check-certificate --content-disposition https://github.com/joyent/node/tarball/v0.7.1
# --no-check-cerftificate was necessary for me to have wget not puke about https
curl -LJO https://github.com/joyent/node/tarball/v0.7.1